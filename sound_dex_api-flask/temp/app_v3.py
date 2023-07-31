from flask import Flask, request, jsonify
from flask_cors import CORS
from clean_word import ThaiSoundex
app = Flask(__name__)
# thai_soundex = ThaiSoundex().run_clean_text('เทส')
# print(thai_soundex)


@app.route("/tokenize", methods=["POST"])
def tokenize():
    res = request.get_json()
 
    if res['text']:
        fa_token = ThaiSoundex()
        result = fa_token.run_clean_text(res['text'])

    return jsonify(clean_text=result,text=res['text'])



if __name__ == "__main__":
    app.run(debug=True)