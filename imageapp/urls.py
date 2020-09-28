from django.urls import path, include
from imageapp import views
urlpatterns = [

    path('upload/', views.image_upload_view)

]
