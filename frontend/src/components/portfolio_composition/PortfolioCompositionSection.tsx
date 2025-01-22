import React from 'react';
import PortfolioCompositionTable from './PortfolioCompositionTable';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
  
export default function PortfolioCompositionSection() {
return (
    <Box>
        <Typography variant="h6" sx={{backgroundColor: '#6CB4EE'}} textAlign="left"> Portfolio composition </Typography>
        <PortfolioCompositionTable />
    </Box>
);
}
