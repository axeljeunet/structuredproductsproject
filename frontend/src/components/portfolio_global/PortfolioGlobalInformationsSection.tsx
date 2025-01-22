import React from 'react';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import PortfolioFlows from './PortfolioFlows';
  
export default function PortfolioGlobalInformationsSection() {
    return (
        <>
            <Box component="section">
                <Typography> P&L: {1+1} % </Typography>
            </Box>
            <Box component="section">
                <Typography> Value of portfolio: {1+1} €</Typography>
            </Box>
            <Box component="section">
                <Typography> Liquidative value: {1+1} €</Typography>
            </Box>

            <PortfolioFlows />
        </>
    );
}
