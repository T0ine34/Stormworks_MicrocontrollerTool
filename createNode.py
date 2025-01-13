import os
from sre_constants import IN
from PIL import Image, ImageDraw
from memory import Memory
from enum import StrEnum

import xml.etree.ElementTree as ET


# logic : red
# number : green
# composite : purple
# video : light blue
# audio : yellowish, brownish

class TYPES(StrEnum):
    LOGIC = 'logic'
    NUMBER = 'number'
    COMPOSITE = 'composite'
    VIDEO = 'video'
    AUDIO = 'audio'

COLORS = {
    TYPES.LOGIC : (255, 0, 0),
    TYPES.NUMBER : (0, 255, 0),
    TYPES.COMPOSITE : (129, 20, 196),
    TYPES.VIDEO : (0, 255, 255),
    TYPES.AUDIO : (189, 126, 43)
}

IMG_SIZE = (512, 512)

OUT_CIRCLE_RADIUS = 255
IN_CIRCLE_RADIUS = 127


@Memory
def create_input_node(type : TYPES):
    color = COLORS.get(type)
    img = ET.Element('svg', xmlns='http://www.w3.org/2000/svg', version='1.1', width='512', height='512')
    circle = ET.SubElement(img, 'circle', cx='256', cy='256', r='255', fill=f'rgb{color}', stroke='black', stroke_width='5')
    circle = ET.SubElement(img, 'circle', cx='256', cy='256', r='127', fill='white', stroke='black', stroke_width='5')
    return img

@Memory
def create_output_node(type : TYPES):
    color = COLORS.get(type)
    img = ET.Element('svg', xmlns='http://www.w3.org/2000/svg', version='1.1', width='512', height='512')
    circle = ET.SubElement(img, 'circle', cx='256', cy='256', r='127', fill=f'rgb{color}', stroke='black', stroke_width='5')
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

