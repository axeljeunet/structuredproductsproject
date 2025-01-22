import React from 'react';
import PortfolioCompositionTable from './PortfolioCompositionTable';
import Typography from '@mui/material/Typography';
  
export default function PortfolioCompositionSection() {
return (
    <>
        <Typography variant="h2"> Portfolio composition </Typography>
        <PortfolioCompositionTable />
    </>
);
}
