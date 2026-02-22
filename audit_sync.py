import json

# This creates the data for your website's front-end
audit_data = {
    "account_type": "Institutional/Corporate",
    "verification_status": "L2_Ratification_Pending",
    "inventory": {
        "asset": "Moonitor NFT",
        "series_collection": 5,
        "units_per_series": 6000,
        "total_holdings": 30000
    },
    "settlement_ref": "0xcc51f2662e47ac26308e1d5858fca3f7a28fc3f6dce017d2e9019f76927ed74e",
    "legal_framework": "Listing Services Agreement / MIP65"
}

with open('audit_data.json', 'w') as f:
    json.dump(audit_data, f, indent=4)

print("SUCCESS: audit_data.json updated for Vercel.")
