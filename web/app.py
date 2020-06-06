from flask import Flask,jsonify,request
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

def checkPostedData(postedData,functionName):
	if (functionName == "add" or functionName == "substract" or functionName == "multiply"):
		if "x" not in postedData or "y" not in postedData:
			return 301
		else:
			return 200
	elif (functionName == "division"):
		if "x" not in postedData or "y" not in postedData:
			return 301
		elif int(postedData["y"])==0:
			return 302
		else:
			return 200


class Add(Resource):
	def post(self): 
		#If I am here , then the resouce Add was requested using the method POST
		#Step 1 : GEt posted data
		postedData = request.get_json()
		#Step 1b : Verify validity of posted data
		
		status_code = checkPostedData(postedData,"add")

		if (status_code!=200):
			 retJson = {
			 	"Message":"An error happened",
			 	"StatusCode":status_code
			 }
			 return jsonify(retJson)

		#If I am here then StatusCode=200

		x = postedData["x"]
		y = postedData["y"]
		x = int(x)
		y = int(y)

		#Step 2 : Add the posted data
		ret = x+y
		retMap = {
			"Message":ret , 
			"StatusCode": 200
		}
		return retMap
	# def get(self):
	# 	#If I am here , then the resouce Add was requested using the method GET
	# def 	

class Substract(Resource):
		def post(self): 
			#If I am here , then the resouce Substract was requested using the method POST
			#Step 1 : GEt posted data
			postedData = request.get_json()
			#Step 1b : Verify validity of posted data
			
			status_code = checkPostedData(postedData,"substract")

			if (status_code!=200):
				 retJson = {
				 	"Message":"An error happened",
				 	"StatusCode":status_code
				 }
				 return jsonify(retJson)

			#If I am here then StatusCode=200

			x = postedData["x"]
			y = postedData["y"]
			x = int(x)
			y = int(y)

			#Step 2 : Substract the posted data

			ret = x-y
			retMap = {
				"Message":ret , 
				"StatusCode": 200
			}
			return retMap
	# def get(self):
	# 	#If I am here , then the resouce Add was requested using the method GET
	# def 	

class Multiply(Resource):
		def post(self): 
		#If I am here , then the resouce Substract was requested using the method POST
		#Step 1 : GEt posted data
			postedData = request.get_json()
			#Step 1b : Verify validity of posted data
			
			status_code = checkPostedData(postedData,"multiply")

			if (status_code!=200):
				 retJson = {
				 	"Message":"An error happened",
				 	"StatusCode":status_code
				 }
				 return jsonify(retJson)

			#If I am here then StatusCode=200

			x = postedData["x"]
			y = postedData["y"]
			x = int(x)
			y = int(y)

			#Step 2 : Multiply the posted data

			ret = x*y
			retMap = {
				"Message":ret , 
				"StatusCode": 200
			}
			return retMap

class Divide(Resource):
		def post(self): 
		#If I am here , then the resouce Substract was requested using the method POST
		#Step 1 : GEt posted data
			postedData = request.get_json()
			#Step 1b : Verify validity of posted data
			
			status_code = checkPostedData(postedData,"division")

			if (status_code!=200):
				 retJson = {
				 	"Message":"An error happened",
				 	"StatusCode":status_code
				 }
				 return jsonify(retJson)

			#If I am here then StatusCode=200

			x = postedData["x"]
			y = postedData["y"]
			x = int(x)
			y = int(y)

			#Step 2 : Divide the posted data

			ret = (x*1.0)/y
			retMap = {
				"Message":ret , 
				"StatusCode": 200
			}
			return retMap


api.add_resource(Add,       "/add")
api.add_resource(Substract, "/substract")
api.add_resource(Multiply,  "/multiply")
api.add_resource(Divide,    "/division")

 

# @app.route('/add_two_nums',methods =["POST"])
# def add_two_nums():
# 	#Get x,y from posted data
# 	dataDict = request.get_json()

# 	if "y" not in dataDict:
# 		return "ERROR",305

# 	x = dataDict["x"]
# 	y = dataDict["y"]
# 	z= x+y

# 	retJSON = {
# 		"z":z
# 	}
# 	return jsonify(retJSON), 200

if __name__=="__main__":
	app.run(host='0.0.0.0')
