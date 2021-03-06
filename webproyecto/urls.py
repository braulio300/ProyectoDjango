"""webproyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path  #falta ponerle= 'include,'  antes del path y no hay otro archivo .py dentro de la carpeta app :s.
from core import views as core_views
from event import views as evento_views
from django.contrib.auth import views as auth_views #Necesario para el Log-in

from django.conf import settings
from django.views.generic import TemplateView

from core import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(redirect_authenticated_user=True)), #Necesario para Log-in
    path('accounts/', include('django.contrib.auth.urls')), #Necesario para Log-in
    path('registro/', core_views.registro, name='registro'), #Registro de usuarios   
    path('',core_views.home, name="home"),
    path('about/',core_views.about, name="about"),
    path('event/',evento_views.event, name="event"),
    path('contact/',core_views.contact, name="contact"),


    path('ajaxTest/', core_views.ajaxTest, name="ajaxTest"),
    path('ajaxTestResponse/', core_views.ajaxTestResponse, name="ajaxTestResponse"),
    
    path('contactAjax/', core_views.contactAjax, name="contactAjax"),
    path('contactAjaxResponse', core_views.contactAjaxResponse, name="contactAjaxResponse"),
    
    path('admin/', admin.site.urls),

    # Ruta para ServiceWorker.js 'sw.js'.
    path('sw.js',
         TemplateView.as_view(template_name='sw.js', content_type='application/javascript'), name='sw.js'),

    path("login/", views.login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path("", views.home, name="home"),
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)