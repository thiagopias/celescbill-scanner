from CelescPdfReader import CelescPdfReader

celesc = CelescPdfReader("celesc-2023-09-02.pdf")
#celesc = CelescPdfReader("celesc.pdf")

print(celesc.get_data_emissao())
print(celesc.get_data_vencimento())
print(celesc.get_valor_fatura())
print(celesc.get_celesc_data_leitura_anterior())


