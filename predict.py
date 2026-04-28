import pickle
import pandas as pd

# Load model
model = pickle.load(open("car_price_model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# Sample input
input_data = {
    "Year": 2014,
    "Present_Price": 5.59,
    "Kms_Driven": 27000,
    "Owner": 0,
    "Fuel_Type_Petrol": 1,
    "Fuel_Type_Diesel": 0,
    "Seller_Type_Dealer": 1,
    "Transmission_Manual": 1
}

df = pd.DataFrame([input_data])

# Align columns
df = df.reindex(columns=columns, fill_value=0)

prediction = model.predict(df)
print("Predicted Price:", prediction[0])