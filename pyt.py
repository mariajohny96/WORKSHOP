from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/hello',methods=['GET'])
def hello():
	name=request.args.get("name",'')
	age=request.args.get("age",'')
	phone=request.args.get("phone",'')
	address=request.args.get("address",'')
	print request.__dict__
	return name + " " + age+ " " + phone + " " +address


if __name__ == '__main__':
	app.run()
