"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from taskmanagement import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/",views.hello,name="hello"),
    path("register/",views.RegisterAPIView,name="register"),
    path("login/",views.LoginAPIView,name="LoginAPIView"),
    path("postproduct/",views.post_product_admin,name="postproduct"),
    path("getproduct/",views.get_product_admin,name="getproduct"),
    path("getusers/",views.get_users,name="getusers"),
    path("getproductuser/<int:id>/",views.get_product_user,name="getproductuser"),
    path("getspecificproduct/<int:id>/",views.get_specific_product,name="getspecificproduct"),
    path("updateproduct/<int:id>/",views.update_product,name="updateproduct"),
    path("deleteproduct/<int:id>/",views.delete_product,name="deleteproduct"),
    path("postcomment/",views.post_comment,name="postcomment"),
    path("getcomments/<int:id>/",views.get_comments,name="getcomments")
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)