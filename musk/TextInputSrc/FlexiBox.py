from .Element import Element
class FlexiBox(Element):
    def __init__(self):
        super().__init__()
        self.backcolor = "white"
        self.align = "center"
        self.justifyContent = "center"
        self.divbackcolor = "white"
        self.margin = "10px"
        self.padding = "20px"

        
    def setBackColor(self, color):
        self.backcolor = str(color)
    
    def setAlign(self, align):
        self.align = str(align)
    
    def setJustifyContent(self, align):
        self.justifyContent = str(align)
    
    def setDivBackColor(self,color):
        self.divbackcolor = str(color)
    
    def setMargin(self,margin):
        self.margin = str(margin) + "px"
    
    def setPadding(self, pad):
        self.padding = str(pad) + "px"
    
    def ElementCSS(self):
        string2 = "background: url(https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38) no-repeat center/ cover;"
        string = ".flex-container {\n\t display: flex;\n\t background-color: "+self.backcolor+";\n\t width: auto;\n\t align-items: "+self.align+";\n\t justify-content: "+self.justifyContent+";\n}\n.flex-container > div {\n\t background-color: "+self.divbackcolor+";\n\t margin: "+self.margin+";\n\t padding: "+self.padding+";\n\t width: auto; \n\t" + string2+ "\n}\n"
        return string