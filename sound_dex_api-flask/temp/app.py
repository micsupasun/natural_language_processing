from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name = {name}, views = {views}, likes = {likes})"

db.create_all()

# names = {"tim": {"age": 19,"gender": "male"},
#         "bill":{"age": 70,"gender": "male"}}
# class HelloWorld(Resource):
#     def get(self):
#         return {"data": "Hello"}
# api.add_resource(HelloWorld,"/helloworld/")
# response = requests.get(BASE + "helloworld")

#     def post(self):
#         return {"data": "Posted"}
# api.add_resource(HelloWorld,"/helloworld/")
# response = requests.post(BASE + "helloworld")

    # def get(self, name, test):
    #     return {"name": name, "test":test}
# api.add_resource(HelloWorld,"/helloworld/<string:name>/<int:test>")
# response = requests.get(BASE + "helloworld/tim/19")

# names = {"tim": {"age": 19,"gender": "male"},
#         "bill":{"age": 70,"gender": "male"}}
#     def get(self, name):
#         return names[name]
# api.add_resource(HelloWorld,"/helloworld/<string:name>")
# response = requests.get(BASE + "helloworld/bill")

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video is required")
video_update_args.add_argument("views", type=int, help="Views of the video")
video_update_args.add_argument("likes", type=int, help="Likes of the video")

def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Could not find video...")

def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(409, message="Video already exists with that ID...")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}


class Video(Resource):

    # def put(self, video_id):
    #     print(request.form['likes'])
    #     return {}
# api.add_resource(Video,"/video/<int:video_id>")
# response = requests.put(BASE + "video/1", {"likes": 10})

#     def put(self, video_id):
#         args = video_put_args.parse_args()
#         return {video_id: args}
# api.add_resource(Video,"/video/<int:video_id>")
# response = requests.put(BASE + "video/1", {"likes": 10})

    # def get(self, video_id):
    #     abort_if_video_id_doesnt_exist(video_id)
    #     return videos[video_id]
    # def put(self, video_id):
    #     abort_if_video_exists(video_id)
    #     args = video_put_args.parse_args()
    #     videos[video_id] = args
    #     return videos[video_id], 201
    # def delete(self, video_id):
    #     abort_if_video_exists(video_id)
    #     del videos[video_id]
    #     return '', 204
# api.add_resource(Video,"/video/<int:video_id>")
# data = [{"likes": 78, "name": "Joe", "views": 100000}, 
#         {"likes": 10000, "name": "How to make REST API", "views": 80000},
#         {"likes": 35, "name": "Tim", "views": 2000}]


# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())
# input()
# response = requests.delete(BASE + "video/0")
# print(response)
# input()
# response = requests.get(BASE + "video/2")
    @marshal_with(resource_fields)
    def get(self, video_id):
        # result = VideoModel.query.get(id=video_id)
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Could not find video with that id")
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video id taken...")

        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video doesn't exist, cannot update")
        
        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']
   
        db.session.commit()

        return result

    def delete(self, video_id):
        abort_if_video_exists(video_id)
        del videos[video_id]
        return '', 204
api.add_resource(Video,"/video/<int:video_id>")





if __name__ == "__main__":
    app.run(debug=True)

    # https://www.youtube.com/watch?v=GMppyAPbLYk