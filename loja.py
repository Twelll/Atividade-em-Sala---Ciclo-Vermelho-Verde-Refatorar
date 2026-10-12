class pagamento_a_vista:
    def __init__(self, desconto_percentual=0.0):
        self.desconto_percentual = desconto_percentual


class pagamento_parcelado_sem_juros:
    def __init__(self):
        pass


class pagamento_parcelado_com_juros:
    def __init__(self, juros_percentual=0.0):
        self.juros_percentual = juros_percentual


class venda:
    def __init__(self, valor_base, estrategia_pagamento):
        self.valor_base = valor_base
        self.estrategia_pagamento = estrategia_pagamento

    def calcular_total(self):
        if isinstance(self.estrategia_pagamento, pagamento_a_vista):
            desconto = self.valor_base * (self.estrategia_pagamento.desconto_percentual / 100.0)
            return self.valor_base - desconto

        elif isinstance(self.estrategia_pagamento, pagamento_parcelado_sem_juros):
            return self.valor_base

        elif isinstance(self.estrategia_pagamento, pagamento_parcelado_com_juros):
            acrescimo = self.valor_base * (self.estrategia_pagamento.juros_percentual / 100.0)
            return self.valor_base + acrescimo

        return self.valor_base