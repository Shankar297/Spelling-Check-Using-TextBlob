from flask import Flask, render_template, request, url_for
from textblob import TextBlob

app = Flask('__name__')

@app.route('/', methods = ['GET'])
def home():
    return render_template('home.html')

@app.route('/check',methods = ['POST'])
def check():
    if request.method == 'POST':
        received_text = request.form['rawtext']
        text = TextBlob(received_text)
        text = text.correct()
    return render_template('home.html', your_text = received_text, corrected = text)
    

if __name__ =='__main__':
    app.run(debug=True)