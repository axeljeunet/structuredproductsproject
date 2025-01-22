import React from 'react';
import RebalancingInformationModalContentTable from './RebalancingInformationModalContentTable';
import Typography from '@mui/material/Typography';

  
export default function RebalancingInformationModalContent() {
return (
    <>
        <Typography variant="h2">Rebalancing information for risked assets</Typography>
        <RebalancingInformationModalContentTable />
    </>
    );
}
