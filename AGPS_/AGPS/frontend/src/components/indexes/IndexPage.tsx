import { Button, Typography } from '@mui/material';
import React from 'react';
import { useNavigate } from 'react-router';
  
export default function IndexPage() {
    const navigate = useNavigate()

    return (
        <Button onClick={() => navigate("/") } >
          <Typography>Go back to portfolio page</Typography>
        </Button>
    );
}
