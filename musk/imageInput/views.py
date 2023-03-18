from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import DetailView
from custom.models import AIProject
from imageInput.models import ImagePage
from .ImageInputSrc.main import preprocessing, processImage
from musk.settings import BASE_DIR
import os
import shutil

# Create your views here.


def image_inputListView(request, pk):
    pages = ImagePage.objects.filter(parent=pk)
    project = AIProject.objects.get(id=pk)
    projectName = project.name
    # list of folders to make or cd to, when saving webages
    htmlfolders = ["imageInput", "static", "outputHTML", str(
            project.creator.username), str(project.name)]
    imgfolders = ['media', 'pageImages', 'imageInput', project.creator.username, project.name]
    # deleting project
    if request.method == 'POST':
        made = False
        for page in pages:
            if page.made == True:
                made = True
        # deleting project html folder
        if made == True:
            root = BASE_DIR
            for folder in htmlfolders:
                dir = os.path.join(root, folder)
                if os.path.exists(dir):
                    root = dir
            shutil.rmtree(dir)
            root = BASE_DIR
            # deleting project images folder
            for folder in imgfolders:
                dir = os.path.join(root, folder)
                if os.path.exists(dir):
                    root = dir
            shutil.rmtree(dir)
        # deleting project from database
        AIProject.objects.filter(id=pk).delete()
        messages.error(request, f'{projectName} deleted successfully')
        return redirect('custom_home')
    return render(request, 'imageInput/image_input.html', {'pages': pages})


def image_inputDetailView(request, parent, pk):
    page = ImagePage.objects.get(id=pk, parent=parent)
    if request.method == 'POST':
        page.img = request.FILES.get('imageUpload')
        page.save()
        # list of folders to make or cd to, when saving webages
        folders = ["imageInput", "static", "outputHTML", str(
            page.parent.creator.username), str(page.parent.name)]
        root = BASE_DIR
        for folder in folders:
            dir = os.path.join(root, folder)
            if not os.path.exists(dir):
                os.mkdir(dir)
            root = dir
        outputPath = os.path.join(root, f'{page.pageName}.html')
        detectedImagePath = os.path.join(root, f'{page.pageName}.png')
        # # Creating the webpage
        path = f'/home/swapnil/ai-musks/aawb/musk/media/{str(page.img)}'
        processed_image=preprocessing(path)
        processImage(processed_image, outputPath, detectedImagePath)
        page.made = True
        page.save()
        messages.success(request, f'{page.pageName} for {page.parent.name} created successfully')
        return redirect('custom_image_input', parent)
    return render(request, 'imageInput/image_input_detail.html', {'page': page})

def customizationView(request, parent, pk):
    page = ImagePage.objects.get(id=pk, parent=parent)
    user = page.parent.creator.username
    projectName = page.parent.name
    pageName = page.pageName
    context = {
        'creator': user,
        'projectName': projectName,
        'pageName': pageName
    }
    return render(request, "textInput/customization.html", context)
