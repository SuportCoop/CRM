from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from crm.views import gerar_carta_pdf_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plano-cliente/<int:pk>/pdf/', gerar_carta_pdf_view, name='gerar_carta_pdf'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)