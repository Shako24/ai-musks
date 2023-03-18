import re
class Element:
    def __init__(self):
        self.x = None
        self.y = None
        self.orientation = None
        self.size = None
        self.elementColor = "white"
        self.padding = None
        self.tagList = []
        self.text = "Lorem Ipsum"
        self.name = "Lorem Ipsum"
        self.fontSize = None
        self.font = None
        self.fontColor = None
        self.align = "center"
        self.id = None
    
    def setAlign(self, align):
        self.align = str(align)
    def setElementColor(self,x):
        self.elementColor = x
    def setFontColor(self,x):
        self.fontColor = x
    def setFont(self,x):
        self.font = str(x)
    def setFontSize(self,x):
        self.fontSize = x
    def setpad(self,x):
        self.padding = str(x)
    def setname(self, name):
        self.name = str(name)
    def setText(self, text):
        self.text = str(text)

    def setX(self, xCoord):
        self.x = xCoord

    def setY(self, YCoord):
        self.x = YCoord
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setOrient(self,orient):
        self.orientation = orient
    
    def getOrient(self,orient):
        return self.orientation
    
    def setSize(self,size):
        self.size = size
    
    def setColor(self,color):
        pattern = "[a-fA-f0-9]{6}"
        if re.match(pattern,color):
            color = "#" + color
            self.elementColor = color
        else:
            return 1
    
    def getColor(self):
        return self.elementColor
    
    def ElementToString(self):
        """Needs to be implemented"""
        return 0
    
    def addTag(self,tag):
        self.tagList.append(tag)

    
    
    
