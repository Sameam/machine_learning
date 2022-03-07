from flask import Flask, request, jsonify
import numpy as np 
import pandas as pd 
import os
import json
import pickle 


app = Flask(__name__)

@app.route('/prediction', methods=['POST', 'GET'])
def make_prediction():
  if request.method == 'POST':
    data = request.json
    values = []
    for key, value in data.items():
      values.append(value)
    data = np.array([values])
    svc_model = pickle.load(open('svc_model', 'rb'))
    scaler = pickle.load(open('scaler', 'rb'))
    data = scaler.transform(data)
    result = svc_model.predict(data)
    return jsonify(result[0])
    
  
@app.route("/variable", methods=["GET"])
def get_variable():
  path = os.path.join("../DryBeanDataset","Dry_Bean_Dataset.xlsx")
  data = pd.read_excel(path)
  b =  np.array([{'name': i} for i in data.columns.values])
  b = b.tolist()
  return json.dumps(b[:-1])

  
  


  
  
