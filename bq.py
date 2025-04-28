import streamlit as st
from google.cloud import bigquery
import pandas as pd

# Title
st.title("BigQuery + Streamlit Demo")

# Set your GCP project ID
project_id = "ab-dev-410613"

# Create BigQuery client
client = bigquery.Client(project=project_id)

st.write(client)
