
from django.contrib import admin
from django.urls import path
from apis.views import TodoAPIView,RucAPIView,NombreAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('instituto/', TodoAPIView.as_view()),
    path('ruc/', RucAPIView.as_view()),
    path('nombre/', NombreAPIView.as_view()),
]
