
from sdk.python.trust_score import TrustApiClient

# Point to your running Django API
client = TrustApiClient(base_url="http://127.0.0.1:8000")

# Call the API (replace with a real user ID from your DB)
score = client.get_trust_score(user_id="1")

print("Trust score:", score)
