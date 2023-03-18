from .Element import Element
class CheckBox(Element):
    def __init__(self,id):
        super().__init__()
        self.text = "CheckBox"
        self.id = "elem"+str(id)
        
    def ElementToHTML(self):
        string = "<label id=\"" + self.id + "\"><input type=\"checkbox\">" + self.text + "</label>"
        return string
    
    def ElementCSS(self):
        return 0