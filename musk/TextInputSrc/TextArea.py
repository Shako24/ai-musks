from .Element import Element
class TextArea(Element):
    def __init__(self,id):
        super().__init__()
        self.rows = 4
        self.cols = 50
        self.border = "3"
        self.borderColor = "none"
        self.cursor = "text"
        self.text = "Place Your text Here"
        self.name = "text area"
        self.id = "elem"+str(id)
        
    def setCursor(self,cursor):
        self.cursor = str(cursor)
    
    def setBorder(self,size):
        self.border = size
    def setBorderColor(self,color):
        self.borderColor = color
    
    def setRows(self,rows):
        self.rows = int(rows)
    
    def setCols(self,cols):
        self.cols = int(cols)

    def ElementToHTML(self):
        string = "<textarea id=\"" + self.id + "\" name=\"" + self.name + "\" rows=\"" + str(self.rows) + "\" cols=\"" + str(self.cols) + "\" placeholder=\"" + self.text + "\">""</textarea>"
        return string
    
    def ElementCSS(self, rando):
        css1 = '''
    font-family: inherit;
    border: 0;
    border: 2px solid #9b9b9b;
    outline: 0;
    font-size: 1.3rem;
    color: black;
    padding: 7px 0;
    background: transparent;
    transition: border-color 0.2s;
'''
        css1_1 = '''
textarea::placeholder {
    color: transparent;
}
textarea:focus {
    border: none;
    border: 0.125rem solid #11998e;
}
'''
        css2 = '''
    margin: 1.5rem;
	position: relative;
	border: none;
	border: 0.125rem solid rgba(19, 19, 21, 0.6);
	font-size: 1.0625rem;
	padding-left: 0.875rem;
	line-height: 147.6%;
	padding-top: 0.825rem;
	padding-bottom: 0.5rem;
'''
        css2_2 = '''textarea:focus {
	outline: none;
}
textarea:hover {
	background: rgba(73, 133, 224, 0.12);
	border-color: #121212;
}'''
        css3 = '''  padding: 12px 20px;
    font-size: 1rem;
    border-width: calc(5 * 1px);
    border-style: solid;
    border: none;
    border-radius: calc(6 * 1px);
    text-align: center;
    outline: transparent;
'''
        string = "textarea {\n"
        if rando == 0:
            string += css1
        elif rando == 1:
            string += css2
        else:
            string += css3
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

        # string = string + "margin: 20px auto;\n\toutline: none;\n\tborder-radius: 5px;"

        string = string + "\t cursor: " + str(self.cursor) + ";\n"
        string = string + "}\n"
        if rando == 0:
            string += css1_1
        elif rando == 1:
            string += css2_2
        return string
    
