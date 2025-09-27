from typing import Dict

class HealthScorer:
    def __init__(self):
        self.weights = {
            'current_ratio': 0.2,
            'debt_to_equity': 0.3,
            'roa': 0.5
        }
        self.ideal_ranges = {
            'current_ratio': (1.5, 2.5),
            'debt_to_equity': (0.1, 0.6),
            'roa': (0.05, 0.2)
        }

    def calculate_score(self, ratios: Dict[str, float]) -> Dict:
        score = 0
        factors = {}
        
        for ratio_name, value in ratios.items():
            if ratio_name in self.ideal_ranges:
                low, high = self.ideal_ranges[ratio_name]
                if value >= low and value <= high:
                    factor_score = 100
                else:
                    # Penalize based on deviation
                    if value < low:
                        deviation = (low - value) / low
                    else:
                        deviation = (value - high) / high
                    factor_score = max(0, 100 - (deviation * 100))
                
                factors[ratio_name] = factor_score
                score += factor_score * self.weights[ratio_name]
        
        return {
            "score": round(score, 2),
            "factors": factors
        }