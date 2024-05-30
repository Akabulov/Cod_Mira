import aspose.words as aw
import os

cvdir = r'C:\Users\Коста\Desktop\Cod_Mira\src\ExampleCV\CV'
ccvdir = r'C:\Users\Коста\Desktop\Cod_Mira\src\ConvertedCV'


def convert():
    for filename in os.listdir(cvdir):
        if filename not in os.listdir(ccvdir):
            cv_path = os.path.join(cvdir, filename)
            input_doc = aw.Document(cv_path)
            input_doc.save(ccvdir + cv_path.split('/')[-1]+'.pdf')

