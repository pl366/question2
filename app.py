from flask import Flask , request ,jsonify ,render_template
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin



app = Flask(__name__)
 

cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MONGO_DBNAME'] = 'gramener'
app.config['MONGO_URI'] = 'mongodb://admin:123456p@ds017175.mlab.com:17175/gramener'

          
mongo = PyMongo(app)


# @app.route('/')
# @cross_origin()
# def landing():
# 	return "/student : to enter details\n /students : to see all user entries"


@app.route('/', methods=['POST','GET'])
@cross_origin()
def student():
	if request.method == 'POST':
		name = str(request.form.get('name'))
		age = str(request.form.get('age'))
		gender = str(request.form.get('gender'))

		#print (type(gender))	
		#print (name,age,gender)
		#print (mongo.db.student)	
		p = {"name":name ,"age":age,"gender":gender}
		ps = mongo.db.student
		ps.insert_one(p)

		print ('Inserted data successfully')


	return render_template('studentform.html')

@app.route('/students')
@cross_origin()
def students():
	mycol = mongo.db.student
	mydoc = mycol.find()
	l = []
	for document in mydoc:
		l.append([str(document['name']),str(document['age']),str(document['gender'])])
	
	return render_template('index.html', std_list = l)
	


if __name__ == "__main__":
	app.run() 