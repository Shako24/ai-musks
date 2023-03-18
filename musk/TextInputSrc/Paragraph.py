from .Element import Element
class Paragraph(Element):
    def __init__(self,id):
        super().__init__()
        self.border = None
        self.borderColor = "black"
        self.text = "Lorem ipsum dolor sit amet, ea vocent deserunt postulant nec.<br> Mea id iriure probatus, sit unum clita mandamus ex.<br> Duo zril facilisi expetendis eu, in sea omnes torquatos.<br> Ne deseruisse deterruisset pri, per nostro constituam ut.<br> Est ex natum impedit, ei duo graeci deserunt.<br> Affert recusabonepro."
        self.align = "center"
        self.id = "elem"+str(id)
    
    def setAlign(self,align):
        self.align = str(align)

    def setBorder(self,size):
        self.border = size
    def setBorderColor(self,color):
        self.borderColor = color
    def ElementToHTML(self):
        string = "<p id=\"" + self.id + "\" >" + self.text + "</p>"
        return string
    
    def ElementCSS(self):
        string = "p {\n\t text-align: " + self.align + ";\n"
        if self.elementColor != None:
            string = string + "\t background-color: " + str(self.elementColor) + ";\n"
        if self.border != None:
            string = string + "\t border: " + str(self.border) + "px solid " + str(self.borderColor) + ";\n"
        if self.padding != None:
            string = string + "\t padding: " + str(self.padding) + "px;\n"
        if self.fontSize != None:
            string = string + "\t font-size: " + str(self.fontSize) + "px;\n"   
        if self.font != None:
            string = string + "\t font-family: \"" + str(self.font) + "\";\n" 
        if self.fontColor != None:
            string = string + "\t color: " + str(self.fontColor) + ";\n"
        string = string + "border-radius: 5px;"
        string = string + "}\n"
        return string