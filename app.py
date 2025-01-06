import pandas as pd
import streamlit as st

# Load the primary and alternate datasets
primary_file_path = "test.csv"  # Update this to your actual primary dataset path
alternate_file_path = "Alternate.csv"  # Update this to your actual alternate dataset path

# Load datasets
data = pd.read_csv(primary_file_path)
alternate_data = pd.read_csv(alternate_file_path)

# Merge datasets using the 'id' column
combined_data = pd.merge(data, alternate_data, on='id', how='inner')

# Display previews of the datasets
st.title("Enhanced Real-Time Credit Scoring App")
st.sidebar.title("Filters")

# Display merged dataset
st.write("### Combined Data Preview:")
st.write(combined_data.head())

# Feature Engineering
# Normalize 'notability' if numeric
if pd.api.types.is_numeric_dtype(combined_data['notability']):
    combined_data['notability_normalized'] = (combined_data['notability'] - combined_data['notability'].min()) / (
        combined_data['notability'].max() - combined_data['notability'].min()
    )
else:
    # Encode if 'notability' is categorical
    combined_data['notability_encoded'] = pd.factorize(combined_data['notability'])[0]

# Extend scoring algorithm
combined_data['risk_score'] = (
    0.4 * combined_data['credit_score_normalized'] +
    0.3 * combined_data['debt_to_income_ratio'] +
    0.2 * combined_data.get('notability_normalized', 0) +
    0.1 * combined_data.get('additional_features_score', 0)  # Placeholder for further enhancements
)

# Visualization
st.write("### Risk Score Distribution")
st.bar_chart(combined_data['risk_score'])

# Filters for exploration
income_filter = st.sidebar.slider(
    "Income Range:", int(combined_data['Income'].min()), int(combined_data['Income'].max()), (50000, 100000)
)
sentiment_filter = st.sidebar.slider(
    "Social Media Sentiment:", float(combined_data['social_media_sentiment'].min()), float(combined_data['social_media_sentiment'].max()), (0.2, 0.8)
)

filtered_data = combined_data[
    (combined_data['Income'] >= income_filter[0]) &
    (combined_data['Income'] <= income_filter[1]) &
    (combined_data['social_media_sentiment'] >= sentiment_filter[0]) &
    (combined_data['social_media_sentiment'] <= sentiment_filter[1])
]

st.write("### Filtered Data:")
st.write(filtered_data)

# Download link for updated data
@st.cache
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

data_csv = convert_df(combined_data)
st.download_button(
    label="Download Enhanced Dataset",
    data=data_csv,
    file_name="enhanced_credit_data.csv",
    mime="text/csv",
)
