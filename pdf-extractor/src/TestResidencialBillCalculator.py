from ResidencialBillCalculator import BillCalculator

billing = BillCalculator()
billing.set_valor_conta(1000)
billing.add_unidade_consumidora('ap1',0,100)
billing.add_unidade_consumidora('ap2',0,200)
billing.add_unidade_consumidora('ap3',0,300)
billing.add_unidade_consumidora('ap4',0,400)
billing.add_unidade_consumidora('ap5',0,500)
billing.add_unidade_consumidora('ap6',0,600)
billing.add_unidade_consumidora('oficina',0,700)

print(billing.calcula_faturamento_interno())

