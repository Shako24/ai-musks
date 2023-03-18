from django.urls import path
from . import views

urlpatterns = [
     path('image_input/<int:pk>', views.image_inputListView,
          name='custom_image_input'),
     path('image_input/<int:parent>/<int:pk>', views.image_inputDetailView,
          name='custom_image_input_detail'),
     path('image_input/<int:parent>/<int:pk>/customization', views.customizationView,
         name='custom_image_customization'),
]
