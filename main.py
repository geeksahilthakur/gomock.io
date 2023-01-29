from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
import docx
import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

app = Flask(__name__)
app.config['SECRET_KEY'] = 'superscribe'
app.config['UPLOAD_FOLDER'] = 'static/files'


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")


@app.route('/', methods=['GET', "POST"])
@app.route('/home', methods=['GET', "POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data  # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'],
                               secure_filename(file.filename)))  # Then save the file
        # print(file.filename)
        global fname
        fname = file.filename
        return "File has been uploaded."
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)


def fun():
    m = fname
    return m

#################

    nltk.download('punkt')
    nltk.download('stopwords')


    mm = fun()
    print("jelloooo ")
    print(mm)

    def extract_skills(resume_text):
        # Tokenize the resume text
        word_tokens = word_tokenize(resume_text)

        # Remove stop words
        stop_words = set(stopwords.words('english'))
        word_tokens = [word for word in word_tokens if word.lower() not in stop_words]

        # Extract skills
        skills = []
        with open("C:\\Users\\hp\\Desktop\\moKer\\skill.txt") as f:
            skills_list = f.read().splitlines()
        for token in word_tokens:
            if token.lower() in skills_list:
                skills.append(token)
        return skills


    # Extract text from .docx file
    def extract_text_from_docx(filepath):
        doc = docx.Document(filepath)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        return '\n'.join(fullText)


    # Extract text from .pdf file
    def extract_text_from_pdf(filepath):
        pdfFileObj = open(filepath, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        text = ""
        for i in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(i)
            text += pageObj.extractText()
        pdfFileObj.close()
        return text


    # Read the resume file
    file_path = "C:\\Users\hp\\Desktop\\moKer\\Resume1.docx"  # or "resume.pdf"
    extracted_text = ""
    if file_path.endswith('.docx'):
        extracted_text = extract_text_from_docx(file_path)
    elif file_path.endswith('.pdf'):
        extracted_text = extract_text_from_pdf(file_path)

    # Extract skills from the resume
    skills = extract_skills(extracted_text)
    print(skills)





