from django.urls import path
from . import views

urlpatterns = [
    path('text_input/<int:pk>', views.text_inputListView,
         name='custom_text_input'),
    path('text_input/<int:parent>/<int:pk>',
         views.text_inputDetailView, name='custom_text_input_detail'),
    path('text_input/<int:parent>/<int:pk>/customization',
         views.customizationView, name='custom_customization'),
]
