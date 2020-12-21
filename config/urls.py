"""config URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include# new
from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('category/<int:id>/<slug:slug>/', views.category_houses, name='category'),
    path('house/<int:id>/<slug:slug>/', views.house_detail, name='house_detail'),
    path('house/', include('house.urls')),
    path('home/', include('home.urls')),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('sss/', views.faq, name='faq'),
    path('blog/', include('blog.urls')), # new
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
