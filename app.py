from flask import Flask, render_template, request
from converter import convertToHTML


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/convertMessage', methods=['POST'])
def convertMessage():
    text = request.form['message']
    return convertToHTML(text)

@app.route('/convertFile', methods=['POST'])
def convertFile():
    file = request.files['file']
    if file:
        file_contents = file.read()
        file_string = file_contents.decode('utf-8')
    return convertToHTML(file_string)

if __name__ == 'main__':
    app.run()