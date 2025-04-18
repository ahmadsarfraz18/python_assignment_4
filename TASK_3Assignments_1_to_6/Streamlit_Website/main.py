import streamlit as st
import pandas as pd  # correction: 'pandas as pandas' ko 'pandas as pd' hona chahiye
import matplotlib.pyplot as plt

# Title of the app
st.title("📊 Simple Data Dashboard App")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)

    # Show data preview
    st.subheader("🔍 Data Preview")
    st.write(df)

    # Show basic statistics
    st.subheader("📈 Data Description")
    st.write(df.describe())

    # Column selection for visualization
    st.subheader("📊 Plot a Column")
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if numeric_columns:
        column_to_plot = st.selectbox("Select a numeric column to plot", numeric_columns)
        plt.figure(figsize=(10, 5))
        plt.hist(df[column_to_plot], bins=20, color='skyblue', edgecolor='black')
        plt.title(f"Histogram of {column_to_plot}")
        plt.xlabel(column_to_plot)
        plt.ylabel("Frequency")
        st.pyplot(plt)
    else:
        st.warning("No numeric columns available to plot.")
else:
    st.info("Please upload a CSV file to get started.")
