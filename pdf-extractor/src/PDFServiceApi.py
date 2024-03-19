from adobe.pdfservices.operation.auth.credentials import Credentials
from adobe.pdfservices.operation.exception.exceptions import ServiceApiException, ServiceUsageException, SdkException
from adobe.pdfservices.operation.execution_context import ExecutionContext
from adobe.pdfservices.operation.io.file_ref import FileRef
from adobe.pdfservices.operation.pdfops.extract_pdf_operation import ExtractPDFOperation
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_pdf_options import ExtractPDFOptions
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_element_type import ExtractElementType

import os.path
import zipfile
import json
import pandas as pd

class TextExtractor():
    
    def __init__(this, input_file_name: str):
        this.path = '../resources/'
        this.input_file_name = input_file_name
        this.output_file_name = ""
        this.output_json_file_name = ""
        this.set_input_file_name(input_file_name)
        
        this.json_data = []

    def set_input_file_name(this, input_file_name: str):
        this.input_file_name = this.path + input_file_name
        this.output_file_name = this.path + input_file_name.replace("pdf", "zip")
        this.output_json_file_name = this.path + input_file_name.replace("pdf", "json")

    def loadCredentials(this):
        # Initial setup, create credentials instance.
        this.credentials = Credentials.service_principal_credentials_builder() \
            .with_client_id(os.getenv('PDF_SERVICES_CLIENT_ID')) \
            .with_client_secret(os.getenv('PDF_SERVICES_CLIENT_SECRET')) \
            .build()
        return this.credentials
    
    def run_extraction_process(this):
        zip_file = this.output_file_name
        
        output_file = this.output_file_name

        if os.path.isfile(output_file):
            os.remove(output_file)

        input_pdf = this.input_file_name #"./celesc-2023-09-02.pdf"

        try:

            # Initial setup, create credentials instance.
            credentials = this.loadCredentials()
            # Create an ExecutionContext using credentials and create a new operation instance.
            execution_context = ExecutionContext.create(credentials)
            extract_pdf_operation = ExtractPDFOperation.create_new()

            # Set operation input from a source file.
            source = FileRef.create_from_local_file(input_pdf)
            extract_pdf_operation.set_input(source)

            # Build ExtractPDF options and set them into the operation
            extract_pdf_options: ExtractPDFOptions = ExtractPDFOptions.builder() \
                .with_element_to_extract(ExtractElementType.TEXT) \
                .build()
            extract_pdf_operation.set_options(extract_pdf_options)

            # Execute the operation.
            result: FileRef = extract_pdf_operation.execute(execution_context)
            
            # Save the result to the specified location.
            result.save_as(output_file)

        except (ServiceApiException, ServiceUsageException, SdkException):
            print("Error extracting data from PDF file: ", this.input_file_name)


    def extract_as_json_file(this):
        zip_file = this.output_file_name
        output_file = this.output_json_file_name
        if os.path.isfile(this.output_json_file_name):
            print('removing '+this.output_json_file_name+' file')
            os.remove(this.output_json_file_name)

        input_pdf = this.input_file_name #"./celesc-2023-09-02.pdf"
        archive = None
        data = {}
        try:
            archive = zipfile.ZipFile(zip_file, 'r')
            
        except FileNotFoundError as err:
            print('Zip file not found. Automattically downloading the zip file from  PDF services API.')
            this.run_extraction_process()
            archive = zipfile.ZipFile(zip_file, 'r')

        if archive is not None:            
            jsonentry = archive.open('structuredData.json')
            jsondata = jsonentry.read()
            data = json.loads(jsondata)
            with open(this.output_json_file_name,'x') as f:
                json.dump(data, f)
                print(f'File {this.output_json_file_name} was created sucessfuly')
        else:
            print(f'File {this.output_json_file_name} was not created.')
        
        return data
            
        
    def extract_as_pandas_dataframe(this)-> pd.DataFrame:
        zip_file = this.output_file_name
        print('opening file ',zip_file)
        p = pd.DataFrame([])
        archive = None
        try:
            archive = zipfile.ZipFile(zip_file, 'r')
            
        except FileNotFoundError as err:
            print('Zip file not found. Automattically downloading the zip file from  PDF services API.')
            this.run_extraction_process()
            #this.extract_as_json_file()
            archive = zipfile.ZipFile(zip_file, 'r')
        
        
        if archive is not None:

            jsonentry = archive.open('structuredData.json')
            jsondata = jsonentry.read()
            data = json.loads(jsondata)
            allText = []
            for n, i in enumerate(data['elements']):
                if 'Text' in i:
                    try:

                        #print(n, i['Text'])
                        allText.append(i['Text'])
                        #time.sleep(1)
                        #print("")
                        #print("-------------------------")
                    except:
                        print('error trying to get Text property', 'line: ',n)
            p = pd.DataFrame(allText)
            
        return p
    
        