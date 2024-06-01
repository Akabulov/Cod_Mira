import PyPDF2
from sklearn.model_selection import train_test_split
from tensorflow.python import keras
from tensorflow.python.keras.layers import TextVectorization, Embedding, LSTM, Dense
from tensorflow.python.keras import Sequential


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page in range(pdf_reader.numPages):
            text += pdf_reader.getPage(page).extractText()
    return text

resumes = [...]
parameters = [...]

resumes_train, resumes_test, parameters_train, parameters_test = train_test_split(resumes, parameters, test_size=0.2)

# Create a TextVectorization layer
vectorizer = keras.layers.TextVectorization(max_tokens=10000, output_sequence_length=500)
vectorizer.adapt(resumes_train)

num_parameters = 2

model = Sequential()
model.add(TextVectorization(max_tokens=10000, output_sequence_length=500))
model.add(Embedding(input_dim=10000, output_dim=128))
model.add(LSTM(128))
model.add(Dense(64, activation='relu'))
model.add(Dense(num_parameters, activation='softmax'))


model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(resumes_train, parameters_train, epochs=10, batch_size=32)


predictions = model.predict(resumes_test)
