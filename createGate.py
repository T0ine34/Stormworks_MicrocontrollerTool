from createNode import create_input_node, create_output_node, TYPES
import xml.etree.ElementTree as ET
from svgGate import AND, OR, XOR, NOT, NAND, NOR, XNOR, BUFFER

DATA = {
    "AND": {
        "inputs": {
            "A": TYPES.LOGIC,
            "B": TYPES.LOGIC
        },
        "outputs": {
            "A AND B": TYPES.LOGIC
        },
    },
    "OR": {
        "inputs": {
            "A": TYPES.LOGIC,
            "B": TYPES.LOGIC
        },
        "outputs": {
            "A OR B": TYPES.LOGIC
        },
    },
    "BUFFER": {
        "inputs": {
            "A": TYPES.LOGIC
        },
        "outputs": {
            "A": TYPES.LOGIC
        },
    },
    "XOR": {
        "inputs": {
            "A": TYPES.LOGIC,
            "B": TYPES.LOGIC
        },
        "outputs": {
            "A XOR B": TYPES.LOGIC
        },
    },
    "NOT": {
        "inputs": {
            "A": TYPES.LOGIC
        },
        "outputs": {
            "NOT A": TYPES.LOGIC
        },
    },
    "NAND": {
        "inputs": {
            "A": TYPES.LOGIC,
            "B": TYPES.LOGIC
        },
        "outputs": {
            "A NAND B": TYPES.LOGIC
        },
    },
    "NOR": {
        "inputs": {
            "A": TYPES.LOGIC,
            "B": TYPES.LOGIC
        },
        "outputs": {
            "A NOR B": TYPES.LOGIC
        },
    },
    "XNOR": {
        "inputs": {
            "A": TYPES.LOGIC,
            "B": TYPES.LOGIC
        },
        "outputs": {
            "A XNOR B": TYPES.LOGIC
        },
    }
}

def create_item(gate : callable):
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


if __name__ == '__main__':
    import os
    for gate in [AND, OR, XOR, NOT, NAND, NOR, XNOR, BUFFER]:
        item = create_item(gate)
        os.makedirs('./output', exist_ok=True)
        svg = ET.Element('svg', xmlns='http://www.w3.org/2000/svg', version='1.1', width='512', height='512')
        item.set('transform', 'translate(32, 32)')
        svg.append(item)
        root = ET.ElementTree(svg)
        root.write(f'./output/{gate.__name__}.svg')