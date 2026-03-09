import pandas as pd
import random

data = []

for i in range(500):

    claim_amount = random.randint(1000,50000)
    delay_days = random.randint(0,60)
    previous_claims = random.randint(0,5)

    fraud = 1 if (claim_amount > 30000 and delay_days > 20) else 0

    data.append({
        "claim_id":i,
        "claim_amount":claim_amount,
        "delay_days":delay_days,
        "previous_claims":previous_claims,
        "fraud":fraud
    })

df = pd.DataFrame(data)

df.to_csv("data/claims_dataset.csv",index=False)

print("dataset generated")