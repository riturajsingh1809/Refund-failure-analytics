
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Refund & Failure Analytics Dashboard", layout="wide")

st.title("Refund & Failure Analytics Dashboard")

df = pd.read_excel("Cleaned_Refund_Dataset.xlsx")

total_receipts = len(df)
total_amount = df["Amount"].sum()
successful = (df["Payment_Status"]=="Success").sum()
failed = (df["Payment_Status"]=="Failed").sum()
refunds = (df["Refund_Status"]=="Refunded").sum()
refund_amount = df["Refund_Amount"].sum()

col1,col2,col3 = st.columns(3)

col1.metric("Total Receipts", total_receipts)
col2.metric("Total Revenue", f"₹{total_amount}")
col3.metric("Successful Payments", successful)

col1,col2,col3 = st.columns(3)

col1.metric("Failed Payments", failed)
col2.metric("Refund Count", refunds)
col3.metric("Refund Amount", f"₹{refund_amount}")

st.subheader("Dataset Preview")
st.dataframe(df)
