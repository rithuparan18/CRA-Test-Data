import streamlit as st
import pandas as pd
import numpy as np

# Load mock data
data = pd.read_csv("mock_data.csv")

st.title("Psychometric-Enhanced Real-Time Credit Scoring")  
st.markdown("### Demonstration of Credit Scoring Pipeline")  

# Sidebar filters
st.sidebar.header("Filter Users")

# Handle 'net_yearly_income' filter
if 'net_yearly_income' in data.columns:
    income_filter = st.sidebar.slider(
        "Income Range:",
        int(data['net_yearly_income'].min()),
        int(data['net_yearly_income'].max()),
        (50000, 100000)
    )
else:
    st.error("'net_yearly_income' column is missing in the dataset.")
    st.stop()

# Optional: Check if 'Sentiment_Score' exists
sentiment_filter_applied = False
if 'Sentiment_Score' in data.columns:
    sentiment_filter = st.sidebar.slider("Sentiment Score:", 0.0, 1.0, (0.4, 0.8))
    data = data[
        (data['Sentiment_Score'] >= sentiment_filter[0]) &
        (data['Sentiment_Score'] <= sentiment_filter[1])
    ]
    sentiment_filter_applied = True

# Filter data for income
filtered_data = data[
    (data['net_yearly_income'] >= income_filter[0]) &
    (data['net_yearly_income'] <= income_filter[1])
]

# Display data
st.markdown("### Filtered Data")
st.write(filtered_data)

# Visualize scoring
if 'Final_Score' in filtered_data.columns:
    st.markdown("### Credit Score Distribution")
    st.bar_chart(filtered_data['Final_Score'])
else:
    st.warning("The 'Final_Score' column is missing in the data.")

# Explanation section
st.markdown("### Feature Contribution Explanation")
if sentiment_filter_applied:
    st.write("Mock explanation for feature contributions to credit scoring with sentiment analysis.")
else:
    st.write("Mock explanation for feature contributions to credit scoring without sentiment analysis.")
