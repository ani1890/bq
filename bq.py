import streamlit as st
from google.cloud import bigquery
import pandas as pd

# Title
st.title("BigQuery + Streamlit Demo")

# Set your GCP project ID
project_id = "ab-dev-410613"

# Create BigQuery client
client = bigquery.Client(project=project_id)

# Query BigQuery
query = """
    SELECT employee_id, name, age, department
    FROM `your-project-id.my_dataset.employees`
    LIMIT 10
"""

st.write("Running Query...")
query_job = client.query(query)

# Get the results
df = query_job.to_dataframe()

# Display results
st.subheader("Query Results")
st.dataframe(df)

# Optionally: Plot
if not df.empty:
    st.bar_chart(df.set_index("name")["age"])
