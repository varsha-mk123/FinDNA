import React from 'react';

interface HealthScoreProps {
  healthScore: {
    score: number;
    factors: { [key: string]: number };
  } | null;
}

const HealthScoreCard: React.FC<HealthScoreProps> = ({ healthScore }) => {
  if (!healthScore) {
    return <div>Loading...</div>;
  }

  return (
    <div className="bg-white p-6 rounded-lg shadow">
      <h3 className="text-lg font-medium mb-4">Financial Health Score</h3>
      <div className="text-4xl font-bold text-center mb-4">{healthScore.score}</div>
      <div className="space-y-2">
        {Object.entries(healthScore.factors).map(([factor, score]) => (
          <div key={factor} className="flex justify-between">
            <span className="capitalize">{factor.replace('_', ' ')}</span>
            <span>{score}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default HealthScoreCard;