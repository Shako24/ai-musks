from django.shortcuts import render, redirect
from custom.models import AIProject
from .models import TextPage
from django.contrib import messages
from nbformat import read
from TextInputSrc.Webpage import Webpage
from TextInputSrc.Header import Header
from TextInputSrc.TextBox import TextBox
from TextInputSrc.Paragraph import Paragraph
from TextInputSrc.TextArea import TextArea
from TextInputSrc.Button import Button
from TextInputSrc.CheckBox import CheckBox
from TextInputSrc.DropDown import DropDown
from TextInputSrc.Footer import Footer
from TextInputSrc.Label import Label
from TextInputSrc.NavBar import NavBar
from TextInputSrc.Image import Image
from TextInputSrc.Link import Link
from TextInputSrc.TextNLP import TextNLP
import os
import shutil
from musk.settings import BASE_DIR

# Create your views here.


def text_inputListView(request, pk):
    pages = TextPage.objects.filter(parent=pk)
    project = AIProject.objects.get(id=pk)
    projectName = project.name
    # list of folders to make or cd to, when saving webages
    folders = ["textInput", "static", "outputHTML", str(
            project.creator.username), str(project.name)]
    # deleting project
    if request.method == 'POST':
        made = False
        # deleting project html folder
        for page in pages:
            if page.made == True:
                made = True
        if made == True:
            root = BASE_DIR
            for folder in folders:
                dir = os.path.join(root, folder)
                if os.path.exists(dir):
                    root = dir
            shutil.rmtree(dir)
        # deleting project from database
        AIProject.objects.filter(id=pk).delete()
        messages.error(request, f'{projectName} deleted successfully')
        return redirect('custom_home')
    return render(request, 'textInput/text_input.html', {'pages': pages})


def text_inputDetailView(request, parent, pk):
    page = TextPage.objects.get(id=pk, parent=parent)
    if request.method == 'POST':
        if bool(request.POST.get('NavbarCheckbox', False)):
            page.navbar = 1
        else:
            page.navbar = 0
        if bool(request.POST.get('FooterCheckbox', False)):
            page.footer = 1
        else:
            page.footer = 0
        heading = int(request.POST['HeadingTextbox'])
        checkbox = int(request.POST['CheckboxTextbox'])
        dropdown = int(request.POST['DropdownTextbox'])
        textbox = int(request.POST['TextboxTextbox'])
        paragraph = int(request.POST['ParagraphTextbox'])
        # label = int(request.POST['LabelTextbox'])
        image = int(request.POST['ImageTextbox'])
        textarea = int(request.POST['TextareaTextbox'])
        button = int(request.POST['ButtonTextbox'])
        # link = int(request.POST['LinkTextbox'])
        colorScheme = str(request.POST['colorScheme'])
        if (heading >= 0 and checkbox >= 0 and dropdown >= 0 and
            textbox >= 0 and paragraph >= 0 and image >= 0 and
                textarea >= 0 and button >= 0):
            page.heading = int(heading)
            page.checkbox = int(checkbox)
            page.dropdown = int(dropdown)
            page.textbox = int(textbox)
            page.paragraph = int(paragraph)
            # page.label = int(label)
            page.image = int(image)
            page.textarea = int(textarea)
            page.button = int(button)
            # page.link = int(link)
            page.colorScheme = str(colorScheme)
            page.save()
            # Making the page
            count = 1
            k = 0
            list = []
            # adding all elements to webpage object
            while(k < int(page.navbar)):
                e = NavBar(count)
                list.append(e)
                k = k + 1
                count = count + 1
            k = 0
            if (int(page.heading) > (int(page.image) + int(page.paragraph))):
                page.heading = page.image + page.paragraph
                
            while(k < int(page.heading)):
                e = Header(count)
                list.append(e)
                k = k + 1
                count = count + 1
            k = 0
            while(k < int(page.button)):
                e = Button(count)
                list.append(e)
                k = k + 1
                count = count + 1
            k = 0
            while(k < int(page.checkbox)):
                e = CheckBox(count)
                list.append(e)
                k = k + 1
                count = count + 1
            k = 0
            while(k < int(page.dropdown)):
                e = DropDown(count)
                list.append(e)
                k = k + 1
                count = count + 1
            k = 0
            while(k < int(page.footer)):
                e = Footer(count)
                list.append(e)
                k = k + 1
                count = count + 1
            k = 0
            while(k < int(page.image)):
                e = Image(count)
                list.append(e)
                k = k + 1
                count = count + 1
            k = 0
            # while(k < int(page.label)):
            #     e = Label(count)
            #     list.append(e)
            #     k = k + 1
            #     count = count + 1
            k = 0
            while(k < int(page.paragraph)):
                e = Paragraph(count)
                list.append(e)
                k = k + 1
                count = count + 1
            k = 0
            while(k < int(page.textbox)):
                e = TextBox(count)
                list.append(e)
                k = k + 1
                count = count + 1
            k = 0
            while(k < int(page.textarea)):
                e = TextArea(count)
                list.append(e)
                k = k + 1
                count = count + 1
            k = 0
            # while(k < int(page.link)):
            #     e = Link(count)
            #     list.append(e)
            #     k = k + 1
            #     count = count + 1
            # creating webpage string
            count = 0
            webpage = Webpage()
            for x in list:
                webpage.addWebpageElement(x)
            # getting nlp description from database
            k = TextNLP()
            para = page.colorScheme
            # if no description given, create string with "No input"
            if para == None:
                para = "No input"
            # list of folders to make or cd to, when saving webages
            folders = ["textInput", "static", "outputHTML", str(
                page.parent.creator.username), str(page.parent.name)]
            root = BASE_DIR
            for folder in folders:
                dir = os.path.join(root, folder)
                if not os.path.exists(dir):
                    os.mkdir(dir)
                root = dir
            outputPath = os.path.join(root, f'{page.pageName}.html')
            # Creating the webpage
            webpage.WebpageToHTML(outputPath, k.process(para))
            page.made = True
            page.save()
            messages.success(request, f'{page.pageName} for {page.parent.name} created successfully')
            return redirect('custom_text_input', parent)
        else:
            messages.error(
                request, 'ERROR - Negative values invalid')
            return redirect('custom_text_input_detail', parent, pk)
    return render(request, 'textInput/text_input_detail.html', {'page': page})


def customizationView(request, parent, pk):
    page = TextPage.objects.get(id=pk, parent=parent)
    user = page.parent.creator.username
    projectName = page.parent.name
    pageName = page.pageName
    context = {
        'creator': user,
        'projectName': projectName,
        'pageName': pageName
    }
    return render(request, "textInput/customization.html", context)
