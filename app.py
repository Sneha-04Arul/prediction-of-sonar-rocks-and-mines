# from flask import Flask, request, render_template
# import numpy as np
# import joblib  # Replace `joblib` with your model library (e.g., pickle) if different

# app = Flask(__name__)

# # Load your trained model (ensure the path is correct)
# model = joblib.load('mine.sav')  

# @app.route('/')
# def home():
#     return render_template('index.html') 
# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Check if form data is provided
#         if 'input_data' not in request.form:
#             return "Error: No input provided. Please enter values."
        
#         # Get the input data from the form
#         input_data = request.form['input_data']
        
#         # Check if input is empty
#         if not input_data.strip():
#             return "Error: Input cannot be empty. Please provide comma-separated numeric values."
        
#         # Process the input into a list of floats
#         try:
#             input_data = [float(i) for i in input_data.split(',')]
#         except ValueError:
#             return "Error: Input contains invalid values. Ensure all values are numeric and comma-separated."

#         # Validate the number of inputs (60 required for your model)
#         if len(input_data) != 60:
#             return "Error: Exactly 60 numeric values are required. You provided {} values.".format(len(input_data))
        
#         # Reshape the input data and make a prediction
#         input_data_reshaped = np.asarray(input_data).reshape(1, -1)
#         prediction = model.predict(input_data_reshaped)

#         # Return the result
#         if prediction[0] == 'R':
#             return "The object is a Rock."
#         else:
#             return "The object is a Mine."

#     except Exception as e:
#         return f"An unexpected error occurred: {e}"

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, render_template
import numpy as np
import joblib  # Replace `joblib` with your model library (e.g., pickle) if different

app = Flask(__name__)

# Load your trained model (ensure the path is correct)
model = joblib.load('mine.sav')

@app.route('/')
def home():
    return render_template('index.html')  # Renders index.html in the templates folder

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if form data is provided
        if 'input_data' not in request.form:
            return "Error: No input provided. Please enter values."
        
        # Get the input data from the form
        input_data = request.form['input_data']
        
        # Check if input is empty
        if not input_data.strip():
            return "Error: Input cannot be empty. Please provide comma-separated numeric values."
        
        # Process the input into a list of floats
        try:
            input_data = [float(i) for i in input_data.split(',')]
        except ValueError:
            return "Error: Input contains invalid values. Ensure all values are numeric and comma-separated."

        # Validate the number of inputs (60 required for your model)
        if len(input_data) != 60:
            return "Error: Exactly 60 numeric values are required. You provided {} values.".format(len(input_data))
        
        # Reshape the input data and make a prediction
        input_data_reshaped = np.asarray(input_data).reshape(1, -1)
        prediction = model.predict(input_data_reshaped)

        # Render result page with the prediction result
        if prediction[0] == 'R':
            return render_template('result.html', prediction="Rock")
        else:
            return render_template('result.html', prediction="Mine")

    except Exception as e:
        return f"An unexpected error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
