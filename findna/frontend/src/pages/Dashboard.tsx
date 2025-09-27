import React, { useEffect, useState } from 'react';
import HealthScoreCard from '../components/dashboard/HealthScoreCard';
import FinancialOverview from '../components/dashboard/FinancialOverview';

interface HealthScore {
  score: number;
  factors: { [key: string]: number };
}

interface FinancialRatio {
  ratio_name: string;
  ratio_value: number;
}

const Dashboard: React.FC = () => {
  const [healthScore, setHealthScore] = useState<HealthScore | null>(null);
  const [ratios, setRatios] = useState<FinancialRatio[]>([]);

  useEffect(() => {
    // Mock data for now
    setHealthScore({
      score: 75,
      factors: {
        current_ratio: 80,
        debt_to_equity: 70,
        roa: 75
      }
    });
    setRatios([
      { ratio_name: 'current_ratio', ratio_value: 2.0 },
      { ratio_name: 'debt_to_equity', ratio_value: 0.5 },
      { ratio_name: 'roa', ratio_value: 0.1 }
    ]);
  }, []);

  return (
    <div>
      <h2 className="text-2xl font-semibold mb-6">Dashboard</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <HealthScoreCard healthScore={healthScore} />
        <FinancialOverview ratios={ratios} />
      </div>
    </div>
  );
};

export default Dashboard;