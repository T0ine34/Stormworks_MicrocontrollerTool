import xml.etree.ElementTree as ET
from memory import Memory

@Memory
def AND():
    # Create the root SVG element
    svg = ET.Element('svg', width='100', height='60', xmlns='http://www.w3.org/2000/svg')
    
    # Create the base rectangle (only the top, bottom, and left sides)
    ET.SubElement(svg, 'line', x1='10', y1='10', x2='10', y2='50', stroke='black')
    ET.SubElement(svg, 'line', x1='10', y1='10', x2='30', y2='10', stroke='black')
    ET.SubElement(svg, 'line', x1='10', y1='50', x2='30', y2='50', stroke='black')

    # Create the arc
    ET.SubElement(svg, 'path', d='M 30 10 A 20 20 0 0 1 30 50', fill='none', stroke='black')
    
    # Create the input lines
    ET.SubElement(svg, 'line', x1='0', y1='20', x2='10', y2='20', stroke='black')
    ET.SubElement(svg, 'line', x1='0', y1='40', x2='10', y2='40', stroke='black')
    
    # Create the output line
    ET.SubElement(svg, 'line', x1='50', y1='30', x2='60', y2='30', stroke='black')
    
    return svg

def OR():
    # Create the root SVG element
    svg = ET.Element('svg', width='100', height='60', xmlns='http://www.w3.org/2000/svg')
    
    # Create the base rectangle (only the top, bottom, and left sides)
    # ET.SubElement(svg, 'line', x1='10', y1='10', x2='10', y2='50', stroke='black')
    #replace by a arc
    ET.SubElement(svg, 'path', d='M 10 10 A 20 20 0 0 1 10 50', fill='none', stroke='black')
    ET.SubElement(svg, 'line', x1='10', y1='10', x2='30', y2='10', stroke='black')
    ET.SubElement(svg, 'line', x1='10', y1='50', x2='30', y2='50', stroke='black')

    # Create the arc
    ET.SubElement(svg, 'path', d='M 30 10 A 20 20 0 0 1 30 50', fill='none', stroke='black')
    
    # Create the input lines
    ET.SubElement(svg, 'line', x1='0', y1='20', x2='10', y2='20', stroke='black')
    ET.SubElement(svg, 'line', x1='0', y1='40', x2='10', y2='40', stroke='black')
    
    # Create the output line
    ET.SubElement(svg, 'line', x1='50', y1='30', x2='60', y2='30', stroke='black')
    
    return svg

if __name__ == '__main__':
    # Create the OR gate
    or_gate = OR()
    or_root = ET.ElementTree(or_gate)
    or_root.write('./output/or.svg')