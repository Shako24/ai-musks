from .Element import Element
class Header(Element):
    def __init__(self,id):
        super().__init__()
        self.text = "Header"
        self.name = "Header"
        self.align = "center"
        self.id = "elem"+str(id)

    def setAlign(self, align):
        self.align = str(align)

    def ElementToHTML(self):
        string = "<h1 id=\""+ self.id +"\">" + self.text + "</h1>"
        return string
    
    def ElementCSS(self):
        string = "h1 {\n\t text-align: " + self.align + ";\n"
        if self.fontSize != None:
            string = string + "\t font-size: " + str(self.fontSize) + "px;\n"   
        if self.font != None:
            string = string + "\t font-family: \"" + str(self.font) + "\";\n" 
        if self.fontColor != None:
            string = string + "\t color: " + str(self.fontColor) + ";\n"
        string = string + "}\n"
        return string