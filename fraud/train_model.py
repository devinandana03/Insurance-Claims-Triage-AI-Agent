import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("data/claims_dataset.csv")

X = df[["claim_amount","delay_days","previous_claims"]]
y = df["fraud"]

model = RandomForestClassifier()

model.fit(X,y)

joblib.dump(model,"fraud/fraud_model.pkl")

print("model trained")