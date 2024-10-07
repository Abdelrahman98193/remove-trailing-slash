import pandas as pd
import streamlit as st

# Function to remove the trailing slash from URLs
def remove_trailing_slash(url):
    if url.endswith('/'):
        return url[:-1]  # Remove the last character if it is a slash
    return url  # Return the original URL if no trailing slash

# Streamlit file uploader
st.title("Remove Trailing Slashes from URLs")
uploaded_file = st.file_uploader("Please upload the CSV file containing URLs.", type="csv")

# Check if a file is uploaded
if uploaded_file is not None:
    try:
        # Reading the CSV file
        df = pd.read_csv(uploaded_file)

        # Check if the CSV has a column named 'URLs'
        if 'URLs' in df.columns:
            # Applying the function to remove trailing slashes
            df['Cleaned URLs'] = df['URLs'].apply(remove_trailing_slash)

            # Display the cleaned URLs
            st.write("Cleaned URLs:")
            st.write(df)

            # Allow user to download the cleaned URLs as a CSV
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Cleaned URLs as CSV",
                data=csv,
                file_name='cleaned_urls.csv',
                mime='text/csv',
            )
        else:
            st.error("Error: The CSV file must contain a column named 'URLs'.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
