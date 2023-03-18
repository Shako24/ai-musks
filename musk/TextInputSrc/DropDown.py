from .Element import Element
class DropDown(Element):
    def __init__(self,id):
        super().__init__()
        self.options = ["Dropdown1", "Dropdown2", "Dropdown3"]
        self.border = None
        self.borderColor = "black"
        self.cursor = "pointer"
        self.id = "elem"+str(id)
        
    
    def setCursor(self,cursor):
        self.cursor = str(cursor)
    
    def setBorder(self,size):
        self.border = size
    def setBorderColor(self,color):
        self.borderColor = color
    
    def setOptions(self,array):
        self.options = array

    def ElementToHTML(self):
        string = "<select name= \"" + self.name + "\" id=\""+ self.id +"\">"
        for x in self.options:
            string = string + "<option value=\"" + str(x) + "\">" + str(x) + "</option>"
        string = string + "</select>"        
        return string
    
    def ElementCSS(self):
        css = '''
	height: 35px;
	background: #e0dede;
	justify-content: center;
	display: flex;
	border: none;
	outline: none;
	border-radius: 5px;
'''

        string = "select {\n"
        string += css
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
        string = string + "\t cursor: " + str(self.cursor) + ";\n"
        string = string + "}\n"
        return string