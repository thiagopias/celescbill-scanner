from CelescPdfReader import CelescPdfReader

celesc = CelescPdfReader("celesc.pdf")
print(celesc.get_data_emissao())
print(celesc.get_data_vencimento())
print(celesc.get_valor_fatura())


