from .Element import Element
class NavBar(Element):
    def __init__(self,id):
        super().__init__()
        self.options = ["Lorem Ipsum1", "Lorem Ipsum2"]
        self.refs = ["#Lorem Ipsum1", "#Lorem Ipsum2"]
        self.elementColor = "black"
        self.padding = 14
        self.linkcolor = "white"
        self.hoverColor = "grey"
        self.activeColor = "blue" 
        self.fontSize = 17
        self.hoverfontColor = "red"
        self.activefontColor = "green"
        self.id = "elem"+str(id)
        

    def ElementToHTML(self):
        string = "<div id=\"" + self.id + "\" class=\"topnav\">\n"
        x = 0
        while(x < len(self.options)):
            if x == 0:
                string = string + "<a class=\"active\" href=\"" + self.refs[x] + "\">" + self.options[x] + "</a>\n"
            else:
                string = string + "<a href=\"" + self.refs[x] + "\">" + self.options[x] + "</a>\n"
            x = x + 1
        string = string + "</div>"
        return string
    
    def ElementCSS(self):
        string = ".topnav { \n\t width: 100%;\n\t background-color: " + str(self.elementColor) + ";\n\t overflow: hidden;\n}\n.topnav a {\n\t float: left;\n\t color: " + str(self.linkcolor) + ";\n\t text-align: center;\n\t padding: " + str(self.padding) + "px ;\n\t text-decoration: none;\n\t font-size: " + str(self.fontSize) + "px;\n}\n.topnav a:hover {\n\t background-color: " + self.hoverColor + ";\n\t color: " + self.hoverfontColor + ";\n}\n.topnav a.active {\n\t background-color: " + self.activeColor + ";\n\t color: " + self.activefontColor + ";\n}\n"
        return string
        
    def sethoverfontColor(self,color):
        self.hoverfontColor = str(color)
    def setactivefontColor(self,color):
        self.activefontColor = str(color)
    def setlinkColor(self,color):
        self.linkcolor = str(color)
    def sethoverColor(self,color):
        self.hoverColor = str(color)
    def setactiveColor(self,color):
        self.activeColor = str(color)
    def setOptions(self,array):
        self.options = array

    def setRefs(self,array):
        self.Refs = array

    