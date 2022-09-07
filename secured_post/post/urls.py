from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostView.as_view()),
    path('<int:id>/',views.PostView.as_view()),
]