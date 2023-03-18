from .Element import Element
class RadioButton(Element):
    def __init__(self,id):
        super().__init__()
        self.text = "Radio button"
        self.id = "elem"+str(id)
        
    def ElementToHTML(self):
        string = "<label id=\"" + self.id + "\"><input type=\"radio\">" + self.text + "</label>"
        return string
    
    def ElementCSS(self):
        return 0