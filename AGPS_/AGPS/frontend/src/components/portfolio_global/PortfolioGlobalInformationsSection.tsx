import React from 'react';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import PortfolioFlows from './PortfolioFlows';
  
export default function PortfolioGlobalInformationsSection() {
    return (
        <Box display="flex" flexDirection="row">
            <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                <Box component="section" borderRadius={2} sx={{ backgroundColor: '#7FFFD4', flexGrow: 1 }}>
                    <Typography> P&L: {1+1} % </Typography>
                </Box>
                <Box component="section" borderRadius={2} sx={{ backgroundColor: '#6CB4EE', flexGrow: 1 }}>
                    <Typography> Value of portfolio: {1+1} €</Typography>
                </Box>
                <Box component="section" borderRadius={2} sx={{ backgroundColor: '#007FFF', flexGrow: 1 }}>
                    <Typography> Liquidative value: {1+1} €</Typography>
                </Box>
            </Box>

            <PortfolioFlows />
        </Box>
    );
}
