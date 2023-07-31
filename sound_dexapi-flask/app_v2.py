from flask import Flask, jsonify
from flask_restful import Resource, Api ,reqparse
from flask_pymongo import PyMongo
from clean_word import ThaiSoundex
# 
parser = reqparse.RequestParser()
# parser.add_argument('date', type=str)
parser.add_argument('word_not_clean', type=str)
# 

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/visipedia_annotation_toolkit"

mongo = PyMongo(app)
api = Api(app)
list_word = ['เพียร','ยรดา','เร','ควร','เวร','เฮร','กร','ครน','ฮรร','กรร','กรรม','ฮรรม','อย่า','กย่า','ทรี','ทราย','ไป','ใช้']

list_data = []
for i in range(len(list_word)):
    thai_soundex_class = ThaiSoundex().run_clean_text(f'{list_word[i]}')
    list_data.append({
                # "id": i,
                "word_not_clean": f"{list_word[i]}",
                "word_clean": thai_soundex_class
            })

class SoundexWordAll(Resource):
    def get(self):
        return jsonify(list_data)

class SoundexWordEach(Resource):
    def get(self):
        args = parser.parse_args()
        category_word_not_clean = args['word_not_clean']
        thai_soundex_class = ThaiSoundex().run_clean_text(category_word_not_clean)
        print(category_word_not_clean)
        print(thai_soundex_class)
        dict_data = {
            "word_not_clean": category_word_not_clean,
            "word_clean": thai_soundex_class
        }
        return jsonify(dict_data)


# http://127.0.0.1:5000/clean_word?word_not_clean=%E0%B9%80%E0%B8%9E%E0%B8%B5%E0%B8%A2%E0%B8%A3
api.add_resource(SoundexWordAll, '/')
api.add_resource(SoundexWordEach, '/clean_word')


if __name__ == "__main__":
    app.run(debug=True)