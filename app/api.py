from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Загрузка модели
with open('../model/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([data['features']])
    return jsonify({'prediction': int(prediction[0])})
