from .Element import Element
class Button(Element):
    def __init__(self,id):
        super().__init__()
        self.border = "2"
        self.borderColor = "black"
        self.cursor = "pointer"
        self.text = "Button"
        self.name = "Button"
        self.fontSize = "1em"
        self.id = "elem"+str(id)
    def setCursor(self,cursor):
        self.cursor = str(cursor)
    def setBorder(self,size):
        self.border = size
    def setBorderColor(self,color):
        self.borderColor = color

    def ElementToHTML(self):
        string = "<button class=\"button\" id=\"" + self.id + "\">"+ self.text + "</button>"
        return string
    
    def ElementCSS(self, rando):
        css1 = '''
        border-radius: 4px;
        border-style: none;
        box-sizing: border-box;
        color: black;
        cursor: pointer;
        display: inline-block;
        font-size: 16px;
        font-weight: 700;
        line-height: 1.5;
        margin: 0;
        max-width: none;
        min-height: 44px;
        min-width: 10px;
        outline: none;
        overflow: hidden;
        padding: 9px 20px 8px;
        position: relative;
        text-align: center;
        text-transform: none;
        user-select: none;
        -webkit-user-select: none;
        touch-action: manipulation;
        width: 100%;
        '''
        css1_1 =  '''button:hover,
        button:focus {
            opacity: .75;
        }'''
        css2 = '''
        background-color: #fff;
  border: 0 solid #e2e8f0;
  border-radius: 1.5rem;
  box-sizing: border-box;
  color: #0d172a;
  cursor: pointer;
  display: inline-block;
  font-family: "Basier circle",-apple-system,system-ui,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
  font-size: 1.1rem;
  font-weight: 600;
  line-height: 1;
  padding: 1rem 1.6rem;
  text-align: center;
  text-decoration: none #0d172a solid;
  text-decoration-thickness: auto;
  transition: all .1s cubic-bezier(.4, 0, .2, 1);
  box-shadow: 0px 1px 2px rgba(166, 175, 195, 0.25);
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
'''
        css2_2 = '''button:hover {
  background-color: #1e293b;
  color: #fff;
}

@media (min-width: 768px) {
  button {
    font-size: 1.125rem;
    padding: 1rem 2rem;
  }
}'''
        css3 = '''
  align-items: center;
  background-color: #fff;
  border: 2px solid #000;
  box-sizing: border-box;
  color: #000;
  cursor: pointer;
  display: inline-flex;
  fill: #000;
  font-family: Inter,sans-serif;
  font-size: 16px;
  font-weight: 600;
  height: 48px;
  justify-content: center;
  letter-spacing: -.8px;
  line-height: 24px;
  min-width: 140px;
  outline: 0;
  padding: 0 17px;
  text-align: center;
  text-decoration: none;
  transition: all .3s;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
'''
        css3_3 = '''button:focus {
  color: #171e29;
}

button:hover {
  border-color: #06f;
  color: #06f;
  fill: #06f;
}

button:active {
  border-color: #06f;
  color: #06f;
  fill: #06f;
}

@media (min-width: 768px) {
  button {
    min-width: 170px;
  }
}'''

        string = "button {\n"
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
        # string = string + "border-radius: 5px;\n\tmargin-top: 20px;\n\tmargin: 10px auto;\n\toutline: none;"
        
        string = string + "}"
        # string += css3
        if rando == 0:
            string += css1_1
        elif rando == 1:
            string += css2_2
        else:
            string += css3_3
        return string