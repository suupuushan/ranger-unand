'''
	Contoh Deloyment untuk Domain Data Science (DS)
	Orbit Future Academy - AI Mastery - KM Batch 3
	Tim Deployment
	2022
'''

# =[Modules dan Packages]========================

from flask import Flask,render_template,request,jsonify
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from joblib import load

# =[Variabel Global]=============================

app   = Flask(__name__, static_url_path='/static')
modelRF = None
modelGaussian = None
modelKNN = None
modelSVM = None

# =[Routing]=====================================

# [Routing untuk Halaman Utama atau Home]	
@app.route("/")
def beranda():
    return render_template('index.html')

# [Routing untuk API]	
@app.route("/api/deteksi",methods=['POST'])
def apiDeteksi():
	# Nilai default untuk variabel input atau features (X) ke model
	input_sepal_length = 5.1
	input_sepal_width  = 3.5
	input_petal_length = 1.4
	input_petal_width  = 0.2
	
	if request.method=='POST':
		# Set nilai untuk variabel input atau features (X) berdasarkan input dari pengguna
		input_sepal_length = float(request.form['sepal_length'])
		input_sepal_width  = float(request.form['sepal_width'])
		input_petal_length = float(request.form['petal_length'])
		input_petal_width  = float(request.form['petal_width'])
		modelType  = request.form['modelType']
		
		# Prediksi kelas atau spesies bunga iris berdasarkan data pengukuran yg diberikan pengguna
		df_test = pd.DataFrame(data={
			"SepalLengthCm" : [input_sepal_length],
			"SepalWidthCm"  : [input_sepal_width],
			"PetalLengthCm" : [input_petal_length],
			"PetalWidthCm"  : [input_petal_width]
		})

		if (modelType == "Random Forest"):
			hasil_prediksi = modelRF.predict(df_test[0:1])[0]
		elif (modelType == "GaussianNB"):
			hasil_prediksi = modelGaussian.predict(df_test[0:1])[0]
		elif (modelType == "KNN"):
			hasil_prediksi = modelKNN.predict(df_test[0:1])[0]
		else:
			hasil_prediksi = modelSVM.predict(df_test[0:1])[0]

		# Set Path untuk gambar hasil prediksi
		if hasil_prediksi == 'Iris-setosa':
			gambar_prediksi = '/static/img/iris_setosa.jpg'
		elif hasil_prediksi == 'Iris-versicolor':
			gambar_prediksi = '/static/img/iris_versicolor.jpg'
		else:
			gambar_prediksi = '/static/img/iris_virginica.jpg'
		
		# Return hasil prediksi dengan format JSON
		return jsonify({
			"prediksi": hasil_prediksi,
			"gambar_prediksi" : gambar_prediksi
		})

# =[Main]========================================

if __name__ == '__main__':
	
	# Load model yang telah ditraining
	modelRF = load('model_iris_rf.model')
	modelGaussian = load('model_iris_gaussian.model')
	modelKNN = load('model_iris_knn.model')
	modelSVM = load('model_iris_svm.model')

	# Run Flask di localhost 
	app.run(host="localhost", port=5000, debug=True)
	
	


