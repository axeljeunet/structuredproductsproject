import React from 'react';
import { DateTimePicker } from '@mui/x-date-pickers/DateTimePicker';
import { Box, Button, Typography } from '@mui/material';
  
export default function DateInformation({ date, setDate }) {

    const incrementDate = () => {
        const newDate = new Date(date);
        newDate.setDate(newDate.getDate() + 1);
        setDate(newDate);
      };

    return (
        <Box className="DateInformation" sx={{ display: "flex", flexDirection: "row", gap: 2 }}>
            <Button onClick={incrementDate}>
            <Typography>DAY +1</Typography>
            </Button>
            <DateTimePicker
                label="Choose a day"
                value={date}
                views={['year', 'month', 'day']}
                onChange={(newValue) => newValue && setDate(newValue)}
            />
        </Box>
    );
}
