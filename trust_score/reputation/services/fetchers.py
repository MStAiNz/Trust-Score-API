import requests
import random

def fetch_social_data(user_id: int) -> float:
    # Example: call Twitter/Reddit API → likes/followers
    
    # Here we just return a random score for demonstration purposes
    return random.randint(0, 1000)

def fetch_blockchain_data(user_id: int) -> float:   
    # Example: call blockchain explorer → number of transactions, balance
    
    return random.randint(0, 100)

def fetch_transaction_data(user_id: int) -> float:
    # Example: fetch number of transactions, amounts, reviews from payment processors
    
    return random.randint(0, 500)