from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

translator = Translator()

@app.route('/', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        text_to_translate = request.form['text']
        target_language = request.form['language']
        
        try:
            translated_text = translator.translate(text_to_translate, dest=target_language)
            translated_text = translated_text.text
        except Exception as e:
            translated_text = str(e)
        
        return render_template('index.html', translated_text=translated_text)
    
    return render_template('index.html', translated_text=None)

if __name__ == '__main__':
    app.run(debug=True)
