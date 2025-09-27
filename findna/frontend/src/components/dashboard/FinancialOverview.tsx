import React from 'react';

interface FinancialRatio {
  ratio_name: string;
  ratio_value: number;
}

interface FinancialOverviewProps {
  ratios: FinancialRatio[];
}

const FinancialOverview: React.FC<FinancialOverviewProps> = ({ ratios }) => {
  return (
    <div className="bg-white p-6 rounded-lg shadow">
      <h3 className="text-lg font-medium mb-4">Key Financial Ratios</h3>
      <div className="space-y-3">
        {ratios.map((ratio) => (
          <div key={ratio.ratio_name} className="flex justify-between">
            <span className="capitalize">{ratio.ratio_name.replace('_', ' ')}</span>
            <span>{ratio.ratio_value.toFixed(2)}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default FinancialOverview;