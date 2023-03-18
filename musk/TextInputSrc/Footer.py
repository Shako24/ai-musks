
from .Element import Element
class Footer(Element):
    def __init__(self,id):
        super().__init__()
        self.border = "5"
        self.borderColor = "black"
        self.cursor = "pointer"
        self.text = "Footer"
        self.name = "Footer"
        self.align = "center"
        self.id = "elem"+str(id)
    
    def setAlign(self, align):
        self.align = str(align)
        
    def setCursor(self,cursor):
        self.cursor = str(cursor)
    
    def setBorder(self,size):
        self.border = size
    def setBorderColor(self,color):
        self.borderColor = color
    
    def ElementToHTML(self):
        string = "<footer id=\""+ self.id +"\">" + self.text + "</footer>"
        return string
    
    def ElementCSS(self):
        string = "footer {\n\t width: 100%;\n"
        if self.elementColor != None:
            string = string + "\t background-color: " + str(self.elementColor) + ";\n"
        if self.border != None:
            string = string + "\t border: " + str(self.border) + "px solid " + str(self.borderColor) + ";\n"
        if self.padding != None:
            string = string + "\t padding: " + str(self.padding) + "px;\n"
        string = string + "\t cursor: " + str(self.cursor) + ";\n"
        string = string + "\t display: flex;\n\t justify-content: center;\n\t font-weight: bolder;\n\t font-size: 2em;\n"
        string = string + "}\n"
        return string
        