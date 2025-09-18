def normalize_score(platform: str, value: float) -> float:
    """
    Normalizes scores from different sources into a 0–1 range.
    """
    ranges = {
        'social': (0, 1000),    # Example range for social media likes
        'blockchain': (0, 100),  # Example range for blockchain transactions    
        'transaction': (0, 500), # Example range for financial transactions
    }
    min_val, max_val = ranges.get(platform, (0, 1))
    return min(1.0, max(0.0, (value - min_val) / (max_val - min_val)))