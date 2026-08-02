import streamlit as st
import pandas as pd
import requests

# Base URL of the Flask backend
BACKEND_URL = "http://backend:5000"

# Set the title of the Streamlit app
st.title("Super Kart Sales Forecasting Model")

# Section for online prediction
st.subheader("Online Prediction")

# Input fields for product and store data
Product_Weight = st.number_input("Product Weight", min_value=0.0, value=12.66)
Product_Sugar_Content = st.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"])
Product_Allocated_Area = st.number_input("Product Allocated Area",min_value=0.0,value=0.027) #Complete the code to define the UI element for Product_Allocated_Area
Product_MRP = st.number_input("Product MRP",min_value=0.0,value=117.08) #Complete the code to define the UI element for Product_MRP
Store_Size = st.selectbox("Store Size",["Small", "Medium", "High"]) #Complete the code to define the UI element for Store_Size
Store_Location_City_Type = st.selectbox("Store Location City Type",["Tier 1", "Tier 2", "Tier 3"]) #Complete the code to define the UI element for Store_Location_City_Type
Store_Type = st.selectbox("Store Type",["Supermarket Type1", "Supermarket Type2", "Departmental Store", "Food Mart"]) #Complete the code to define the UI element for Store_Type
Product_Id_char = st.selectbox("Product ID Prefix",["FD", "DR", "NC"]) #Complete the code to define the UI element for Product_Id_char
Store_Age_Years = st.number_input("Store Age (Years)",min_value=0,value=15) #Complete the code to define the UI element for Store_Age_Years
Product_Type_Category = st.selectbox("Product Type Category",["Frozen Foods","Dairy","Canned","Baking Goods","Health and Hygiene","Snack Foods","Meat","Household","Fruits and Vegetables","Hard Drinks","Soft Drinks","Breads","Starchy Foods","Breakfast","Seafood","Others"]) #Complete the code to define the UI element for Product_Type_Category

product_data = {
    "Product_Weight": Product_Weight,
    "Product_Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": Product_Allocated_Area,
    "Product_MRP": Product_MRP,
    "Store_Size": Store_Size,
    "Store_Location_City_Type": Store_Location_City_Type,
    "Store_Type": Store_Type,
    "Product_Id_char": Product_Id_char,
    "Store_Age_Years": Store_Age_Years,
    "Product_Type_Category": Product_Type_Category
}


# Make prediction when the "Predict" button is clicked
if st.button("Predict", type="primary"):
    response = requests.post(f"{BACKEND_URL}/v1/predict", json=product_data)  # Send data to Flask API
    if response.status_code == 200:
        prediction = response.json()['Sales']
        st.success(f"Predicted Product Store Sales Total: ₹{prediction:,.2f}")
    else:
        st.error("Unable to connect to the prediction API.")
