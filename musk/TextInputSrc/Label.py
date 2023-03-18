from .Element import Element
class Label(Element):
    def __init__(self,id):
        super().__init__()
        self.text = "Label"
        self.align = "center"
        self.backcolor = "white"
        self.justifyContent = "center"
        self.id = "elem"+str(id)
        
    def setBackColor(self, color):
        self.backcolor = str(color)
    
    def setAlign(self, align):
        self.align = str(align)
    
    def setJustifyContent(self, align):
        self.justifyContent = str(align)
    
    def ElementToHTML(self):
        string = "<label id=\"" + self.id + "\" for=\"" + self.name + "\">" + self.text + "</label>"
        return string
    
    def ElementCSS(self):
        string = "label {\n\t text-align: " + self.align + ";\n"
        if self.fontSize != None:
            string = string + "\t font-size: " + str(self.fontSize) + "px;\n"   
        if self.font != None:
            string = string + "\t font-family: \"" + str(self.font) + "\";\n" 
        if self.fontColor != None:
            string = string + "\t color: " + str(self.fontColor) + ";\n"
        string = string + "}\n"
        string = string + ".flex-container2 {\n\t display: flex;\n\t background-color: "+self.backcolor+";\n\t width: auto;\n\t align-items: "+self.align+";\n\t justify-content: "+self.justifyContent+";\n}\n"
        return string