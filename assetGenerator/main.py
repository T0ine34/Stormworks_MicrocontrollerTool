from createNode import create_input_node, create_output_node
from svgGate import AND, OR, XOR, NOT, NAND, NOR, XNOR, BUFFER
from data import DATA

import os
import xml.etree.ElementTree as ET
from typing import Callable


def create_item(gate : Callable) -> ET.Element:
    """Create a gate item, with inputs and outputs nodes corresponding to the gate
    The gived gate must be in the DATA dictionnary

    Args:
        gate (callable): The gate to create (a function taking no arguments and returning a tuple (gate_img, input_coords, output_coords)). This function should create the gate svg image, and return the coordinates of the inputs and outputs nodes

    Raises:
        ValueError: If the gate is not in the DATA dictionnary

    Returns:
        xml.etree.ElementTree.Element: The gate item
    """
    if gate.__name__ not in DATA.keys():
        raise ValueError(f'Gate {gate.__name__} not found in DATA')
    data = DATA[gate.__name__]
    inputs = [create_input_node(data["inputs"][name]) for name in data["inputs"]] #type: list[ET.Element]
    outputs = [create_output_node(data["outputs"][name]) for name in data["outputs"]]
    gate_img, input_coords, output_coords = gate()

    height = 50*max(len(inputs), len(outputs), 1)+10
    input_nodes_heights = [(height//2 - 50*len(inputs)//2 + 50*i)+12.5 for i in range(len(inputs))]
    output_nodes_heights = [(height//2 - 50*len(outputs)//2 + 50*i)+12.5 for i in range(len(outputs))]

    # the returned item
    item = ET.Element('g')
    ET.SubElement(item, 'rect', x='0', y='0', width = '128', height = str(height), fill='white', stroke='black').set('stroke-width', '5')

    # gate image
    gate_img.set('transform', f'translate(25 {height//2 - 30})')
    item.append(gate_img)
    
    # link between input node and gate
    for i, input in enumerate(inputs):
        node_pos = (0, input_nodes_heights[i] + 12.5)
        gate_input_pos = (input_coords[i][0] + 25, input_coords[i][1] + height//2 - 30)
        group = ET.Element('g')
        ET.SubElement(group, 'line', x1=str(node_pos[0]), y1=str(node_pos[1]), x2=str(gate_input_pos[0]), y2=str(node_pos[1]), stroke='black').set('stroke-width', '3')
        ET.SubElement(group, 'circle', cx=str(gate_input_pos[0]), cy=str(node_pos[1]), r='1.5', fill='black')
        ET.SubElement(group, 'line', x1=str(gate_input_pos[0]), y1=str(node_pos[1]), x2=str(gate_input_pos[0]), y2=str(gate_input_pos[1]), stroke='black').set('stroke-width', '3')
        ET.SubElement(group, 'circle', cx=str(gate_input_pos[0]), cy=str(gate_input_pos[1]), r='1.5', fill='black')
        item.append(group)
        
    # link between gate and output node
    for i, output in enumerate(outputs):
        node_pos = (128, output_nodes_heights[i] + 12.5)
        gate_output_pos = (output_coords[i][0] + 25, output_coords[i][1] + height//2 - 30)
        group = ET.Element('g')
        ET.SubElement(group, 'circle', cx=str(gate_output_pos[0]), cy=str(gate_output_pos[1]), r='1.5', fill='black')
        ET.SubElement(group, 'line', x1=str(gate_output_pos[0]), y1=str(gate_output_pos[1]), x2=str(gate_output_pos[0]), y2=str(node_pos[1]), stroke='black').set('stroke-width', '3')
        ET.SubElement(group, 'circle', cx=str(gate_output_pos[0]), cy=str(node_pos[1]), r='1.5', fill='black')
        ET.SubElement(group, 'line', x1=str(gate_output_pos[0]), y1=str(node_pos[1]), x2=str(node_pos[0]), y2=str(node_pos[1]), stroke='black').set('stroke-width', '3')
        item.append(group)
    
    # inputs nodes
    for i, input in enumerate(inputs):
        item.append(input)
        input.set(
            'transform',
            f'translate(-12.5 {input_nodes_heights[i]}) scale(0.05, 0.05)',
        )

    # outputs nodes
    for i, output in enumerate(outputs):
        item.append(output)
        output.set(
            'transform',
            f'translate(115 {output_nodes_heights[i]}) scale(0.05, 0.05)',
        )

    return item


def save_item(gate : Callable, output_dir : str = './output'):    
    objSvg = ET.Element('svg', xmlns='http://www.w3.org/2000/svg', version='1.1', width='512', height='512')
    iconSvg = ET.Element('svg', xmlns='http://www.w3.org/2000/svg', version='1.1', width='80', height='80')
    
    object = create_item(gate)
    object.set('transform', 'translate(32, 32)')
    objSvg.append(object)
    
    icon = gate()[0]
    icon.set('transform', 'translate(0, 10)')
    iconSvg.append(icon)
    
    os.makedirs(f'{output_dir}/{gate.__name__}', exist_ok=True)
    
    ET.ElementTree(objSvg).write(f'{output_dir}/{gate.__name__}/object.svg')
    ET.ElementTree(iconSvg).write(f'{output_dir}/{gate.__name__}/icon.svg')
    
    print(f'{os.path.abspath(output_dir)}/{gate.__name__} created')

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Create a svg image for each gate')
    parser.add_argument('output', type=str, help='The output directory', default='./output', nargs='?')
    args = parser.parse_args()
    
    output_dir = args.output
    
    for gate in [AND, OR, XOR, NOT, NAND, NOR, XNOR, BUFFER]:
        save_item(gate, output_dir)