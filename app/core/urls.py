from django.contrib import admin
from django.urls import path, include 
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('music.urls')), 
    path('accounts/', include('accounts.urls')), 


    path('', RedirectView.as_view(url='/music/categories/', permanent=True)),
]