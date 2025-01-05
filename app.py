import streamlit as st
import pandas as pd
import numpy as np

# Load mock data
data = pd.read_csv("mock_data.csv")

st.title("Psychometric-Enhanced Real-Time Credit Scoring")  
st.markdown("### Demonstration of Credit Scoring Pipeline")  

# Sidebar filters
st.sidebar.header("Filter Users")
income_filter = st.sidebar.slider("Income Range:", int(data['net_yearly_income'].min()), int(data['net_yearly_income'].max()), (50000, 100000))

sentiment_filter = st.sidebar.slider("Sentiment Score:", 0.0, 1.0, (0.4, 0.8))

# Filter data
filtered_data = data[
    (data['Income'] >= income_filter[0]) &
    (data['Income'] <= income_filter[1]) &
    (data['Sentiment_Score'] >= sentiment_filter[0]) &
    (data['Sentiment_Score'] <= sentiment_filter[1])
]

# Display data
st.markdown("### Filtered Data")
st.write(filtered_data)

# Visualize scoring
st.markdown("### Credit Score Distribution")
st.bar_chart(filtered_data['Final_Score'])

# Explanation section
st.markdown("### Feature Contribution Explanation")
st.write("Mock explanation for feature contributions to credit scoring (replace with DALEx or similar visualization).")
