import datetime
import re
from .Image import Image
from .Link import Link
from .Element import Element
from .CheckBox import CheckBox
from .NavBar import NavBar
from .Footer import Footer
from .Header import Header
from .Button import Button
from .CheckBox import CheckBox
from .DropDown import DropDown
from .Paragraph import Paragraph
from .TextArea import TextArea
from .TextBox import TextBox
from .Label import Label
from .FlexiBox import FlexiBox
from .Form import Form
import random

class Webpage:
    def __init__(self):
        background_list = ["linear-gradient(112.1deg, rgb(32, 38, 57) 11.4%, rgb(63, 76, 119) 70.2%);","linear-gradient(15deg, #13547a 0%, #80d0c7 100%);","linear-gradient(109.5deg, rgb(13, 11, 136) 9.4%, rgb(86, 255, 248) 78.4%);","linear-gradient(120deg, #e0c3fc 0%, #8ec5fc 100%);","linear-gradient(to top, #c471f5 0%, #fa71cd 100%);","radial-gradient(circle at 3% 4.8%, rgb(169, 224, 127) 0%, rgb(248, 247, 121) 86.6%);","radial-gradient(circle at 52.1% -29.6%, rgb(144, 17, 105) 0%, rgb(51, 0, 131) 100.2%);"]
        self.webpageName = None
        self.webpageDate = datetime.datetime.now()
        self.webElementsList = []
        self.webpageImage = None
        self.backgroundColor = background_list[random.randint(0,6)]
    
    def setWebpageName(self,name):
        self.webpageName = name
    
    def getWebpageName(self):
        return self.webpageName
    
    def setWebpageDate(self):
        self.webpageDate = datetime.datetime.now()
    
    def getWebpageDate(self):
        return self.webpageDate
    
    def addWebpageElement(self,element):
        self.webElementsList.append(element)
    
    def removeWebpageElement(self,element):
        self.webElementsList.remove(element)
    
    def setBackgroundColor(self,colorhex):
        self.backgroundColor = str(colorhex)
    
    def webpageToString(self):
        """Needs to be implemented"""
        return 0
        
    def stringToElement(self):
        """Needs to be implemented"""
        return 0
    
    def setImage(self, Image):
        self.webpageImage = Image
    
    def getImage(self, Image):
        return self.webpageImage
    """
    def uploadImage(self, image):
        
        im = Image.open(image)
        data = asarray(image)
        self.setImage(data)
    """
    """
    def CheckboxArranger(self):
        res = []
        test = CheckBox()
        count = 0
        for x in self.webElementsList: 
            if type(x) == type(test) :
                count = count + 1
        if count == 0:
            return NULL
        else:
            for x in self.webElementsList: 
                if type(x) == type(test) :
                    res.append(x)
            return res
    """
    """Make sure only 1 navbar and 1 footer"""
    """initialize list as [] incase the text input paragraph is empty"""

    def formmaker(self,buttonList,checkboxList,dropdownList,textareaList,textboxList):
        total = len(buttonList) + len(checkboxList) + len(dropdownList) + len(textareaList) + len(textboxList)
        if total > 0:
            id = "elem"
            counter = 0
            string = "<div>"
            head = Header(id+str(counter))
            counter = counter + 1
            head.text = "This is Your Form!!"
            string = string + head.ElementToHTML()
            
            if len(dropdownList) != 0:
                for x in dropdownList:
                    string = string + "<div>"
                    label = Label(id + str(counter))
                    counter = counter + 1
                    label.text = "This is the label for your dropdown:"
                    string = string + "<div class=\"flex-container1\" style=\"background: url(https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38) no-repeat center/ cover;\">"
                    string = string + "<div>" + label.ElementToHTML() + "</div>" + "<div>" + x.ElementToHTML() + "</div>" + "</div>"
                    string = string + "</div>"
            
            if len(textboxList) != 0:
                for x in textboxList:
                    string = string + "<div>"
                    label = Label(id + str(counter))
                    counter = counter + 1
                    label.text = "This is the label for your textbox:"
                    string = string + "<div class=\"flex-container1\" style=\"background: url(https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38) no-repeat center/ cover;\">"
                    string = string + "<div>" + label.ElementToHTML() + "</div>" + "<div>" + x.ElementToHTML() + "</div>" + "</div>"
                    string = string + "</div>"
            
            if len(textareaList) != 0:
                for x in textareaList:
                    string = string + "<div>"
                    label = Label(id + str(counter))
                    counter = counter + 1
                    label.text = "This is the label for your textarea:"
                    string = string + "<div class=\"flex-container1\" style=\"background: url(https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38) no-repeat center/ cover;\">"
                    string = string + "<div>" + label.ElementToHTML() + "</div>" + "<div>" + x.ElementToHTML() + "</div>" + "</div>"
                    string = string + "</div>"

            if len(checkboxList) != 0:
                string = string + "<div>"
                label = Label(id+str(counter))
                counter = counter + 1
                label.text = "This is the label for your checkboxes:"
                string = string + label.ElementToHTML() + "<br>\n"
                string = string + "<div class=\"flex-container1\" style=\"background: url(https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38) no-repeat center/ cover;\">"
                for x in checkboxList:
                    string = string + "<div>" + x.ElementToHTML() + "</div>"
                string = string + "</div>" + "</div>\n"
            
            if len(buttonList) != 0:
                string = string + "<div>" + "<div class=\"flex-container1\" style=\"background: url(https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38) no-repeat center/ cover;\">"
                for x in buttonList:
                    string = string + "<div>" + x.ElementToHTML() + "</div>"  
                string = string + "<div>" + "</div>\n"

            
            string = string + "</div>\n"
            return string
        else:
            return ""
        
    def WebpageToHTML(self,filename,listCSS):
        f = open(filename, "w")
        f.write("<!DOCTYPE html>\n")
        f.write("<html>\n")
        f.write("<style>\n")
        id = 0
        headerTest = Header(id)
        footerTest = Footer(id)
        NavTest = NavBar(id)
        droptest = DropDown(id)
        buttonTest = Button(id)
        check = CheckBox(id)
        labelTest = Label(id)
        textTest = TextBox(id)
        textAreaTest = TextArea(id)
        imgTest = Image(id)
        linkTest  = Link(id)
        paraTest = Paragraph(id)
        flexiTest = FlexiBox()
        formTest = Form()
        if len(listCSS) != 0:
            for x in listCSS:
                if x[0] == 'Header':
                    if x[1] == 'alignment':
                        headerTest.setAlign(x[3])
                    if x[1] == 'font':
                        if x[3] == 'font-family':
                            headerTest.setFont(x[2])
                        if x[3] == 'color':
                            headerTest.setFontColor(x[2])
                if x[0] == 'Button':
                    if x[1] == 'background':
                        if x[3] == 'color':
                            buttonTest.setElementColor(x[2])
                    if x[1] == 'font':
                        if x[3] == 'font-family':
                            buttonTest.setFont(x[2])
                        if x[3] == 'color':
                            buttonTest.setFontColor(x[2])
                    if x[1] == 'border':
                        if x[3] == 'color':
                            buttonTest.setBorderColor(x[2])
                if x[0] == 'Dropdown':
                    if x[1] == 'background':
                        if x[3] == 'color':
                            droptest.setElementColor(x[2])
                    if x[1] == 'font':
                        if x[3] == 'font-family':
                            droptest.setFont(x[2])
                        if x[3] == 'color':
                            droptest.setFontColor(x[2])
                    if x[1] == 'border':
                        if x[3] == 'color':
                            droptest.setBorderColor(x[2])
                if x[0] == 'Footer':
                    if x[1] == 'background':
                        if x[3] == 'color':
                            footerTest.setElementColor(x[2])
                    if x[1] == 'font':
                        if x[3] == 'font-family':
                            footerTest.setFont(x[2])
                        if x[3] == 'color':
                            footerTest.setFontColor(x[2])
                    if x[1] == 'border':
                        if x[3] == 'color':
                            footerTest.setBorderColor(x[2])
                    if x[1] == 'alignment':
                        footerTest.setAlign(x[3])
                if x[0] == 'Label':
                    if x[1] == 'background':
                        if x[3] == 'color':
                            labelTest.setElementColor(x[2])
                    if x[1] == 'font':
                        if x[3] == 'font-family':
                            labelTest.setFont(x[2])
                        if x[3] == 'color':
                            labelTest.setFontColor(x[2])
                    if x[1] == 'alignment':
                        labelTest.setAlign(x[3])
                if x[0] == 'Link':
                    if x[1] == 'font':
                        if x[3] == 'font-family':
                            linkTest.setFont(x[2])
                        if x[3] == 'color':
                            linkTest.setFontColor(x[2])
                if x[0] == 'Navbar':
                    if x[1] == 'background':
                        if x[3] == 'color':
                            NavTest.setElementColor(x[2])
                    if x[1] == 'font':
                        if x[3] == 'font-family':
                            NavTest.setFont(x[2])
                        if x[3] == 'color':
                            NavTest.setFontColor(x[2])
                if x[0] == 'Paragraph':
                    if x[1] == 'background':
                        if x[3] == 'color':
                            paraTest.setElementColor(x[2])
                    if x[1] == 'font':
                        if x[3] == 'font-family':
                            paraTest.setFont(x[2])
                        if x[3] == 'color':
                            paraTest.setFontColor(x[2])
                    if x[1] == 'border':
                        if x[3] == 'color':
                            paraTest.setBorderColor(x[2])
                    if x[1] == 'alignment':
                        paraTest.setAlign(x[3])
                if x[0] == 'TextBox':
                    if x[1] == 'background':
                        if x[3] == 'color':
                            textTest.setElementColor(x[2])
                    if x[1] == 'font':
                        if x[3] == 'font-family':
                            textTest.setFont(x[2])
                        if x[3] == 'color':
                            textTest.setFontColor(x[2])
                    if x[1] == 'border':
                        if x[3] == 'color':
                            textTest.setBorderColor(x[2])
                if x[0] == 'TextArea':
                    if x[1] == 'background':
                        if x[3] == 'color':
                            textAreaTest.setElementColor(x[2])
                    if x[1] == 'font':
                        if x[3] == 'font-family':
                            textAreaTest.setFont(x[2])
                        if x[3] == 'color':
                            textAreaTest.setFontColor(x[2])
                    if x[1] == 'border':
                        if x[3] == 'color':
                            textAreaTest.setBorderColor(x[2])
                if x[0] == 'Image':
                    if x[1] == 'border':
                        if x[3] == 'color':
                            imgTest.setBorderColor(x[2])
                if x[0] == 'Webpage':
                    self.backgroundColor = x[2]
        lister = [headerTest,footerTest,NavTest,droptest,buttonTest,check,labelTest,textTest,textAreaTest,imgTest,linkTest,paraTest]
        Nav = None
        foot = None
        rando = random.randint(0,2)
        for x in lister:
            if ((x == buttonTest) or (x == textTest) or (x == textAreaTest)):
                k = x.ElementCSS(rando)
            else:
                k = x.ElementCSS()   
            if k != 0 and k != None:  
                f.write(k)
        
        string3 = flexiTest.ElementCSS()
        f.write(string3)
        string3 = formTest.ElementCSS()
        f.write(string3)
        f.write("body {\n\t background: " + self.backgroundColor + ";\n}")
        f.write("</style>\n")
        f.write("<body>\n")
        """make form before this"""
        headerList = []
        imageList = []
        paraList = []
        linkList = []
        labelList = []
        textboxList= []
        textareaList = [] 
        checkboxList = []
        buttonList = []
        dropdownList = [] 
        formFlag = 0
        for x in self.webElementsList:
            if type(x) == type(headerTest):
                headerList.append(x)
            if type(x) == type(imgTest):
                imageList.append(x)
            if type(x) == type(paraTest):
                paraList.append(x)
            if type(x) == type(linkTest):
                linkList.append(x)
            if type(x) == type(labelTest):
                labelList.append(x)
            if type(x) == type(textTest):
                textboxList.append(x)
            if type(x) == type(textAreaTest):
                textareaList.append(x)
            if type(x) == type(check):
                checkboxList.append(x)
            if type(x) == type(buttonTest):
                buttonList.append(x)
            if type(x) == type(droptest):
                dropdownList.append(x)
            if type(x) == type(NavTest):
                Nav = x
            if type(x) == type(footerTest):
                foot = x
        if Nav != None:
            f.write(Nav.ElementToHTML())
            f.write("<br>\n")
        makesections = len(headerList)
        numimages = len(imageList)
        numlinks = len(linkList)
        numlabels = len(labelList)
        numparas = len(paraList)
        total = numimages + numparas
        while(makesections > total):
            headerList.pop(makesections-1)
            makesections = len(headerList)
        secdiv = None
        secdiv2 = None
        if(numimages >= numparas):
            secdiv = imageList
            secdiv2 = paraList
        else:
            secdiv = paraList
            secdiv2 = imageList
        
        numsecdiv = int(len(secdiv)/makesections)  ##larger value here
        numsecdiv2 = int(len(secdiv2)/makesections)
        string = ""
        while(makesections != 0):
            string = string + "<div>\n"
            head = headerList[0]
            head.text = "The Header for this section"
            string = string + head.ElementToHTML()
            headerList.pop(0)
            makesections = len(headerList)
            if(numsecdiv != 0):
                if (numsecdiv2 != 0):
                    counter1 = 0
                    counter2 = 0
                    while(counter2 < numsecdiv2):  ##smaller value first
                        string = string + "<div class=\"flex-container\" style=\"background: url(https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38) no-repeat center/ cover;\">"
                        string = string + "<div>"
                        string = string + secdiv2[counter2].ElementToHTML() + "</div>" + "<div>" + secdiv[counter2].ElementToHTML() + "</div>" + "</div>\n"
                        counter2 = counter2 + 1
                    while(counter1 < counter2):
                        secdiv2.pop(0)
                        counter1 = counter1 + 1  
                    flag = 0  
                    if (counter1 < numsecdiv):
                            string = string + "<div class=\"flex-container\" style=\"background: url(https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38) no-repeat center/ cover;\">"
                            flag = 1
                    while(counter1 < numsecdiv):
                        string = string + "<div>" + secdiv[counter1].ElementToHTML() + "</div>"
                        counter1 = counter1 + 1
                    if (flag == 1):
                        string = string + "</div>\n"
                    count = 0
                    while (count < counter1):
                        secdiv.pop(0)
                        count = count + 1
                
                else:
                    if(len(secdiv2) != 0):
                        counter1 = 0
                        string = string + "<div class=\"flex-container\" style=\"background: url(https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38) no-repeat center/ cover;\">" 
                        string = string + "<div>" + secdiv[counter1].ElementToHTML() + "</div>" + "<div>" + secdiv2[counter1].ElementToHTML() + "</div>" + "</div>\n"
                        counter1 = counter1 + 1
                        counter2 = 0
                        while(counter2 < counter1):
                            secdiv2.pop(0)
                            counter2 = counter2 + 1
                        flag = 0
                        if (counter1 < numsecdiv):
                            string = string + "<div class=\"flex-container\" style=\"background: url(https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38) no-repeat center/ cover;\">"
                            flag = 1
                        while(counter1 < numsecdiv):
                            string = string + "<div>" + secdiv[counter1].ElementToHTML() + "</div>"
                            counter1 = counter1 + 1
                        if (flag == 1):
                            string = string + "</div>\n"
                        count = 0
                        while (count < counter1):
                            secdiv.pop(0)
                            count = count + 1
                    
                    else:
                        string = string + "<div class=\"flex-container\" style=\"background: url(https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38) no-repeat center/ cover;\">"
                        counter1 = 0
                        while(counter1 < numsecdiv):
                            string = string + "<div>" + secdiv[counter1].ElementToHTML() + "</div>"
                            counter1 = counter1 + 1
                        string = string + "</div>\n"
                        count = 0
                        while (count < counter1):
                            secdiv.pop(0)
                            count = count + 1
            else:
                if len(secdiv) != 0:
                    if len(secdiv2) != 0:
                        string = string + "<div class=\"flex-container\" style=\"background: url(https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38) no-repeat center/ cover;\">"
                        string = string + "<div>" + secdiv2[0].ElementToHTML() + "</div>" + "</div>\n"
                        secdiv2.pop(0)
                    else:
                        string = string + "<div class=\"flex-container\" style=\"background: url(https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38) no-repeat center/ cover;\">"
                        string = string + "<div>" + secdiv[0].ElementToHTML() + "</div>" + "</div>\n"
                        secdiv.pop(0)
            string = string + "</div>"
            makesections = len(headerList)
            fg = 0
            if formFlag == 0:
                fg = random.randint(0,1)
            else:
                fg = 0
            if fg == 1:
                formFlag = 1
                string = string + self.formmaker(buttonList,checkboxList,dropdownList,textareaList,textboxList)
        if (len(secdiv) != 0):
            while(len(secdiv) != 0):
                if(len(secdiv2) != 0):
                    string = string + "<div class=\"flex-container\" style=\"background: url(https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38) no-repeat center/ cover;\">"
                    string = string + "<div>" + secdiv[0].ElementToHTML() + "</div>" + "<div>" + secdiv2[0].ElementToHTML() + "</div>" + "</div>\n"
                    secdiv.pop(0)
                    secdiv2.pop(0)
                else:
                    string = string + "<div class=\"flex-container\" style=\"background: url(https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38) no-repeat center/ cover;\">"
                    while(len(secdiv) != 0):
                        string = string + "<div>" + secdiv[0].ElementToHTML() + "</div>"
                        secdiv.pop(0)
                    string = string + "</div>\n"
        if formFlag == 0:
            string = string + self.formmaker(buttonList,checkboxList,dropdownList,textareaList,textboxList)
            formFlag = 1
        f.write(string)
        if foot != None:
            f.write(foot.ElementToHTML())   
        f.write("</body>\n")
        f.write("</html>\n")


####set min 1 header
# remove label and link
#         

"""   
    def WebpageToHTML(self,filename,listCSS):
        f = open(filename, "w")
        f.write("<!DOCTYPE html>\n")
        f.write("<html>\n")
        f.write("<style>\n")
        id = 0
        headerTest = Header(id)
        footerTest = Footer(id)
        NavTest = NavBar(id)
        droptest = DropDown(id)
        buttonTest = Button(id)
        check = CheckBox(id)
        labelTest = Label(id)
        textTest = TextBox(id)
        textAreaTest = TextArea(id)
        imgTest = Image(id)
        linkTest  = Link(id)
        paraTest = Paragraph(id)
        flexiTest = FlexiBox()
        formTest = Form()
        if len(listCSS) != 0:
            for x in listCSS:
                if x[0] == 'Header':
                    if x[1] == 'alignment':
                        headerTest.setAlign(x[3])
                    if x[1] == 'font':
                        if x[3] == 'font-family':
                            headerTest.setFont(x[2])
                        if x[3] == 'color':
                            headerTest.setFontColor(x[2])
                if x[0] == 'Button':
                    if x[1] == 'background':
                        if x[3] == 'color':
                            buttonTest.setElementColor(x[2])
                    if x[1] == 'font':
                        if x[3] == 'font-family':
                            buttonTest.setFont(x[2])
                        if x[3] == 'color':
                            buttonTest.setFontColor(x[2])
                    if x[1] == 'border':
                        if x[3] == 'color':
                            buttonTest.setBorderColor(x[2])
                if x[0] == 'Dropdown':
                    if x[1] == 'background':
                        if x[3] == 'color':
                            droptest.setElementColor(x[2])
                    if x[1] == 'font':
                        if x[3] == 'font-family':
                            droptest.setFont(x[2])
                        if x[3] == 'color':
                            droptest.setFontColor(x[2])
                    if x[1] == 'border':
                        if x[3] == 'color':
                            droptest.setBorderColor(x[2])
                if x[0] == 'Footer':
                    if x[1] == 'background':
                        if x[3] == 'color':
                            footerTest.setElementColor(x[2])
                    if x[1] == 'font':
                        if x[3] == 'font-family':
                            footerTest.setFont(x[2])
                        if x[3] == 'color':
                            footerTest.setFontColor(x[2])
                    if x[1] == 'border':
                        if x[3] == 'color':
                            footerTest.setBorderColor(x[2])
                    if x[1] == 'alignment':
                        footerTest.setAlign(x[3])
                if x[0] == 'Label':
                    if x[1] == 'background':
                        if x[3] == 'color':
                            labelTest.setElementColor(x[2])
                    if x[1] == 'font':
                        if x[3] == 'font-family':
                            labelTest.setFont(x[2])
                        if x[3] == 'color':
                            labelTest.setFontColor(x[2])
                    if x[1] == 'alignment':
                        labelTest.setAlign(x[3])
                if x[0] == 'Link':
                    if x[1] == 'font':
                        if x[3] == 'font-family':
                            linkTest.setFont(x[2])
                        if x[3] == 'color':
                            linkTest.setFontColor(x[2])
                if x[0] == 'Navbar':
                    if x[1] == 'background':
                        if x[3] == 'color':
                            NavTest.setElementColor(x[2])
                    if x[1] == 'font':
                        if x[3] == 'font-family':
                            NavTest.setFont(x[2])
                        if x[3] == 'color':
                            NavTest.setFontColor(x[2])
                if x[0] == 'Paragraph':
                    if x[1] == 'background':
                        if x[3] == 'color':
                            paraTest.setElementColor(x[2])
                    if x[1] == 'font':
                        if x[3] == 'font-family':
                            paraTest.setFont(x[2])
                        if x[3] == 'color':
                            paraTest.setFontColor(x[2])
                    if x[1] == 'border':
                        if x[3] == 'color':
                            paraTest.setBorderColor(x[2])
                    if x[1] == 'alignment':
                        paraTest.setAlign(x[3])
                if x[0] == 'TextBox':
                    if x[1] == 'background':
                        if x[3] == 'color':
                            textTest.setElementColor(x[2])
                    if x[1] == 'font':
                        if x[3] == 'font-family':
                            textTest.setFont(x[2])
                        if x[3] == 'color':
                            textTest.setFontColor(x[2])
                    if x[1] == 'border':
                        if x[3] == 'color':
                            textTest.setBorderColor(x[2])
                if x[0] == 'TextArea':
                    if x[1] == 'background':
                        if x[3] == 'color':
                            textAreaTest.setElementColor(x[2])
                    if x[1] == 'font':
                        if x[3] == 'font-family':
                            textAreaTest.setFont(x[2])
                        if x[3] == 'color':
                            textAreaTest.setFontColor(x[2])
                    if x[1] == 'border':
                        if x[3] == 'color':
                            textAreaTest.setBorderColor(x[2])
                if x[0] == 'Image':
                    if x[1] == 'border':
                        if x[3] == 'color':
                            imgTest.setBorderColor(x[2])
                if x[0] == 'Webpage':
                    self.backgroundColor = x[2]
        lister = [headerTest,footerTest,NavTest,droptest,buttonTest,check,labelTest,textTest,textAreaTest,imgTest,linkTest,paraTest]
        headTop = None
        Nav = None
        foot = None
        arrangeList = []
        rando = random.randint(0,2)
        for x in lister:
            print(x)
            if ((x == buttonTest) or (x == textTest) or (x == textAreaTest)):
                k = x.ElementCSS(rando)
            else:
                k = x.ElementCSS()                
            if k != 0 and k != None:
                f.write(k)
        
        string3 = flexiTest.ElementCSS()
        f.write(string3)
        string3 = formTest.ElementCSS()
        f.write(string3)
        for x in self.webElementsList:
                        
            if type(x) == type(headerTest):
                if headTop == None:
                    headTop = x
                else:
                    arrangeList.append(x)
            
            elif type(x) == type(footerTest):
                foot = x
            
            elif type(x) == type(NavTest):
                Nav = x
            
            else: 
                arrangeList.append(x)
        f.write("body {\n\t background: " + self.backgroundColor + ";\n}")
        f.write("</style>\n")
        f.write("<body>\n")
        if Nav != None:
            f.write(Nav.ElementToHTML())
            f.write("<br>\n")
       
        if headTop != None:
            f.write(headTop.ElementToHTML())
            f.write("<br>\n")
        newList = arrangeList
        dropdownList = []
        buttonList = []
        checkList = []
        labelList = []
        textBoxList = []
        textAreaList = []
        i = 0
        while i < len(newList):
            if type(newList[i]) == type(droptest):
                dropdownList.append(newList[i])
                newList.remove(newList[i])
                i = -1
            if type(newList[i]) == type(buttonTest):
                buttonList.append(newList[i])
                newList.remove(newList[i])
                i = -1
            if type(newList[i]) == type(check):
                checkList.append(newList[i])
                newList.remove(newList[i])
                i = -1
            if type(newList[i]) == type(labelTest):
                labelList.append(newList[i])
                newList.remove(newList[i])
                i = -1
            if type(newList[i]) == type(textTest):
                textBoxList.append(newList[i])
                newList.remove(newList[i])
                i = -1
            if type(newList[i]) == type(textAreaTest):
                textAreaList.append(newList[i])
                newList.remove(newList[i])
                i = -1
            i = i + 1
        if(len(labelList) >= (len(textBoxList)+len(textAreaList))):
            newlabelList = []
            while (len(labelList) != (len(textBoxList)+len(textAreaList))):
                x = labelList[len(labelList)-1]
                newlabelList.append(x)
                labelList.remove(x)
            if len(newlabelList) != 0:
                for x in newlabelList:
                    newList.append(x)

        else:
            for x in labelList:
                newList.append(x)
                labelList.remove(x)
            counting = 0
            adder = "elem"
            while(len(labelList) != (len(textBoxList)+len(textAreaList))):
                x = Label(adder+str(counting))
                labelList.append(x)
                counting = counting + 1
        
        strings = []
        if len(labelList) != 0:
            k = 0
            if len(textAreaList) != 0 and len(textBoxList) != 0:
                
                while(k != (len(textAreaList) + len(textBoxList))):
                    if k < len(textAreaList):
                        string = labelList[k].ElementToHTML() + "<br>\n" + textAreaList[k].ElementToHTML() + "<br>\n"
                    else:
                        string = labelList[k].ElementToHTML() + "<br>\n" + textBoxList[k-len(textAreaList)].ElementToHTML() + "<br>\n"
                    strings.append(string)
                    k = k + 1
            elif len(textAreaList) == 0:
                while(k != (len(textBoxList))):
                    string = labelList[k].ElementToHTML() + "<br>\n" + textBoxList[k].ElementToHTML() + "<br>\n"
                    strings.append(string)
                    k = k + 1
                    
            elif len(textBoxList) == 0:
                while(k != (len(textAreaList))):
                    string = labelList[k].ElementToHTML() + "<br>\n" + textAreaList[k].ElementToHTML() + "<br>\n"
                    strings.append(string)
                    k = k + 1
        
        newstrings = []
        while len(strings) != 0:
            index = random.randint(0,len(strings)-1)
            item = strings[index]
            strings.remove(item)
            newstrings.append(item)
        strings = newstrings
        newstrings = []
        prob = random.randint(0,1)
        print(prob)
        if prob == 1:
            flag3 = 0
            prob2 = random.randint(0,1)
            if prob2 != 0:
                string2 = ""
                for x in strings:
                    string2 = string2 + x
                flag3 = 1
                newstrings.append(string2)
            if len(dropdownList) != 0:
                string = ""
                for x in dropdownList:
                    string = string + x.ElementToHTML() + "<br>\n"
                if string != "": 
                    newstrings.append(string)
            if flag3 == 0:
                prob2 = random.randint(0,1)
                if prob2 != 0:
                    string2 = ""
                    for x in strings:
                        string2 = string2 + x
                    flag3 = 1
                    newstrings.append(string2)
            if len(checkList) != 0:
                string = ""
                for x in checkList:
                    string = string + x.ElementToHTML() + "<br>\n"
                if string != "": 
                    newstrings.append(string)
            if flag3 == 0:
                prob2 = 1
                if prob2 != 0:
                    string2 = ""
                    for x in strings:
                        string2 = string2 + x
                    flag3 = 1
                    newstrings.append(string2)
            
        else:
            flag3 = 0
            prob2 = random.randint(0,1)
            if prob2 != 0:
                string2 = ""
                for x in strings:
                    string2 = string2 + x
                flag3 = 1
                newstrings.append(string2)
            if len(dropdownList) != 0:
                string = "<div class=\"flex-container1\" style=\"url(https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38) no-repeat center/ cover;\">"
                for x in dropdownList:
                    string = string +"<div>"+x.ElementToHTML()+"</div>"
                string = string + "</div><br>\n"
                if string != "<div class=\"flex-container1\" style=\"url(https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38) no-repeat center/ cover;\">": 
                    newstrings.append(string)
            if flag3 == 0:
                prob2 = random.randint(0,1)
                if prob2 != 0:
                    string2 = ""
                    for x in strings:
                        string2 = string2 + x
                    flag3 = 1
                    newstrings.append(string2)
            if len(checkList) != 0:
                string = "<div class=\"flex-container1\" style=\"url(https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38) no-repeat center/ cover;\">"
                for x in checkList:
                    string = string +"<div>"+x.ElementToHTML()+"</div>"
                string = string + "</div><br>\n"
                if string != "<div class=\"flex-container1\" style=\"url(https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38) no-repeat center/ cover;\">": 
                    newstrings.append(string)
            if flag3 == 0:
                prob2 = 1
                if prob2 != 0:
                    string2 = ""
                    for x in strings:
                        string2 = string2 + x
                    flag3 = 1
                    newstrings.append(string2)
        
        if len(buttonList) != 0:
            string = "<div class=\"flex-container1\" style=\"url(https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38) no-repeat center/ cover;\">"
            for x in buttonList:
                string = string + "<div>"+x.ElementToHTML()+"</div>"
                
            string = string + "</div><br>"
            newstrings.append(string)        
        arrangeList = newList
        newList = []
        while len(arrangeList) != 0:
            index = random.randint(0,len(arrangeList)-1)
            item = arrangeList[index]
            arrangeList.remove(item)
            newList.append(item)
        k = 0
        arrangeList = newList
        """
"""
        while (k < len(arrangeList)):
            if type(arrangeList[k]) == type(labelTest) and k != (len(arrangeList)-1):
                if type(arrangeList[k+1]) == type(labelTest):
                    index = random.randint(0,len(arrangeList)-1)
                    item = arrangeList[index]
                    if type(item) == type(labelTest):
                        while(type(item) == type(labelTest)):
                            index = random.randint(0,len(arrangeList)-1)
                            item = arrangeList[index]
                    item2 = arrangeList[k]
                    arrangeList[k] = item
                    arrangeList[index] = item2
            k = k + 1
        """
"""
        flag4 = 0
        if len(arrangeList) > 0:
            flag1 = 0
            string3 = "<div class=\"flex-container\" style=\"url(https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38) no-repeat center/ cover;\">"
            
            for x in arrangeList:
                flag = 0
                if type(x) == type(headerTest):
                    flag = 1
                else:
                    flag = random.randint(0,1)
                
                if flag == 1:
                    if flag4 == 0:
                        if type(x) == type(labelTest):
                            f.write("<div class=\"flex-container2\" style=\"url(https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38) no-repeat center/ cover;\">"+x.ElementToHTML()+"</div><br>")
                        else:
                            f.write(x.ElementToHTML())
                            f.write("<br>\n")
                    else:
                        if type(x) == type(headerTest):
                            f.write("</div>\n" + x.ElementToHTML() + "<br>\n") 
                        else:
                            f.write("<div>" + x.ElementToHTML() + "</div></div><br>\n" )
                        flag4 = 0
                    k = random.randint(0,1)
                    if k == 1 and flag1 == 0:
                        string = ""
                        for x in newstrings:
                            string = string + x 
                        f.write("<div>" + string + "</div><br>\n")
                        flag1 = 1
                        
                else:
                    if flag4 == 0:
                        flag4 = 1
                        f.write(string3 + "<div>" + x.ElementToHTML() + "</div>")
                    else:
                        f.write("<div>" + x.ElementToHTML() + "</div>")
            if flag1 == 0:
                
                string = ""
                for x in newstrings:
                    string = string + x
                f.write("<div>" + string + "</div><br>\n")
                flag1 == 1
        if flag4 == 1:
            f.write("</div><br>\n")
        if foot != None:
            f.write(foot.ElementToHTML())
            
        f.write("</body>\n")
        f.write("</html>\n")
"""