"""
URL configuration for practiceapps project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from practiceapps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage),
    path('about-us/', views.aboutUs),
    path('course/', views.course),
    # URL patterns for int, str, slug and random dynamic URLs respectively
    path('course/<int:courseid>', views.courseDetails),
    path('course/<str:coursedet>', views.courseDetailsStr),
    path('course/<slug:courseslug>', views.courseDetailsSlug),
    path('course/<courserand>', views.courseDetailsRand),
    path('userform', views.userForm),
    path('submitform', views.submitform, name="submitform"),
    path('evenodd', views.evenodd),
    path('marksheet', views.marksheet)
]
