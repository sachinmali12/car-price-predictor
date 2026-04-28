from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load model
model = pickle.load(open("model/car_price_model.pkl", "rb"))
columns = pickle.load(open("model/columns.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.form.to_dict()

        # Convert numeric values
        year = float(data["Year"])
        present_price = float(data["Present_Price"])
        kms = float(data["Kms_Driven"])
        owner = float(data["Owner"])

        # 🔥 CREATE Car_Age (IMPORTANT)
        car_age = 2026 - year

        # Build correct input
        input_dict = {
            "Car_Age": car_age,
            "Present_Price": present_price,
            "Kms_Driven": kms,
            "Owner": owner,
            "Fuel_Type_Petrol": int(data["Fuel_Type_Petrol"]),
            "Seller_Type_Dealer": int(data["Seller_Type_Dealer"]),
            "Transmission_Manual": int(data["Transmission_Manual"])
        }

        df = pd.DataFrame([input_dict])

        # Match training columns
        df = df.reindex(columns=columns, fill_value=0)

        prediction = model.predict(df)[0]

        return {"prediction": round(prediction, 2)}

    except Exception as e:
        return {"error": str(e)}
    
if __name__ == "__main__":
    app.run(debug=True)