from typing import Dict

class TrustScorer:
    def __init__(self, weights: Dict[str, float] = None):
        self.weights = weights or {
            'social': 0.3, 
            'blockchain': 0.2, 
            'transaction': 0.5
        }

    def score(self, signals: Dict[str, float]) -> float:
        total = sum(signals.get(k, 0) * w for k, w in self.weights.items())
        return round(total, 2)
    
    def explain(self, signals: Dict[str, float]) -> Dict[str, float]:
        return {k: round(signals.get(k, 0) * w, 2) for k, w in self.weights.items()}
        