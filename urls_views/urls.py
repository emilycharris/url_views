"""urls_views URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from url_views_app.views import index_view, hello_view, balloon_view, extra_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view), # bulletpoint # 1 in assignment
    url(r'^hello', hello_view), #bulletpoint # 2 in assignment
    url(r'^99/red/balloons', balloon_view), #bulletpoint # 3 in assignment
    url(r'^extra', extra_view)

]
