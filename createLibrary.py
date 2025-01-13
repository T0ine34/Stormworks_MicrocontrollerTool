import xml.etree.ElementTree as ET
from PIL import Image
import base64
from io import BytesIO
import json

class Library:
    def __init__(self, name : str):
        self.name = name
        self.data = []
        
    def addPILImage(self, img : Image.Image, name : str):
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue())
        self.data.append({
            "data": "data:image/png;base64," + img_str.decode('utf-8'),
            "w": img.width,
            "h": img.height,
            "title": name,
            "aspect": "fixed"
        })
        print(f'Image {name} added')
        
    def addImage(self, path : str):
        img = Image.open(path)       
        name = "".join(path.split('/')[-1].split('.')[:-1]) 
        self.addPILImage(img, name)
        
    
    def addImages(self, paths : list):
        for path in paths:
            self.addImage(path)

    def createLibrary(self, output_path):
        # create the file structure, and write data in it
        mxlibrary = ET.Element('mxlibrary')
        mxlibrary.text = json.dumps(self.data)
        # create a new XML file with the results
        mydata = ET.tostring(mxlibrary)
        myfile = open(output_path, "wb")
        myfile.write(mydata)
        myfile.close()
        print(f'Library created at {output_path}')