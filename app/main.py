from fastapi import FastAPI
from joblib import load 
from pydantic import BaseModel
from sklearn.datasets import load_iris
import pickle 

iris = load_iris()
class data_format(BaseModel):
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float
    

tree_model = pickle.load(open('model_tree.sav', 'rb')) 

app = FastAPI()

@app.get('/')
def root():
    print(tree_model)
    return "Tree Classifier API"

@app.post("/predict_flower")
def predict(data : data_format):
    test_data = [[
            data.sepal_length, 
            data.sepal_width, 
            data.petal_length, 
            data.petal_width
    ]]
    class_idx = tree_model.predict(test_data)[0]
    return { 'class' : iris.target_names[class_idx]}