from os import link
from .Element import Element
class Link(Element):
    def __init__(self,id):
        super().__init__()
        self.text = "link"
        self.name = "link"
        self.id = "elem"+str(id)
    def ElementToHTML(self):
        string = "<a id=\"" + self.id + "\" href=\"" + self.name + "\">" + self.text + "</a>"
        return string
    
    def ElementCSS(self):
        string = "a {\n"
        if self.fontSize != None:
            string = string + "\t font-size: " + str(self.fontSize) + "px;\n"   
        if self.font != None:
            string = string + "\t font-family: \"" + str(self.font) + "\";\n" 
        if self.fontColor != None:
            string = string + "\t color: " + str(self.fontColor) + ";\n"
        string = string + "}\n"
        return string