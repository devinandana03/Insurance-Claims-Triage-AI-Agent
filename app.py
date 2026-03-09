import streamlit as st
import pandas as pd
import joblib

from rag.rag_engine import load_docs,build_index,retrieve
from utils.claim_parser import parse_claim
from utils.groq_llm import call_llm

docs = load_docs()

index,_ = build_index(docs)

model = joblib.load("fraud/fraud_model.pkl")

st.title("Insurance Claims Triage AI")

st.subheader("Enter Claim Details")

claim_amount = st.number_input("Claim Amount")
delay_days = st.number_input("Delay Days")
previous_claims = st.number_input("Previous Claims")

if st.button("Analyze Claim"):

    claim = {
        "claim_amount":claim_amount,
        "delay_days":delay_days,
        "previous_claims":previous_claims
    }

    x = [[claim_amount,delay_days,previous_claims]]

    fraud_prob = model.predict_proba(x)[0][1]

    retrieved = retrieve("insurance claim rules",docs,index)

    context = "\n".join(retrieved)

    prompt = f"""
Context:
{context}

Claim Data:
{claim}

Fraud Probability: {fraud_prob}

Generate:
1 Claims triage summary
2 Fraud risk report
3 IFRS17 financial note
"""

    response = call_llm(prompt)

    st.subheader("Fraud Score")
    st.write(fraud_prob)

    st.subheader("AI Analysis")

    st.write(response)