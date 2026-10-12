"""
1. Problema Escolhido:
   Cálculo do valor total final para vendas de veículos em uma concessionária,
   suportando diferentes condições comerciais de pagamento.

2. Padrão de Projeto Escolhido e Justificativa:
   - Padrão: Strategy.
   - Justificativa: O cálculo do valor final varia conforme a forma de pagamento
     escolhida. O Strategy permite encapsular cada regra de precificação em classes
     independentes e intercambiáveis (Open/Closed Principle), eliminando cadeias
     extensas de condicionais (if/elif/else) no contexto da venda e facilitando a 
     inclusão futura de novas modalidades de pagamento sem alterar o fluxo principal.

3. Casos de Teste (Variações de Comportamento):
   - Caso 1: Venda à vista (aplica desconto de 10% sobre o valor base).
   - Caso 2: Venda parcelada sem juros (valor base mantido integralmente, dividido em até 12x).
   - Caso 3: Venda parcelada com juros (aplica acréscimo de taxa sobre o valor base para prazos longos).

4. Estimativa de Tempo por Fase (Total: 120 minutos):
   - Fase de Planejamento (Passo 1): 10 minutos
   - Fase Red (escrita dos testes e commit red): 15 minutos
   - Fase Green (implementação mínima com condicionais e commit green): 15 minutos
   - Fase Refactor (aplicação do Strategy e commit refactor): 70 minutos
   - Autoavaliação e Finalização (Passo 3): 10 minutos

5. Declaração do Uso de Inteligência Artificial:
   - Uso de IA: Sim (Gemini / LLM).
   - Finalidade: Apoio na escrita de codigo, comentario e revisoes.
"""

import pytest
from loja import (
    venda,
    pagamento_a_vista,
    pagamento_parcelado_sem_juros,
    pagamento_parcelado_com_juros,
)

def test_venda_a_vista_com_desconto():
    estrategia_a_vista = pagamento_a_vista(desconto_percentual=10.0)
    venda_instancia = venda(valor_base=50000.0, estrategia_pagamento=estrategia_a_vista)

    total = venda_instancia.calcular_total()

    assert total == 45000.0


def test_venda_parcelada_sem_juros():
    estrategia_sem_juros = pagamento_parcelado_sem_juros()
    venda_instancia = venda(valor_base=50000.0, estrategia_pagamento=estrategia_sem_juros)

    total = venda_instancia.calcular_total()

    assert total == 50000.0


def test_venda_parcelada_com_juros():
    estrategia_com_juros = pagamento_parcelado_com_juros(juros_percentual=15.0)
    venda_instancia = venda(valor_base=50000.0, estrategia_pagamento=estrategia_com_juros)

    total = venda_instancia.calcular_total()

    assert total == 57500.0