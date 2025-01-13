import xml.etree.ElementTree as ET
from memory import Memory


STROKE_COLOR = 'black'
STROKE_WIDTH = '3'


@Memory
def AND():
    # Create the root SVG element
    svg = ET.Element('svg', width='100', height='60', xmlns='http://www.w3.org/2000/svg')
    
    # Create the base rectangle (only the top, bottom, and left sides)
    ET.SubElement(svg, 'line', x1='20', y1='10', x2='20', y2='50', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='20', y1='10', x2='40', y2='10', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='20', y1='50', x2='40', y2='50', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)

    # Create the arc
    ET.SubElement(svg, 'path', d='M 40 10 A 20 20 0 0 1 40 50', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the input lines
    ET.SubElement(svg, 'line', x1='0', y1='20', x2='20', y2='20', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='0', y1='40', x2='20', y2='40', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the output line
    ET.SubElement(svg, 'line', x1='60', y1='30', x2='80', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    return svg

@Memory
def OR():
    # Create the root SVG element
    svg = ET.Element('svg', width='100', height='60', xmlns='http://www.w3.org/2000/svg')
    
    
    ET.SubElement(svg, 'path', d='M 12.5 10 A 5 10 0 0 1 12.5 50', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='12.5', y1='10', x2='40', y2='10', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='12.5', y1='50', x2='40', y2='50', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)

    # Create the arc
    ET.SubElement(svg, 'path', d='M 40 10 A 30 30 0 0 1 60 30', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'path', d='M 40 50 A 30 30 0 0 0 60 30', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the input lines
    ET.SubElement(svg, 'line', x1='0', y1='20', x2='20', y2='20', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='0', y1='40', x2='20', y2='40', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the output line
    ET.SubElement(svg, 'line', x1='60', y1='30', x2='80', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    return svg

@Memory
def BUFFER():
    # Create the root SVG element
    svg = ET.Element('svg', width='100', height='60', xmlns='http://www.w3.org/2000/svg')
    
    # Create the base rectangle (only the top, bottom, and left sides)
    ET.SubElement(svg, 'line', x1='20', y1='10', x2='20', y2='50', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='20', y1='10', x2='60', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='20', y1='50', x2='60', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)

    # Create the input lines
    ET.SubElement(svg, 'line', x1='0', y1='30', x2='20', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the output line
    ET.SubElement(svg, 'line', x1='60', y1='30', x2='80', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    return svg


@Memory
def NAND():
    # Create the root SVG element
    svg = ET.Element('svg', width='100', height='60', xmlns='http://www.w3.org/2000/svg')
    
    # Create the base rectangle (only the top, bottom, and left sides)
    ET.SubElement(svg, 'line', x1='20', y1='10', x2='20', y2='50', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='20', y1='10', x2='40', y2='10', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='20', y1='50', x2='40', y2='50', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)

    # Create the arc
    ET.SubElement(svg, 'path', d='M 40 10 A 20 20 0 0 1 40 50', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the input lines
    ET.SubElement(svg, 'line', x1='0', y1='20', x2='20', y2='20', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='0', y1='40', x2='20', y2='40', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the output line
    ET.SubElement(svg, 'line', x1='70', y1='30', x2='80', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the circle at the output
    ET.SubElement(svg, 'circle', cx='65', cy='30', r='5', fill='white', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    return svg

@Memory
def NOR():
    # Create the root SVG element
    svg = ET.Element('svg', width='100', height='60', xmlns='http://www.w3.org/2000/svg')
    
    ET.SubElement(svg, 'path', d='M 12.5 10 A 5 10 0 0 1 12.5 50', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='12.5', y1='10', x2='40', y2='10', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='12.5', y1='50', x2='40', y2='50', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)

    # Create the arc
    ET.SubElement(svg, 'path', d='M 40 10 A 30 30 0 0 1 60 30', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'path', d='M 40 50 A 30 30 0 0 0 60 30', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the input lines
    ET.SubElement(svg, 'line', x1='0', y1='20', x2='20', y2='20', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='0', y1='40', x2='20', y2='40', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the output line
    ET.SubElement(svg, 'line', x1='70', y1='30', x2='80', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the circle at the output
    ET.SubElement(svg, 'circle', cx='65', cy='30', r='5', fill='white', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    return svg

@Memory
def NOT():
    # Create the root SVG element
    svg = ET.Element('svg', width='100', height='60', xmlns='http://www.w3.org/2000/svg')
    
    # Create the base rectangle (only the top, bottom, and left sides)
    ET.SubElement(svg, 'line', x1='20', y1='10', x2='20', y2='50', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='20', y1='10', x2='60', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='20', y1='50', x2='60', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)

    # Create the input lines
    ET.SubElement(svg, 'line', x1='0', y1='30', x2='20', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the output line
    ET.SubElement(svg, 'line', x1='70', y1='30', x2='80', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the circle at the output
    ET.SubElement(svg, 'circle', cx='65', cy='30', r='5', fill='white', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    return svg


@Memory
def XOR():
    # Create the root SVG element
    svg = ET.Element('svg', width='100', height='60', xmlns='http://www.w3.org/2000/svg')
    
    
    ET.SubElement(svg, 'path', d='M 12.5 10 A 5 10 0 0 1 12.5 50', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'path', d='M 7.5 10 A 5 10 0 0 1 7.5 50', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='12.5', y1='10', x2='40', y2='10', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='12.5', y1='50', x2='40', y2='50', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)

    # Create the arc
    ET.SubElement(svg, 'path', d='M 40 10 A 30 30 0 0 1 60 30', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'path', d='M 40 50 A 30 30 0 0 0 60 30', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the input lines
    ET.SubElement(svg, 'line', x1='0', y1='20', x2='20', y2='20', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='0', y1='40', x2='20', y2='40', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the output line
    ET.SubElement(svg, 'line', x1='60', y1='30', x2='80', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    return svg

@Memory
def XNOR():
    # Create the root SVG element
    svg = ET.Element('svg', width='100', height='60', xmlns='http://www.w3.org/2000/svg')
    
    
    ET.SubElement(svg, 'path', d='M 12.5 10 A 5 10 0 0 1 12.5 50', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'path', d='M 7.5 10 A 5 10 0 0 1 7.5 50', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='12.5', y1='10', x2='40', y2='10', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='12.5', y1='50', x2='40', y2='50', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)

    # Create the arc
    ET.SubElement(svg, 'path', d='M 40 10 A 30 30 0 0 1 60 30', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'path', d='M 40 50 A 30 30 0 0 0 60 30', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the input lines
    ET.SubElement(svg, 'line', x1='0', y1='20', x2='20', y2='20', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='0', y1='40', x2='20', y2='40', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the output line
    ET.SubElement(svg, 'line', x1='70', y1='30', x2='80', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the circle at the output
    ET.SubElement(svg, 'circle', cx='65', cy='30', r='5', fill='white', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    return svg
