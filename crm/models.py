from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    TIPO_PESSOA_CHOICES = (
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    )

    tipo = models.CharField(max_length=2, choices=TIPO_PESSOA_CHOICES, default='PF')
    documento = models.CharField('CPF/CNPJ', max_length=20, unique=True)
    nome = models.CharField('Nome / Razão Social', max_length=200)
    email = models.EmailField('E-mail', blank=True, null=True)
    telefone = models.CharField('Telefone', max_length=20)
    
    cep = models.CharField('CEP', max_length=9)
    endereco = models.CharField('Endereço', blank=True , max_length=52) 
    numero = models.CharField('Número', max_length=20, blank=True)
    bairro = models.CharField('Bairro', blank=True , max_length=20)
    cidade = models.CharField('Cidade', blank=True , max_length=52)
    uf = models.CharField('UF', max_length=2, blank=True)
    
    data_inicio = models.DateField('Data de Início', default=timezone.now)
    contrato_assinado = models.BooleanField('Contrato Assinado?', default=False)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} ({self.documento})"

class Servico(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nome} "

class Plano(models.Model):
    TIPO_SERVICOS_CHOICES = (
        ('ZAP', 'ZAPFLOW'),
        ('CONS', 'CONSULTORIA'),
        ('DEV', 'DESENVOLVIMENTO'),
        ('LP', 'LANDING PAGE'),
    )
    nome = models.CharField('Plano',max_length=50)
    descricao = models.TextField('Descrição', blank=True)
    servico = models.ManyToManyField(Servico,default='ZAP')
    valor = models.DecimalField('Valor Base', max_digits=10, decimal_places=2)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'

    def __str__(self):
        return f"{self.nome} - R$ {self.valor}"


class PlanoCliente(models.Model):
    STATUS_CHOICES = (
        ('ativo', 'Ativo'),
        ('pendente', 'Pendente'),
        ('cancelado', 'Cancelado'),
        ('pausado', 'Pausado'),
    )

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='planos_contratados')
    plano = models.ForeignKey(Plano, on_delete=models.RESTRICT, related_name='clientes_vinculados')
    data_inicio = models.DateField('Data de Início', default=timezone.now)
    data_vencimento = models.IntegerField('Data de Vencimento', default=timezone.now)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='pendente')
    valor_cobrado = models.DecimalField(
        'Valor Cobrado', max_digits=10, decimal_places=2, null=True, blank=True,
        help_text="Deixe em branco para usar o valor padrão do plano."
    )

    class Meta:
        verbose_name = 'Plano do Cliente'
        verbose_name_plural = 'Planos dos Clientes'
        unique_together = ('cliente', 'plano')

    def __str__(self):
        return f"{self.cliente.nome} - {self.plano.nome}"
    
    def get_valor(self):
        return self.valor_cobrado if self.valor_cobrado is not None else self.plano.valor
