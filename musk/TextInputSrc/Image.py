from .Element import Element
from musk.settings import MEDIA_URL
import os

imgPath = MEDIA_URL

class Image(Element):
    def __init__(self,id):
        super().__init__()
        self.path = os.path.join(imgPath, 'cyberpunk.jpg')
        self.border = "5"
        self.borderColor = "black"
        self.text = "Your Image"
        self.id = "elem"+str(id)

    def setBorder(self,size):
        self.border = size
    def setBorderColor(self,color):
        self.borderColor = color
    def setPath(self,path):
        self.path = path
    def ElementToHTML(self):
        string = "<img id=\""+ self.id +"\" src=\"" + self.path + "\" alt=\"" + self.text + "\">"
        return string
    
    def ElementCSS(self):
        string = "img {\n\t width: 75%;\n"
        if self.elementColor != None:
            string = string + "\t background-color: " + str(self.elementColor) + ";\n"
        if self.border != None:
            string = string + "\t border: " + str(self.border) + "px solid " + str(self.borderColor) + ";\n"
        if self.padding != None:
            string = string + "\t padding: " + str(self.padding) + "px;\n"
        string = string + "}\n"
        return string