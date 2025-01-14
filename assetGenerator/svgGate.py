import xml.etree.ElementTree as ET


STROKE_COLOR = 'black'
STROKE_WIDTH = '3'


def AND():
    # Create the root SVG element
    svg = ET.Element('g')
    
    # Create the base rectangle (only the top, bottom, and left sides)
    ET.SubElement(svg, 'line', x1='20', y1='10', x2='20', y2='50', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='20', y1='10', x2='40', y2='10', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='20', y1='50', x2='40', y2='50', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    ET.SubElement(svg, "circle", cx="20", cy="10", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="20", cy="50", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="40", cy="10", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="40", cy="50", r="1.5", fill="black")

    # Create the arc
    ET.SubElement(svg, 'path', d='M 40 10 A 20 20 0 0 1 40 50', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the input lines
    ET.SubElement(svg, 'line', x1='0', y1='20', x2='20', y2='20', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='0', y1='40', x2='20', y2='40', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the output line
    ET.SubElement(svg, 'line', x1='60', y1='30', x2='80', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    return svg, ((0, 20), (0, 40)), ((80, 30),)

def OR():
    # Create the root SVG element
    svg = ET.Element('g')
    
    
    ET.SubElement(svg, 'path', d='M 12.5 10 A 5 10 0 0 1 12.5 50', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='12.5', y1='10', x2='40', y2='10', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='12.5', y1='50', x2='40', y2='50', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    ET.SubElement(svg, "circle", cx="12.5", cy="10", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="12.5", cy="50", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="40", cy="10", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="40", cy="50", r="1.5", fill="black")

    # Create the arc
    ET.SubElement(svg, 'path', d='M 40 10 A 30 30 0 0 1 60 30', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'path', d='M 40 50 A 30 30 0 0 0 60 30', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the input lines
    ET.SubElement(svg, 'line', x1='0', y1='20', x2='20', y2='20', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='0', y1='40', x2='20', y2='40', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the output line
    ET.SubElement(svg, 'line', x1='60', y1='30', x2='80', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    return svg, ((0, 20), (0, 40)), ((80, 30),)

def BUFFER():
    # Create the root SVG element
    svg = ET.Element('g')
    
    # Create the base rectangle (only the top, bottom, and left sides)
    ET.SubElement(svg, 'line', x1='20', y1='10', x2='20', y2='50', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='20', y1='10', x2='60', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='20', y1='50', x2='60', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    ET.SubElement(svg, "circle", cx="20", cy="10", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="20", cy="50", r="1.5", fill="black")

    # Create the input lines
    ET.SubElement(svg, 'line', x1='0', y1='30', x2='20', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the output line
    ET.SubElement(svg, 'line', x1='60', y1='30', x2='80', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    return svg, ((0, 30),), ((80, 30),)


def NAND():
    # Create the root SVG element
    svg = ET.Element('g')
    
    # Create the base rectangle (only the top, bottom, and left sides)
    ET.SubElement(svg, 'line', x1='20', y1='10', x2='20', y2='50', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='20', y1='10', x2='40', y2='10', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='20', y1='50', x2='40', y2='50', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    ET.SubElement(svg, "circle", cx="20", cy="10", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="20", cy="50", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="40", cy="10", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="40", cy="50", r="1.5", fill="black")

    # Create the arc
    ET.SubElement(svg, 'path', d='M 40 10 A 20 20 0 0 1 40 50', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the input lines
    ET.SubElement(svg, 'line', x1='0', y1='20', x2='20', y2='20', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='0', y1='40', x2='20', y2='40', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the output line
    ET.SubElement(svg, 'line', x1='70', y1='30', x2='80', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the circle at the output
    ET.SubElement(svg, 'circle', cx='65', cy='30', r='5', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    return svg, ((0, 20), (0, 40)), ((80, 30),)

def NOR():
    # Create the root SVG element
    svg = ET.Element('g')
    
    ET.SubElement(svg, 'path', d='M 12.5 10 A 5 10 0 0 1 12.5 50', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='12.5', y1='10', x2='40', y2='10', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='12.5', y1='50', x2='40', y2='50', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    ET.SubElement(svg, "circle", cx="12.5", cy="10", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="12.5", cy="50", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="40", cy="10", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="40", cy="50", r="1.5", fill="black")

    # Create the arc
    ET.SubElement(svg, 'path', d='M 40 10 A 30 30 0 0 1 60 30', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'path', d='M 40 50 A 30 30 0 0 0 60 30', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the input lines
    ET.SubElement(svg, 'line', x1='0', y1='20', x2='20', y2='20', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='0', y1='40', x2='20', y2='40', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the output line
    ET.SubElement(svg, 'line', x1='70', y1='30', x2='80', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the circle at the output
    ET.SubElement(svg, 'circle', cx='65', cy='30', r='5', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    return svg, ((0, 20), (0, 40)), ((80, 30),)

def NOT():
    # Create the root SVG element
    svg = ET.Element('g')
    
    # Create the base rectangle (only the top, bottom, and left sides)
    ET.SubElement(svg, 'line', x1='20', y1='10', x2='20', y2='50', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='20', y1='10', x2='60', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='20', y1='50', x2='60', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    ET.SubElement(svg, "circle", cx="20", cy="10", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="20", cy="50", r="1.5", fill="black")

    # Create the input lines
    ET.SubElement(svg, 'line', x1='0', y1='30', x2='20', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the output line
    ET.SubElement(svg, 'line', x1='70', y1='30', x2='80', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the circle at the output
    ET.SubElement(svg, 'circle', cx='65', cy='30', r='5', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    return svg, ((0, 30),), ((80, 30),)


def XOR():
    # Create the root SVG element
    svg = ET.Element('g')
    
    
    ET.SubElement(svg, 'path', d='M 12.5 10 A 5 10 0 0 1 12.5 50', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'path', d='M 7.5 10 A 5 10 0 0 1 7.5 50', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='12.5', y1='10', x2='40', y2='10', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='12.5', y1='50', x2='40', y2='50', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    ET.SubElement(svg, "circle", cx="12.5", cy="10", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="12.5", cy="50", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="40", cy="10", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="40", cy="50", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="7.5", cy="10", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="7.5", cy="50", r="1.5", fill="black")

    # Create the arc
    ET.SubElement(svg, 'path', d='M 40 10 A 30 30 0 0 1 60 30', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'path', d='M 40 50 A 30 30 0 0 0 60 30', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the input lines
    ET.SubElement(svg, 'line', x1='0', y1='20', x2='20', y2='20', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='0', y1='40', x2='20', y2='40', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the output line
    ET.SubElement(svg, 'line', x1='60', y1='30', x2='80', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    return svg, ((0, 20), (0, 40)), ((80, 30),)


def XNOR():
    # Create the root SVG element
    svg = ET.Element('g')
    
    
    ET.SubElement(svg, 'path', d='M 12.5 10 A 5 10 0 0 1 12.5 50', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'path', d='M 7.5 10 A 5 10 0 0 1 7.5 50', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='12.5', y1='10', x2='40', y2='10', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='12.5', y1='50', x2='40', y2='50', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    ET.SubElement(svg, "circle", cx="12.5", cy="10", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="12.5", cy="50", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="40", cy="10", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="40", cy="50", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="7.5", cy="10", r="1.5", fill="black")
    ET.SubElement(svg, "circle", cx="7.5", cy="50", r="1.5", fill="black")

    # Create the arc
    ET.SubElement(svg, 'path', d='M 40 10 A 30 30 0 0 1 60 30', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'path', d='M 40 50 A 30 30 0 0 0 60 30', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the input lines
    ET.SubElement(svg, 'line', x1='0', y1='20', x2='20', y2='20', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    ET.SubElement(svg, 'line', x1='0', y1='40', x2='20', y2='40', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the output line
    ET.SubElement(svg, 'line', x1='70', y1='30', x2='80', y2='30', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    # Create the circle at the output
    ET.SubElement(svg, 'circle', cx='65', cy='30', r='5', fill='none', stroke=STROKE_COLOR).set('stroke-width', STROKE_WIDTH)
    
    return svg, ((0, 20), (0, 40)), ((80, 30),)


if __name__ == "__main__":
    import os
    os.makedirs('output', exist_ok=True)
    for gate in [AND, OR, BUFFER, NAND, NOR, NOT, XOR, XNOR]:
        ET.ElementTree(gate()[0]).write(f'output/{gate.__name__}.svg')