# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import random

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

auditList = []

# Auxiliary string to array function
def splitStr(s):
    return [c for c in s]

# Axiliary logging function
def logThis(entry):
    n = len(auditList)
    auditList.insert(0,entry)
    maxLen = 10
    n = len(auditList)
    if n > maxLen:
        auditList.pop()

# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Audit(Resource):

	# corresponds to the GET request.
	# this function is called whenever there
	# is a GET request for this resource
	def get(self):
		return jsonify({'Last 10 calls:': '\n'.join(auditList)})

	# Corresponds to POST request
	def post(self):
		data = request.get_json()	 # status code
		return jsonify({'data': data}), 201


# another resource to calculate the square of a number
class Jumble(Resource):

	def get(self, myStr):
		
		msg = ("Endpoint: " + "/Jumble/" + myStr)
		arr =  (splitStr(myStr))
		random.shuffle(arr)
		myStr = "".join(str(x) for x in arr)
		logThis ('\n' + msg + " Result: " +  myStr )
		return jsonify((myStr))

# adding the defined resources along with their corresponding urls
api.add_resource(Audit, '/Audit')
api.add_resource(Jumble, '/Jumble/<myStr>')


# driver function
if __name__ == '__main__':

	app.run(debug = True)

