"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    #Plugin for Admin UI , Always place this above url(r'^admin/', admin.site.urls)
	url(r'^grappelli/', include('grappelli.urls')),
    #Url to access Admin Site. We can also include the admin's Documents ofr users.
    url(r'^admin/', admin.site.urls),
    # CSIT App URL's are present in CSIT Folder in (urls.py).
    url(r'', include('csit.urls')),   
]
