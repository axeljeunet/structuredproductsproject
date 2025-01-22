import React from 'react';
import { BarChart } from '@mui/x-charts/BarChart';
import Typography from '@mui/material/Typography';

// TODO Change with real data
  
export default function PortfolioFlows() {
    return (
        <>
            <Typography variant="h6">
                Flows until now (in €)
            </Typography>
            <BarChart
                    series={[
                        { data: [35, 44, 24, 34] },
                    ]}
                    height={290}
                    xAxis={[{ data: ['Q1', 'Q2', 'Q3', 'Q4'], scaleType: 'band' }]}
                    margin={{ top: 10, bottom: 30, left: 40, right: 10 }} 
            />
        </>
    );
}
