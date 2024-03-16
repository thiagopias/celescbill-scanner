import PyPDF2
import pandas as pd
from datetime import datetime

#show full lines and columns when visualizing the dataframe
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)




class CelescPdfReader:
    def __init__(this, pdfFileName: str ):
        reader = PyPDF2.PdfReader(pdfFileName)
        page = reader.pages[0]
        txt = page.extract_text()
        lista = txt.split('\n')
        this.df = pd.DataFrame(lista)

    def isCelesc(this) -> bool:
        df = this.df.loc[this.df[0].str.contains("Celesc Distribuicao S.A")]
        if len(df) > 0:
            return True
        return False
    

    def printPdf(this):
        print(this.df)

    def get_data_emissao(this) -> datetime:
        searchString = "EMISSÃO:"
        index = this.df.loc[this.df[0].str.contains(searchString)]
        #EMISSÃO: 16/02/2024 APRES.: 19/02/2024 NOTA FISCAL/CONTA DE ENERGIA ELÉTRICA - SÉRIE ÚNICA: 000.249.514.290 - FAT-01-202411136312055-5 REF.:02/2024
        if len(index) > 0:
            line = index.values[0][0]
            date_string = line.split(":")[1].split(" ")[1] #'18/08/2023'
            date_object = datetime.strptime(date_string, '%d/%m/%Y').date()
            return date_object
        
        return None
    

    def get_data_vencimento(this) -> datetime:
        searchString = "VENCIMENTO"
        df = this.df.loc[this.df[0].str.contains(searchString)]
        if len(df) > 0:
            # string encontrada no indice 58:	41054204VENCIMENTO
            #pega o valor da data de vencimento na proxima linha, 58 + 1 = 59
            data_vencimento_index = df.index.values[0] + 1
            newDf = this.df[this.df.index == data_vencimento_index]
            date_string = newDf.values[0][0]
            date_object = datetime.strptime(date_string, '%d/%m/%Y').date()
            return date_object
        
        return None

    def get_valor_fatura(this) -> float:
        searchString = "VALOR ATÉ O VENCIMENTO"
        df = this.df.loc[this.df[0].str.contains(searchString)]
        if len(df) > 0:
            index_valor = df.index.values[0] + 1
            valor_string = this.df[this.df.index == index_valor][0].values[0].split(" ")[1]
            valor_string = valor_string.replace(",",".")
            valor_float = float(valor_string)
            return valor_float
        return None        

    def get_celesc_data_leitura_anterior(this) -> datetime:
        searchString = "Data da leitura anterior:"
        df = this.df.loc[this.df[0].str.contains(searchString)]
        if len(df) > 0:
            #exemplo string encontrada no indice 17.	Data da leitura anterior: 19/07/2023
            data_index = df.index.values[0]
            newDf = this.df[this.df.index == data_index]
            date_string = newDf.values[0][0]
            date_string = date_string.split(":")[1].strip()
            date_object = datetime.strptime(date_string, '%d/%m/%Y').date()
            return date_object
        
        return None
        




class CelescBillingInfo:
    def __init__(this, periodo, celesc_valorfatura, celesc_datavcto, interno_valorfaturainterna,
                 celesc_leituraatual, celesc_ultimaleitura, celesc_totalfaturado, celesc_leituraatualgtp,
                 celesc_ultimaleituragtp, celesc_totalinjetadowatts, celesc_consumotusd1, celesc_consumotusd2,
                 celesc_consumote1, celesc_consumote2, celesc_consumototal, celesc_injetadotusd1,
                 celesc_injetadotusd2, celesc_injetadote1, celesc_injetadote2, celesc_totalinjetado,
                 celesc_lancamentosservicos, celesc_pdfconta, interno_leituraRelogioApto01,
                 interno_leituraAnteriorRelogioApto01, interno_leituraRelogioApto1_img,
                 interno_totalWattsConsumidoApto01, interno_totalFaturaApto01, interno_leituraRelogioApto02,
                 interno_leituraAnteriorRelogioApto02, interno_leituraRelogioApto2_img,
                 interno_totalWattsConsumidoApto02, interno_totalFaturaApto02, interno_leituraRelogioApto03,
                 interno_leituraAnteriorRelogioApto03, interno_leituraRelogioApto3_img,
                 interno_totalWattsConsumidoApto03, interno_totalFaturaApto03, interno_leituraRelogioApto04,
                 interno_leituraAnteriorRelogioApt04, interno_leituraRelogioApto04_img,
                 interno_totalWattsConsumidoApto04, interno_totalFaturaApto04, interno_leituraRelogioApto05,
                 interno_leituraAnteriorRelogioApto05, interno_leituraRelogioApto05_img,
                 interno_totalWattsConsumidoApto05, interno_totalFaturaApto05, interno_leituraRelogioApto06,
                 interno_leituraAnteriorRelogioApto06, interno_leituraRelogioApto6_img,
                 interno_totalWattsConsumidoApto06, interno_totalFaturaApto06, interno_leituraRelogioOficina,
                 interno_leituraAnteriorRelogioOficina, interno_leituraRelogioOficina_img,
                 interno_totalWattsConsumidoOficina, interno_totalFaturaOficina, total_a_cobrar_interno):
        this.periodo = periodo
        this.celesc_valorfatura = celesc_valorfatura
        this.celesc_datavcto = celesc_datavcto
        this.interno_valorfaturainterna = interno_valorfaturainterna
        this.celesc_leituraatual = celesc_leituraatual
        this.celesc_ultimaleitura = celesc_ultimaleitura
        this.celesc_totalfaturado = celesc_totalfaturado
        this.celesc_leituraatualgtp = celesc_leituraatualgtp
        this.celesc_ultimaleituragtp = celesc_ultimaleituragtp
        this.celesc_totalinjetadowatts = celesc_totalinjetadowatts
        this.celesc_consumotusd1 = celesc_consumotusd1
        this.celesc_consumotusd2 = celesc_consumotusd2
        this.celesc_consumote1 = celesc_consumote1
        this.celesc_consumote2 = celesc_consumote2
        this.celesc_consumototal = celesc_consumototal
        this.celesc_injetadotusd1 = celesc_injetadotusd1
        this.celesc_injetadotusd2 = celesc_injetadotusd2
        this.celesc_injetadote1 = celesc_injetadote1
        this.celesc_injetadote2 = celesc_injetadote2
        this.celesc_totalinjetado = celesc_totalinjetado
        this.celesc_lancamentosservicos = celesc_lancamentosservicos
        this.celesc_pdfconta = celesc_pdfconta
        this.interno_leituraRelogioApto01 = interno_leituraRelogioApto01
        this.interno_leituraAnteriorRelogioApto01 = interno_leituraAnteriorRelogioApto01
        this.interno_leituraRelogioApto1_img = interno_leituraRelogioApto1_img
        this.interno_totalWattsConsumidoApto01 = interno_totalWattsConsumidoApto01
        this.interno_totalFaturaApto01 = interno_totalFaturaApto01
        this.interno_leituraRelogioApto02 = interno_leituraRelogioApto02
        this.interno_leituraAnteriorRelogioApto02 = interno_leituraAnteriorRelogioApto02
        this.interno_leituraRelogioApto2_img = interno_leituraRelogioApto2_img
        this.interno_totalWattsConsumidoApto02 = interno_totalWattsConsumidoApto02
        this.interno_totalFaturaApto02 = interno_totalFaturaApto02
        this.interno_leituraRelogioApto03 = interno_leituraRelogioApto03
        this.interno_leituraAnteriorRelogioApto03 = interno_leituraAnteriorRelogioApto03
        this.interno_leituraRelogioApto3_img = interno_leituraRelogioApto3_img
        this.interno_totalWattsConsumidoApto03 = interno_totalWattsConsumidoApto03
        this.interno_totalFaturaApto03 = interno_totalFaturaApto03
        this.interno_leituraRelogioApto04 = interno_leituraRelogioApto04
        this.interno_leituraAnteriorRelogioApt04 = interno_leituraAnteriorRelogioApt04
        this.interno_leituraRelogioApto04_img = interno_leituraRelogioApto04_img
        this.interno_totalWattsConsumidoApto04 = interno_totalWattsConsumidoApto04
        this.interno_totalFaturaApto04 = interno_totalFaturaApto04
        this.interno_leituraRelogioApto05 = interno_leituraRelogioApto05
        this.interno_leituraAnteriorRelogioApto05 = interno_leituraAnteriorRelogioApto05
        this.interno_leituraRelogioApto05