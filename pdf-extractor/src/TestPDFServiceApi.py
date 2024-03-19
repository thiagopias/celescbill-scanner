from PDFServiceApi import TextExtractor
import time
from CelescPdfReader import CelescPdfReader

pdf = 'celesc-2023-09-02.pdf'
te = TextExtractor(pdf)
te.run_extraction_process()
te.extract_as_json_file()
df = te.extract_as_pandas_dataframe()
print(df)


#te.set_input_file_name('celesc-2024-01-02.pdf') 

#e.set_input_file_name('celesc-2024-02-02.pdf') 

#te.set_input_file_name('celesc-2024-03-02.pdf') 
