from flask import Flask, render_template, request
import pickle, numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    # When you first load the page, no values exist yet
    return render_template('index.html', result=None, values=[5]*9)

@app.route('/predict', methods=['POST'])
def predict():
    # Get all 9 slider values as floats
    data = [float(x) for x in request.form.values()]
    features = np.array(data).reshape(1, -1)
    prediction = model.predict(features)[0]
    result = "Malignant" if prediction == 4 else "Benign"
    # Pass both the result and the current slider values back to the page
    return render_template('index.html', result=f"Tumor is likely {result}", values=data)

if __name__ == '__main__':
    app.run(debug=True)
