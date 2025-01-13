from createNode import create_input_node, create_output_node, TYPES
from PIL import Image



class Gate:
    def __init__(self, name : str, icon : Image.Image):
        self.inputs = []
        self.outputs = []
        self.name = name
        self.icon = None
        
    def addInput(self, type : TYPES, name : str):
        self.inputs.append(create_input_node(type, name))
    
    def addOutput(self, type : TYPES, name : str):
        self.outputs.append(create_output_node(type, name))
        
    

