from CelescPdfReader import CelescPdfReader

#celesc = CelescPdfReader("celesc-2023-09-02.pdf")
#celesc = CelescPdfReader("celesc-2023-10-02.pdf")
celesc = CelescPdfReader("../resources/celesc-2023-11-02.pdf")

#celesc = CelescPdfReader("celesc-2023-12-02.pdf")
#celesc = CelescPdfReader("celesc-2024-01-02.pdf")



#celesc-2023-11-02.pdf
#celesc.readerControl = -4

#celesc-2024-01-02.pdf
#celesc.readerControl = -4

print(celesc.get_data_emissao())
print(celesc.get_data_vencimento())
print(celesc.get_valor_fatura())
print(celesc.get_celesc_data_leitura_anterior())
print(celesc.get_celesc_leitura_anterior())
print(celesc.get_celesc_leitura_atual())
print(celesc.get_celesc_leitura_anterior_gtp())
print(celesc.get_celesc_leitura_atual_gtp())
print(celesc.get_celesc_consumo_faturado_no_mes())


#celesc-2023-12-02.pdf
#celesc.readerControl = 2

print('consumo tus ',celesc.get_celesc_consumo_tus())
print('consumo tus2 ',celesc.get_celesc_consumo_tus2())
print('consumo te',celesc.get_celesc_consumo_te())
print('consumo te2',celesc.get_celesc_consumo_te2())
#celesc.readerControl = 2


print('energia injetada tusd',celesc.get_celesc_energia_injetada_tusd())
print('energia injetada tusd2',celesc.get_celesc_energia_injetada_tusd2())
print('energia injetada te',celesc.get_celesc_energia_injetada_te())
print('energia injetada te2',celesc.get_celesc_energia_injetada_te2())

#celesc-2023-12-02.pdf
celesc.readerControl = 0

#celesc-2023-11-02.pdf
#celesc.readerControl = 15

#celesc.readerControl = -1

#celesc-2024-01-02.pdf
#celesc.readerControl = -4
print('energia injetada subtotal',celesc.get_celesc_energia_injetada_subtotal2())

#celesc-2023-11-02.pdf
#celesc.readerControl = -10

#celesc-2023-09-02.pdf
#celesc.readerControl = -4

#celesc-2024-01-02.pdf
#celesc.readerControl = 0
print('energia injetada lancamentos e servicos subtotal', celesc.get_celesc_lancamentos_e_servicos_subtotal2())







