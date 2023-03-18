from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import DetailView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from .htmlGenerator import outputTemplate
from .models import AIProject
from textInput.models import TextPage
from imageInput.models import ImagePage
from allauth.account.forms import LoginForm, SignupForm


def homeView(request):
    return render(request, 'custom/home.html')


@login_required
def profileView(request):
    if request.method == 'POST':
        userForm = UserUpdateForm(request.POST, instance=request.user)
        imgForm = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if userForm.is_valid() and imgForm.is_valid():
            userForm.save()
            imgForm.save()
            messages.success(request, f'Account Info Updated!')
            return redirect('custom_profile')
    else:
        userForm = UserUpdateForm(instance=request.user)
        imgForm = ProfileUpdateForm(instance=request.user.profile)
    content = {
        'title': 'Profile',
        'userForm': userForm,
        'imgForm': imgForm
    }
    return render(request, 'custom/profile.html', content)


class projectsView(ListView):
    model = AIProject
    template_name = 'custom/projects.html'
    context_object_name = 'projects'


def purposeView(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            maker = request.user
        else:
            try:
                maker = User.objects.get(username='anonymous')
            except User.DoesNotExist:
                maker = User.objects.create(username='anonymous', email='an@an.com', password='testing321')
        projectName = request.POST['projectName']
        purpose = request.POST['purpose']
        Home = bool(request.POST.get('Home', False))
        About = bool(request.POST.get('About', False))
        Contact = bool(request.POST.get('Contact', False))
        Custom = bool(request.POST.get('Custom', False))
        customName = request.POST['customPageName']
        if not Home and not About and not Contact and not Custom:
            messages.error(
                request, 'ERROR - Choose to create at least one page')
            return redirect('custom_purpose')
        if projectName == '':
            messages.error(
                request, 'ERROR - Website name is required')
            return redirect('custom_purpose')
        else:
            newProject = AIProject.objects.create(creator=maker,
                                                  name=projectName,
                                                  purpose=purpose,
                                                  homePage=Home,
                                                  aboutPage=About,
                                                  contactPage=Contact,
                                                  customPage=Custom,
                                                  customPageName=customName)
            if 'textInputSubmit' in request.POST:
                newProject.projectType = "Text"
                newProject.save()
                if Home:
                    TextPage.objects.create(
                        parent=newProject,
                        pageType='Home',
                        pageName='Home'
                    )
                if About:
                    TextPage.objects.create(
                        parent=newProject,
                        pageType='About',
                        pageName='About'
                    )
                if Contact:
                    TextPage.objects.create(
                        parent=newProject,
                        pageType='Contact',
                        pageName='Contact'
                    )
                if Custom:
                    TextPage.objects.create(
                        parent=newProject,
                        pageType='Custom',
                        pageName=customName
                    )
                messages.success(request, f'{newProject.name} created successfully')
                return redirect('custom_text_input', newProject.id)
            elif 'imageInputSubmit' in request.POST:
                newProject.projectType = "Image"
                newProject.save()
                if Home:
                    ImagePage.objects.create(
                        parent=newProject,
                        pageType='Home',
                        pageName='Home'
                    )
                if About:
                    ImagePage.objects.create(
                        parent=newProject,
                        pageType='About',
                        pageName='About'
                    )
                if Contact:
                    ImagePage.objects.create(
                        parent=newProject,
                        pageType='Contact',
                        pageName='Contact'
                    )
                if Custom:
                    ImagePage.objects.create(
                        parent=newProject,
                        pageType='Custom',
                        pageName=customName
                    )
                messages.success(request, f'{newProject.name} created successfully')
                return redirect('custom_image_input', newProject.id)
    return render(request, "custom/purpose.html")


def CustomLoginView(request):
    return render(request, 'custom/signuppage.html', {'loginForm': LoginForm, 'signupForm': SignupForm})
