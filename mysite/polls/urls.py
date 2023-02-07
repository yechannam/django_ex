from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('polls/', include('poll.urls')),
    path('admin/', admin.site.urls),
]