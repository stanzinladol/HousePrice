
import streamlit as st
import pickle
import pandas as pd

# Load the trained model and columns
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('columns.pkl', 'rb') as columns_file:
    columns = pickle.load(columns_file)

# Create the web app
st.title('House Price Prediction App')

# Input fields
area = st.number_input('Area (sq ft)', min_value=100.0, value=1000.0, step=10.0)

bedrooms = st.number_input('Bedrooms', min_value=1, value=2, step=1)

bathrooms = st.number_input('Bathrooms', min_value=1, value=2, step=1)

stories = st.number_input('Stories', min_value=1, value=1, step=1)

parking = st.number_input('Parking', min_value=0, value=1, step=1)

# Button to trigger prediction
if st.button('Predict House Price'):

    # Create input dataframe
    input_data = pd.DataFrame({
        'Area': [area],
        'Bedrooms': [bedrooms],
        'Bathrooms': [bathrooms],
        'Stories': [stories],
        'Parking': [parking]
    })

    # Add missing columns
    for col in columns:
        if col not in input_data.columns:
            input_data[col] = 0

    # Reorder columns
    input_data = input_data[columns]

    # Predict price
    predicted_price = model.predict(input_data)

    # Display prediction
    st.success(f'Predicted House Price: Rs. {predicted_price[0]:,.2f}')
