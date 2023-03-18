from .Label import Label
from .CheckBox import CheckBox
from .Image import Image
from .Button import Button
from .TextBox import TextBox
from .NavBar import NavBar
from .Footer import Footer
from .Header import Header
from .FlexiBox import FlexiBox
from .RadioButton import RadioButton
import random
class ImageToHTML():
    def __init__(self,page,page2,width):
        self.page = page
        self.pageOut = page2
        self.width = int(width)
    
    def createHTML(self):
        list = []
        f = open(self.page, "r")
        lines = f.readlines()
        count = 1
        flag = 0
        for line in lines:
            if line == "BREAK\n":
                list.append("<br>")
                flag = 0
            else:
                words = line.split(",")
                num1 = int(words[1])
                num2 = (num1/self.width)*100
                words[1] = num2
                ##num = int(words[1])
                ##num = num/150
                ##num = round(num,0)
                ##num = 150*num
                ##words[1] = str(num)
                if words[0] == "Label":
                    if flag == 0:
                        list1 = []
                        list1.append(Label(count))
                        list1.append(words[1])
                        list.append(list1)
                        count = count + 1  
                    else:
                        flag = 1                 
                if words[0] == "TextBox":
                    list1 = []
                    list1.append(TextBox(count))
                    list1.append(words[1])
                    list.append(list1)
                    count = count + 1
                if words[0] == "CheckBox":
                    list1 = []
                    list1.append(CheckBox(count))
                    list1.append(words[1])
                    list.append(list1)
                    flag = 1
                    count = count + 1
                if words[0] == "Image":
                    list1 = []
                    list1.append(Image(count))
                    list1.append(words[1])
                    list.append(list1)
                    count = count + 1
                if words[0] == "Button":
                    list1 = []
                    list1.append(Button(count))
                    list1.append(words[1])
                    list.append(list1)
                    count = count + 1
                if words[0] == "RadioButton":
                    list1 = []
                    list1.append(RadioButton(count))
                    list1.append(words[1])
                    list.append(list1)
                    flag = 1
                    count = count + 1
           ## if words[0] == "RadioButton"
             ##   list.append(RadioButton(count))
            
        f2 = open(self.pageOut, "w")
        f2.write("<!DOCTYPE html>\n")
        f2.write("<html>\n")
        f2.write("<style>\n")
        headerTest = Header(count)
        headerTest.text = "ADD YOUR HEADER HERE!!!"
        headerTest.fontColor = "white"
        count = count + 1
        navTest = NavBar(count)
        count = count + 1
        footerTest = Footer(count)
        string = headerTest.ElementCSS()
        f2.write(string)
        string = navTest.ElementCSS()
        f2.write(string)
        string = footerTest.ElementCSS()
        f2.write(string)
        flexiTest = FlexiBox()
        flexiTest.setJustifyContent("left")
        string = flexiTest.ElementCSS()
        f2.write(string)
        breakTest = "<br>"
        buttonTest = Button(0)
        string = buttonTest.ElementCSS()
        f2.write(string)
        labelTest = Label(0)
        string = labelTest.ElementCSS()
        f2.write(string)
        textTest = TextBox(0)
        string = textTest.ElementCSS()
        f2.write(string)
        imageTest = Image(0)
        string = imageTest.ElementCSS()
        f2.write(string)
        flag = 0
        listcol = ["background: linear-gradient(112.1deg, rgb(32, 38, 57) 11.4%, rgb(63, 76, 119) 70.2%);","background: linear-gradient(15deg, #13547a 0%, #80d0c7 100%);","background: linear-gradient(109.5deg, rgb(13, 11, 136) 9.4%, rgb(86, 255, 248) 78.4%);","background: linear-gradient(120deg, #e0c3fc 0%, #8ec5fc 100%);","background: linear-gradient(to top, #c471f5 0%, #fa71cd 100%);","background: radial-gradient(circle at 3% 4.8%, rgb(169, 224, 127) 0%, rgb(248, 247, 121) 86.6%);","background: radial-gradient(circle at 52.1% -29.6%, rgb(144, 17, 105) 0%, rgb(51, 0, 131) 100.2%);"]
        nuber = random.randint(0,6)
        f2.write("</style>\n")
        f2.write("<body style=\""+ listcol[nuber] +"\">\n")
        string = navTest.ElementToHTML()
        f2.write(string+"<br>\n")
        string = headerTest.ElementToHTML()
        f2.write(string+"<br>\n")
        f2.write("<div style=\"overflow: scroll;\">\n")
        for x in list:
            print(x)
            if(flag == 0):
                flag = 1
                f2.write("<div class=\"flex-container\" style=\"background: url(https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38) no-repeat center/ cover;\">")
                if(type(x) == type(breakTest)):
                    f2.write("</div><br>\n")
                    print("Here")
                    flag = 0
                else:
                    f2.write("<div style = \"transform:translateX(" + str(x[1]) + "vw);\">")
                    f2.write(x[0].ElementToHTML())
                    f2.write("</div><br>")
            else:
                if(type(x) == type(breakTest)):
                    f2.write("</div><br>\n")
                    print("Here")
                    flag = 0
                else:
                    f2.write("<div style = \"transform:translateX(" + str(x[1]) + "vw);\">")
                    f2.write(x[0].ElementToHTML())
                    f2.write("</div><br>")

        if flag == 1:
            f2.write("</div><br>\n")
        f2.write("</div>\n")
        f2.write(footerTest.ElementToHTML())    
        f2.write("</body>\n")
        f2.write("</html>\n")
                

