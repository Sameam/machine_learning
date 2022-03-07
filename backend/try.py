import os 
import pandas as pd 
import numpy as np 
import json
import pickle 


data = {'Area': '190', 'Perimeter': '290', 'MajorAxisLength': '109', 'MinorAxisLength': '290', 'AspectRation': '60', 'Eccentricity': '80', 'ConvexArea': '390', 
        'EquivDiameter': '490', 'Extent': '506', 'Solidity': '304', 'roundness': '42', 'Compactness': '304', 'ShapeFactor1': '405', 'ShapeFactor2': '904', 'ShapeFactor3': '34', 'ShapeFactor4': '32'}

values = []
for key, value in data.items():
  values.append(value)
data = np.array([values])

svc_model = pickle.load(open('svc_model', 'rb'))

result = svc_model.predict(data)
print(result)


  