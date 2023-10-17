from flask_restful import Resource, reqparse, request
import json

from server.db_utils import *

parser = reqparse.RequestParser()

class Data(Resource):
    def get(self):
        data = exec_get_all("SELECT id, trick, difficulty FROM skate ORDER BY id ASC")
        result = {}
        for entry in data:
            result[entry[0]] = {
                "id": entry[0],
                "trick": entry[1],
                "difficulty": entry[2]
            }
        return result


class Edit(Resource):
    def put(self, id):
        parser.add_argument('trick', type = str)
        parser.add_argument('difficulty', type = str)
        args = parser.parse_args()
        trick = args['trick']
        difficulty = args['difficulty']
        exec_commit("UPDATE skate SET trick=%s, difficulty=%s WHERE id=%s", [trick, difficulty, id])


    def delete(self, id):
        exec_commit("DELETE FROM skate WHERE id=%s", [id])
