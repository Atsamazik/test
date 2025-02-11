"""
URL configuration for legal_forms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]

from rest_framework.routers import DefaultRouter
from django.urls import path, include

from forms.views import *

router = DefaultRouter()
router.register(r'answers', RequestWithAnswerViewSet)
router.register(r'texts', RequestWithTextViewSet)
router.register(r'booleans', RequestWithBooleanViewSet)
router.register(r'files', RequestWithFileViewSet)
router.register(r'numbers', RequestWithNumberViewSet)
router.register(r'form_submission', FormSubmissionViewSet, basename='form_submission')

urlpatterns.extend([
    path('api/', include(router.urls)),
])

