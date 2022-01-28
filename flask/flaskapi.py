from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


users_info = {
    1:{"name":"Andrew","age":18},
    2:{"name":"James","age":23},
    3:{"name":"Jordan","age":12},
    4:{"name":"Tobey","age":18},
}

user_notes = {
    1:["gotta go to the functions tonight","make lasagna at home"],
    2:["I just have only one note in this app"],
    3:[],
    4:["jordan is kinda sus","sussy baka jordan","i really dont like jordan","why does jordan always have to be with Lilly"]
}


class mainPage(Resource):

    def get(self):
        return {'message':"welcome, you're at home"}

class user_specific_details(Resource):
    # get user specific profile info
    def get(self,uid):
        if uid in users_info.keys():
            return {"user info":{uid:users_info[uid]}}
        return {"error":f"a user with uid = {uid} doesn't exist"}

class Notes(Resource):
    
    pass

api.add_resource(mainPage,'/')
api.add_resource(user_specific_details,'/users/<int:uid>')
api.add_resource(Notes,'/<uid>')

if __name__ == '__main__':
    app.run(debug = True)
    