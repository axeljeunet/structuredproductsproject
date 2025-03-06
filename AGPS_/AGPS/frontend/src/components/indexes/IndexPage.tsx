import { Button, Typography } from '@mui/material';
import React from 'react';
import { useNavigate } from 'react-router';
import { useIndexesInformationQuery } from '../../utils/queries';
  
export default function IndexPage() {
    const navigate = useNavigate()
    const storedDate = localStorage.getItem("currentDate");
    const date = storedDate ? new Date(storedDate) : new Date();
    const { isLoading, error, data } = useIndexesInformationQuery( { date } );

    if (isLoading) { return <p className="loading-message">Loading...</p> }

    if (error) { 
        const errorMessage = (error as { message?: string })?.message || 'An unknown error occurred';
        return <p className="error-message">{errorMessage}</p>;
    }

    return (
        <Button onClick={() => navigate("/") } >
          <Typography>Go back to portfolio page</Typography>
        </Button>
    );
}
