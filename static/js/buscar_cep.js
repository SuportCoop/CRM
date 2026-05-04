// buscar_cep.js

// Função para iniciar a lógica do CEP
const initCepBusca = ($) => {
    $(document).ready(function() {
        $('#id_cep').on('blur', function() {
            var cep = $(this).val().replace(/\D/g, '');
            if (cep.length === 8) {
                $('#id_endereco').val('...');
                $('#id_bairro').val('...');
                $('#id_cidade').val('...');
                $('#id_uf').val('...');

                $.getJSON(`https://viacep.com.br/ws/${cep}/json/`, function(dados) {
                    if (!("erro" in dados)) {
                        $('#id_endereco').val(dados.logradouro);
                        $('#id_bairro').val(dados.bairro);
                        $('#id_cidade').val(dados.localidade);
                        $('#id_uf').val(dados.uf);
                        $('#id_numero').focus();
                    } else {
                        alert("CEP não encontrado.");
                    }
                });
            }
        });
    });
};

// Tenta encontrar o jQuery do Django em intervalos de 100ms
var checkJQuery = setInterval(function() {
    if (typeof django !== 'undefined' && django.jQuery) {
        initCepBusca(django.jQuery);
        clearInterval(checkJQuery);
    } else if (typeof jQuery !== 'undefined') {
        initCepBusca(jQuery);
        clearInterval(checkJQuery);
    }
}, 100);