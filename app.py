import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Norway Traffic Fines Dashboard", page_icon="🚨", layout="wide")

data = [
    ("Speeding", "60-zone", 15, 2023, 4500),
    ("Speeding", "60-zone", 15, 2024, 5200),
    ("Speeding", "60-zone", 15, 2025, 5650),
    ("Speeding", "60-zone", 15, 2026, 5800),

    ("Speeding", "70-zone", 20, 2023, 6000),
    ("Speeding", "70-zone", 20, 2024, 6700),
    ("Speeding", "70-zone", 20, 2025, 7050),
    ("Speeding", "70-zone", 20, 2026, 7250),

    ("Speeding", "90-zone", 40, 2023, 13000),
    ("Speeding", "90-zone", 40, 2024, 15000),
    ("Speeding", "90-zone", 40, 2025, 15850),
    ("Speeding", "90-zone", 40, 2026, 16250),

    ("Mobile phone use", "All", 0, 2023, 9000),
    ("Mobile phone use", "All", 0, 2024, 9500),
    ("Mobile phone use", "All", 0, 2025, 10450),
    ("Mobile phone use", "All", 0, 2026, 10750),

    ("Red-light running", "All", 0, 2023, 9000),
    ("Red-light running", "All", 0, 2024, 9500),
    ("Red-light running", "All", 0, 2025, 10450),
    ("Red-light running", "All", 0, 2026, 10750),
]

df = pd.DataFrame(data, columns=["Category", "Zone", "Over_km", "Year", "Fine_NOK"])

st.title("🚨 Norway Traffic Fines – Scenario Dashboard")
st.write("Visualizing official 2025 fine levels and 2026 scenario.")

st.subheader("Dataset Preview")
st.dataframe(df)

filtered = df[df["Category"] == "Speeding"]
fig = px.line(filtered, x="Year", y="Fine_NOK", color="Zone", markers=True)
st.plotly_chart(fig)
