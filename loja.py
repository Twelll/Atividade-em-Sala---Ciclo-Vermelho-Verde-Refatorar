from abc import ABC, abstractmethod

"""
===============================================================================
PADRÃO DE PROJETO APLICADO: Strategy (Comportamental)
===============================================================================
Participantes mapeados no domínio:
- Strategy: estrategia_pagamento_base
  Define a interface comum para os algoritmos de cálculo de pagamento.
  
- Concrete Strategies (Estratégias Concretas):
  1. pagamento_a_vista: Encapsula o cálculo aplicando desconto comercial.
  2. pagamento_parcelado_sem_juros: Mantém o valor integral original.
  3. pagamento_parcelado_com_juros: Encapsula o acréscimo percentual de juros.

- Context (Contexto):
  - venda: Mantém os dados da operação comercial e uma referência para a
    estratégia escolhida, delegando a responsabilidade do cálculo.
===============================================================================
"""


class estrategia_pagamento_base(ABC):
    """Interface abstrata base para todas as estratégias de pagamento."""

    @abstractmethod
    def calcular(self, valor_base: float) -> float:
        pass


class pagamento_a_vista(estrategia_pagamento_base):
    """Strategy: pagamento à vista com dedução percentual."""

    def __init__(self, desconto_percentual: float = 0.0):
        self.desconto_percentual = desconto_percentual

    def calcular(self, valor_base: float) -> float:
        desconto = valor_base * (self.desconto_percentual / 100.0)
        return valor_base - desconto


class pagamento_parcelado_sem_juros(estrategia_pagamento_base):
    """Strategy: parcelamento simples sem cobrança de encargos."""

    def calcular(self, valor_base: float) -> float:
        return valor_base


class pagamento_parcelado_com_juros(estrategia_pagamento_base):
    """Strategy: parcelamento com aplicação de juros."""

    def __init__(self, juros_percentual: float = 0.0):
        self.juros_percentual = juros_percentual

    def calcular(self, valor_base: float) -> float:
        acrescimo = valor_base * (self.juros_percentual / 100.0)
        return valor_base + acrescimo


class venda:
    """Contexto: delega o cálculo total para a estratégia configurada."""

    def __init__(self, valor_base: float, estrategia_pagamento: estrategia_pagamento_base):
        self.valor_base = valor_base
        self.estrategia_pagamento = estrategia_pagamento

    def calcular_total(self) -> float:
        return self.estrategia_pagamento.calcular(self.valor_base)


"""
===============================================================================
AUTOAVALIAÇÃO (PASSO 3 DO ESTUDO DIRIGIDO)
===============================================================================
1. Critérios Atingidos:
   - Critério 1: Testes em ficheiro separado com as 3 variações de comportamento (Atingido).
   - Critério 2: Três commits identificados por 'red', 'green' e 'refactor' (Atingido).
   - Critério 3: Commit red com testes que falham e sem a implementação que os faz passar (Atingido).
   - Critério 4: Refatoração com padrão Strategy aplicado, documentado e participantes nomeados (Atingido).
   - Critério 5: Suíte executada e 100% dos testes aprovados após a refatoração (Atingido).

2. Mudanças Estruturais entre as Fases Green e Refactor:
   - Na fase green, o cálculo estava centralizado na classe 'venda' através de
     condicionais e verificação de tipos ('isinstance').
   - Na fase refatorada, o padrão Strategy foi aplicado formalmente com herança
     da classe abstrata 'ABC'. Cada modalidade tornou-se uma classe autónoma que
     implementa o método 'calcular', e o contexto 'venda' passou a delegar essa
     chamada polimorficamente, eliminando acoplamento e estruturas condicionais (if/elif).

3. Maior Dificuldade Encontrada:
   - A sintaxe e convenções da linguagem Python (por estar em fase de aprendizagem,
     sendo este o principal motivo para recorrer à IA) e a assimilação prática do
     ciclo estrito do TDD (red-green-refactor).

4. Papel da Inteligência Artificial:
   - Como ajudou: Auxiliou na escrita da sintaxe em Python, na melhoria do português
     e clareza dos comentários, no esclarecimento de dúvidas sobre comandos do Git/GitHub
     e na aplicação do padrão Strategy.
   - Onde atrapalhou/exigiu intervenção: Dificuldade em seguir instruções estritas à primeira;
     foi necessário reformular os prompts várias vezes para obter o comportamento desejado.
     Inicialmente gerou código misturando convenções de nomenclatura (CamelCase em vez do
     snake_case solicitado)

5. Registo de Execução da Suíte de Testes (pytest):
   ============================= test session starts =============================
   collected 3 items

   test_venda.py ...                                                        [100%]

   ============================== 3 passed in 0.02s ==============================
===============================================================================
"""