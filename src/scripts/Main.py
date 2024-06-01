import os

import nltk
import spacy
import Classificator as cltr
nltk.download('stopwords')
spacy.load('en_core_web_sm')

from tkinter import Tk
from tkinter.filedialog import askopenfilename

import time, datetime

from pyresparser import ResumeParser
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
import io, random


parameter_dict = {
                    'ds_keyword': ['tensorflow', 'keras', 'pytorch', 'machine learning', 'deep Learning', 'flask',
                                   'pandas', 'numpy', 'sklearn', ''],
                    'web_keyword': ['react', 'django', 'node jS', 'react js', 'php', 'laravel', 'magento', 'wordpress',
                                    'javascript', 'angular js', 'c#', 'flask'],
                    'android_keyword': ['android', 'android development', 'flutter', 'kotlin', 'xml', 'kivy'],
                    'ios_keyword': ['ios', 'ios development', 'swift', 'cocoa', 'cocoa touch', 'xcode'],
                    'uiux_keyword': ['ux', 'adobe xd', 'figma', 'zeplin', 'balsamiq', 'ui', 'prototyping', 'wireframes',
                                     'storyframes', 'adobe photoshop', 'photoshop', 'editing', 'adobe illustrator',
                                     'illustrator', 'adobe after effects', 'after effects', 'adobe premier pro',
                                     'premier pro', 'adobe indesign', 'indesign', 'wireframe', 'solid', 'grasp',
                                     'user research', 'user experience'],
                    'sa_keyword': ['uml', 'modeling', 'bpmn', 'workflow', 'confluence', 'ТЗ', 'api', 'postman', 'kibana', 'jira',
                                   'excel', 'bi', 'agile', 'scrum', 'dashboard']
                    }
key_relevancy = {'ds_keyword': 0, 'web_keyword': 0, 'android_keyword': 0, 'ios_keyword': 0, 'uiux_keyword': 0, 'sa_keyword': 0}

key_matches = {'ds_keyword': 'Data Science', 'web_keyword': 'WEB', 'android_keyword': 'Android', 'ios_keyword': 'IOS',
               'uiux_keyword': 'UI/UX', 'sa_keyword': 'System Analytics'}



# Перевод пдф файла в текст
def pdf_reader(file):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    with open(file, 'rb') as f:
        for page in PDFPage.get_pages(f,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
            print(page)
        text = fake_file_handle.getvalue()

    converter.close()
    fake_file_handle.close()
    return text


def parameter_setup(processed_pdf_file):
    for parameter in parameter_dict.keys():
        for value in parameter_dict[parameter]:
            if processed_pdf_file.count(value) >= 1:
                key_relevancy[parameter] += 1
                skill_set.append(value)


def parameter_predict():
    predict = sorted(key_relevancy.items(), key=lambda item: item[1], reverse=True)
    return key_matches[predict[0][0]]


Tk().withdraw()

pdf_file = askopenfilename(filetypes=[('PDF Files', '*.pdf')])
resume_text = ''
if pdf_file is not None:
    save_image_path = ''.join([r"C:\Users\Коста\Desktop\Cod_Mira\src\ScreenedCV\\", pdf_file.split('/')[-1]])
    with open(pdf_file, "rb") as fh:
        buf = io.BytesIO(fh.read()).getvalue()
    if os.path.exists(save_image_path):
        with open(save_image_path, "wb") as f:
            f.write(buf)
    else:
        with open(save_image_path, "w") as temp:
            pass
        with open(save_image_path, "wb") as f:
            f.write(buf)
    # Получение данных резюме
    resume_text = pdf_reader(save_image_path)

keywords = input('Parameters: ').split(' ')
print('\n\nResume analysis: ')
resume_text = resume_text.lower()
skill_set = []
parameter_setup(resume_text)
print()
print('\n\nPredicted skillset: '+ str(skill_set))
print()

recommended_skills = []
predict_field = parameter_predict()

cv_processor = cltr.CV()

print('\n\npredicted field of work: '+str(predict_field))

print('Predicted relevancy: '+str(cv_processor.relevancy_predict(keywords, *skill_set))+'%')

input('\n\nProcess finished')
