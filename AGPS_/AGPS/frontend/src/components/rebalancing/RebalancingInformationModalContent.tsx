import React, { forwardRef } from 'react';
import RebalancingInformationModalContentTable from './RebalancingInformationModalContentTable';
import Typography from '@mui/material/Typography';

interface RebalancingInformationModalContentProps {
    date: Date;
  }

const RebalancingInformationModalContent = forwardRef<HTMLDivElement, RebalancingInformationModalContentProps>(({ date }, ref) => {
  return (
    <div ref={ref}>
      <Typography variant="h6" sx={{ backgroundColor: '#6CB4EE' }}>
        Rebalancing information for risked assets
      </Typography>
      <RebalancingInformationModalContentTable date={date} />
    </div>
  );
});

export default RebalancingInformationModalContent;
