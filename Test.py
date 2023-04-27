from flask import Flask, render_template, request
from keybert import KeyBERT
import pickle

app = Flask(__name__)

# Load the saved model
with open('C:/Users/wiss/Python/Projet_5/API/model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def extract_keywords():
    keywords = None
    if request.method == 'POST':
        sentence = request.form['sentence']
        keywords = model.extract_keywords(sentence)
        keywords = [kw[0] for kw in keywords]
    return render_template('keywords.html', keywords=keywords)

if __name__ == '__main__':
    app.run(port=3000, debug=True)