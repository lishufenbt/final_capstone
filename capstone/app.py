
import requests
import pickle
import numpy as np
import os
from flask import Flask,render_template,request,redirect
app = Flask(__name__)

@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/data')
def data():
	return render_template('data.html')

@app.route('/prediction',methods=["GET","POST"])
def prediction():   
	if request.method=='GET':
		return render_template('prediction.html')	
	else:
		CR1_code=request.form["CR1_code"]
		CR2_code=request.form["CR2_code"]
		CT1_code=request.form["CT1_code"]
		CT2_code=request.form["CT2_code"]
		BK_code=request.form["BK_code"]
		HOUR_code=request.form["HOUR_code"]
		MONTH_code=request.form["MONTH_code"]
		STWIDTH_code=request.form["STWIDTH_code"]

		model = pickle.load(open('model.pkl','rb'))
		result=model.predict([np.array([float(CR1_code),float(CR2_code),float(CT1_code),float(CT2_code),float(BK_code),float(HOUR_code),float(MONTH_code),float(STWIDTH_code)])])
		if result==1:
			return "It is likely that people get injured or killed"
		else:
			return "It is unlikely that people get injured or killed"
		

if __name__ == "__main__":
	port = os.environ.get("PORT", 5000)
	app.run(host='0.0.0.0', port=port)
