from flask import Flask, request, jsonify
import joblib
import pandas as pd


# Create Flask App
app = Flask(__name__)


# Create API routing call
@app.route('/predict', methods=['POST'])
def predict():
    
    # Get JSON Request
    feat_data = request.json
    # Convert JSON request to Pandas DataFrame
    df = pd.DataFrame(feat_data)
    # Match Column Na,es
    df = df.reindex(columns=col_names)
    # Get prediction
    prediction = list(model.predict(df))
    # Return JSON version of Prediction
    return jsonify({'prediction': str(prediction)})

        

if __name__ == '__main__':

    # LOADS MODEL AND FEATURE COLUMNS
    
    print("Wadakam Let's Predict Your Health")
    print("Choose a Classifier: ")
    print("1. Adaptive Boosting,        Accuracy: 100%")
    print("2. Decision Tree,            Accuracy: 70.76%")
    print("3. Gradient Boosting,        Accuracy: 73.85%")
    print("4. Logistic Regression,      Accuracy: 78.46%")
    print("5. Logistic Regression CV,   Accuracy: 77.69%")
    print("6. Random Forrest,           Accuracy: 76.15")
    print("7. Support Vector Machine,   Accuracy: 77.69")
    
    i=0
    #print(str(list(range(1,8))))
    while(1):
        i = input("Enter(index 1,2 or 5): ")
        if i in str(list(range(1,8))): break
    
    
    col_names = joblib.load("./models/column_names.pkl")
    
    if i=='1':
        model = joblib.load("./models/Final Adaptive Boosting Classifier.pkl") 
         
    if i=='2':
        model = joblib.load("./models/Final Descision Tree Classifier.pkl")
        
    if i=='3':
        model = joblib.load("./models/Final Gradient Boosting Classifier.pkl")
        
    if i=='4':
        model = joblib.load("./models/Final Logistics Regression Model.pkl")
        
    if i=='5':
        model = joblib.load("./models/Final Logistics Regression Model CV.pkl")
        
    if i=='6':
        model = joblib.load("./models/Final Random Forrest Classifier.pkl")
        
    if i=='7':
        model = joblib.load("./models/Final Support Vector Machine.pkl")
        
    print("MODEL LOADED")

    app.run(debug=True)
