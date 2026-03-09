def parse_claim(data):

    claim_amount = data["claim_amount"]
    delay_days = data["delay_days"]
    previous_claims = data["previous_claims"]

    return claim_amount,delay_days,previous_claims