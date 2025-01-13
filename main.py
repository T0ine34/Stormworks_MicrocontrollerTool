import createNode
import createLibrary

# Create a library
library = createLibrary.Library('Stormworks')
for type in createNode.COLORS.keys():
    input_node = createNode.create_input_node(type)
    output_node = createNode.create_output_node(type)
    library.addPILImage(input_node, f'{type} input')
    library.addPILImage(output_node, f'{type} output')
library.createLibrary('./output/Stormworks.xml')