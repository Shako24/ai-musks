
from nbformat import read
from Webpage import Webpage
from Header import Header
from TextBox import TextBox
from Paragraph import Paragraph
from TextArea import TextArea
from Button import Button
from CheckBox import CheckBox
from DropDown import DropDown
from Footer import Footer
from Label import Label
from NavBar import NavBar
from Image import Image
from Link import Link
from TextNLP import TextNLP
print("How many navbars")
k = input()
numnav = k
print("How many headers")
k = input()
numhead = k
print("How many buttons")
k = input()
numbutt = k
print("How many checkboxes")
k = input()
numcheck = k
print("How many dropdowns")
k = input()
numdrop = k
print("how many footers")
k = input()
numfoot = k
print("how many images")
k = input()
numimg = k
print("How many labels")
k = input()
numlabel = k
print("How many paragraphs")
k = input()
numpara = k
print("How many textareas")
k = input()
numTextArea = k
print("How many textboxs")
k = input()
numtextbox = k
print("How many links")
k = input()
count = 1
numlink = k
list = []
k = 0
while(k < int(numnav)):
    e = NavBar(count)
    list.append(e)
    k = k + 1
    count = count + 1
k = 0
while(k < int(numhead)):
    e = Header(count)
    list.append(e)
    k = k + 1
    count = count + 1
k = 0
while(k < int(numbutt)):
    e = Button(count)
    list.append(e)
    k = k + 1
    count = count + 1
k = 0
while(k < int(numcheck)):
    e = CheckBox(count)
    list.append(e)
    k = k + 1
    count = count + 1
k = 0
while(k < int(numdrop)):
    e = DropDown(count)
    list.append(e)
    k = k + 1
    count = count + 1
k = 0
while(k < int(numfoot)):
    e = Footer(count)
    list.append(e)
    k = k + 1
    count = count + 1
k = 0
while(k < int(numimg)):
    e = Image(count)
    list.append(e)
    k = k + 1
    count = count + 1
k = 0
while(k < int(numlabel)):
    e = Label(count)
    list.append(e)
    k = k + 1
    count = count + 1
k = 0
while(k < int(numpara)):
    e = Paragraph(count)
    list.append(e)
    k = k + 1
    count = count + 1
k = 0
while(k < int(numtextbox)):
    e = TextBox(count)
    list.append(e)
    k = k + 1
    count = count + 1
k = 0
while(k < int(numTextArea)):
    e = TextArea(count)
    list.append(e)
    k = k + 1
    count = count + 1
k = 0
while(k < int(numlink)):
    e = Link(count)
    list.append(e)
    k = k + 1
    count = count + 1
k = 0
webpage = Webpage()
for x in list:
    webpage.addWebpageElement(x)

k = TextNLP()
print("Write a paragraph explaining the webpage")
para = input()
print(k.process(para))
webpage.WebpageToHTML("output.html",k.process(para))


"""
1 NavBar
1 header
1 image
1 link
1 label
1 Footer
2 form types (horizontal and vertical) -- textb, ta,  
checkbox(no label needed) , 
"""