from data import TYPES, COLORS

import os
import xml.etree.ElementTree as ET


def create_input_node(type : TYPES):
    color = COLORS.get(type)
    img = ET.Element('g')
    circle = ET.SubElement(img, 'circle', cx='256', cy='256', r='255', fill=f'rgb{color}', stroke='black').set('stroke-width', '25')
    circle = ET.SubElement(img, 'circle', cx='256', cy='256', r='127', fill='white', stroke='black').set('stroke-width', '25')
    return img


def create_output_node(type : TYPES):
    color = COLORS.get(type)
    img = ET.Element('g')
    circle = ET.SubElement(img, 'circle', cx='256', cy='256', r='127', fill=f'rgb{color}', stroke='black').set('stroke-width', '25')
    return img


if __name__ == '__main__':
    for type in TYPES:
        input_node = create_input_node(type)
        output_node = create_output_node(type)
        os.makedirs('./output', exist_ok=True)
        input_root = ET.ElementTree(input_node)
        output_root = ET.ElementTree(output_node)
        input_root.write(f'./output/input_{type}.svg')
        output_root.write(f'./output/output_{type}.svg')

