import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/english_to_french")
def english_to_french():
    english_text=request.args.get('textToTranslate')
    # Write your code here
    machinetranslation.translator.english_to_french(english_text)
    return "Translated text to French"

@app.route("/french_to_english")
def french_to_english():
    french_text=request.args.get('textToTranslate')
    # Write your code here
    machinetranslation.translator.french_to_english(french_text)
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
