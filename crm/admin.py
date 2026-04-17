from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.contrib import messages
from xhtml2pdf import pisa

from .models import Cliente, Plano, PlanoCliente,Servico

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'documento', 'tipo', 'telefone', 'data_inicio', 'contrato_assinado', 'ativo')
    list_filter = ('tipo', 'ativo', 'contrato_assinado', 'data_inicio')
    search_fields = ('nome', 'documento', 'email')
    list_editable = ('contrato_assinado', 'ativo')
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('tipo', 'documento', 'nome')
        }),
        ('Contato', {
            'fields': ('email', 'telefone')
        }),
        ('Endereço', {
            'fields': ('cep','endereco','cidade','bairro')
        }),
        ('Status', {
            'fields': ('data_inicio', 'contrato_assinado', 'ativo')
        }),
    )

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome', 'descricao')
    list_editable = ('ativo',)

@admin.register(PlanoCliente)
class PlanoClienteAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'plano', 'data_inicio', 'status', 'get_valor_final')
    list_filter = ('status', 'plano', 'data_inicio')
    search_fields = ('cliente__nome', 'cliente__documento', 'plano__nome')
    autocomplete_fields = ('cliente', 'plano')
    actions = ['gerar_carta_deposito']

    def get_valor_final(self, obj):
        return f"R$ {obj.get_valor()}"
    get_valor_final.short_description = 'Valor Final'

    # @admin.action(description='Gerar Carta de Depósito (PDF)')
    # def gerar_carta_deposito(self, request, queryset):
    #     if queryset.count() > 1:
    #         self.message_user(request, "Selecione apenas UM vínculo por vez para gerar a carta de depósito.", level=messages.ERROR)
    #         return

    #     plano_cliente = queryset.first()
    #     cliente = plano_cliente.cliente
    #     plano = plano_cliente.plano
    #     valor = plano_cliente.get_valor()

    #     context = {
    #         'plano_cliente': plano_cliente,
    #         'cliente': cliente,
    #         'plano': plano,
    #         'valor': valor,
    #     }

    #     # Render HTML e gera PDF com xhtml2pdf
    #     try:
    #         html_string = render_to_string('crm/carta_deposito.html', context)
            
    #         response = HttpResponse(content_type='application/pdf')
    #         filename = f"carta_deposito_{cliente.nome.replace(' ', '_')}.pdf"
    #         response['Content-Disposition'] = f'attachment; filename="{filename}"'

    #         pisa_status = pisa.CreatePDF(html_string, dest=response)

    #         if pisa_status.err:
    #             self.message_user(request, "Erro ao gerar o PDF com pisa.", level=messages.ERROR)
    #             return None

    #         return response
    #     except Exception as e:
    #         self.message_user(request, f"Erro ao gerar PDF: {str(e)}", level=messages.ERROR)
    

    @admin.action(description='Abrir Carta para Impressão')
    def gerar_carta_deposito(self, request, queryset):
        if queryset.count() > 1:
            self.message_user(request, "Selecione apenas um.", level=messages.ERROR)
            return
        
        obj = queryset.first()
        url = reverse('gerar_carta_pdf', args=[obj.pk]) # Certifique-se de criar a URL no urls.py
        
        # Isso abre a view em uma nova aba usando JavaScript
        return HttpResponseRedirect(url) 
        # Ou use um script JS para abrir em target="_blank"
