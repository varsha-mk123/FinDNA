import pandas as pd
from sklearn.linear_model import LinearRegression
from typing import List

class CashFlowForecaster:
    def __init__(self):
        self.model = LinearRegression()

    def forecast(self, historical_data: List[float], periods: int = 6) -> List[float]:
        if len(historical_data) < 2:
            return [historical_data[0]] * periods if historical_data else [0] * periods
        
        X = [[i] for i in range(len(historical_data))]
        y = historical_data
        self.model.fit(X, y)
        
        future_X = [[i] for i in range(len(historical_data), len(historical_data) + periods)]
        return self.model.predict(future_X).tolist()