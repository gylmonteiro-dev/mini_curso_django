"""
URL configuration for core project.

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
#from django.shortcuts import HttpResponse
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from produtos.views import pagina_inicial, cadastrar_produto, detalhar_produto

'''
def lista_produtos(request):
    return HttpResponse('<h1>Seja bem vindo</h1>')
'''


urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', pagina_inicial, name='pagina-inicial'),
    path('cadastrar/', cadastrar_produto, name='cadastra-produto'),
    path('produtos/<int:produto_id>/', detalhar_produto, name='detalha-produto')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
