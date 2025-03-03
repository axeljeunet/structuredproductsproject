import React, { forwardRef } from 'react';
import Typography from '@mui/material/Typography';
import SendIcon from '@mui/icons-material/Send';
import { Button } from '@mui/material';
import { useRebalanceMutation } from "../../utils/mutations"

export default function RebalanceButton( {date} ) {

  const { isPending, error, mutate } = useRebalanceMutation( {date} );
  if (isPending) { return <p className="loading-message">Loading...</p> }

  if (error) { 
      const errorMessage = (error as { message?: string })?.message || 'An unknown error occurred';
      return <p className="error-message">{errorMessage}</p>;
  }

  return (
    <Button onClick={mutate} endIcon={<SendIcon sx={{color: "white"}} />} sx={{backgroundColor: "purple"}}>
        <Typography sx={{color: "white"}}>REBALANCE</Typography>
    </Button>
  );
};
