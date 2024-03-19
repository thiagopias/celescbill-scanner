class UnidadeConsumidora():
    def __init__(self, id: str, leitura_anterior: int, leitura_atual: int ):

        self.id = id
        if leitura_anterior > leitura_atual:
            raise Exception("Leitura anterior nao pode ser maior que leitura atual")


        self.leitura_anterior: int = leitura_anterior
        self.leitura_atual: int = leitura_atual
    
    def calcula_total_consumido_watts(self):
        total_consumido = self.leitura_atual - self.leitura_anterior
        return total_consumido
        

class BillCalculator():
    def __init__(self):
        self.valor_conta: float = 0
        self.ucs = [] #Lista de unidades consumidoras
        self.ucs_fatura = []

    def set_valor_conta(self, valor: float):
        self.valor_conta = valor

    def add_unidade_consumidora(self, id: str, leitura_anterior: int, leitura_atual: int):
        self.ucs.append(UnidadeConsumidora(id,leitura_anterior, leitura_atual))
    
    def calcula_total_consumido_watts(self) -> int:
        total_watts = 0
        for i in self.ucs:
            total_watts += i.calcula_total_consumido_watts()
        return total_watts

    def calcula_faturamento_interno(self) -> dict :
        self.ucs_fatura = []
        total_consumido_watts = self.calcula_total_consumido_watts()
        for i in self.ucs:
            #PARA CADA UNIDADE CONSUMIDORA
            total_uc = i.calcula_total_consumido_watts()

            fatuta_uc = total_uc * self.valor_conta / total_consumido_watts
            self.ucs_fatura.append(
                {
                    "uc": i.id,
                    "consumido": total_uc,
                    "valor_fatura": fatuta_uc
                }
            )
        return self.ucs_fatura