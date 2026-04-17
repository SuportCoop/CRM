from django.shortcuts import render, get_object_or_404
from .models import PlanoCliente

def gerar_carta_pdf_view(request, pk):
    plano_cliente = get_object_or_404(PlanoCliente, pk=pk)
    context = {
        'plano_cliente': plano_cliente,
        'cliente': plano_cliente.cliente,
        'plano': plano_cliente.plano,
        'valor': plano_cliente.get_valor(),
    }
    return render(request, 'crm/carta_pdf_print.html', context)