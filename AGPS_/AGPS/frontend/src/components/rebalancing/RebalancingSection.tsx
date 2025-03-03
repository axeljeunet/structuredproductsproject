import React, { useState } from 'react';
import ModeStandbyIcon from '@mui/icons-material/ModeStandby';
import Button from '@mui/material/Button';
import RebalancingInformationModalContent from './RebalancingInformationModalContent';
import Modal from '@mui/material/Modal';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import RebalanceButton from './RebalanceButton';
  
export default function RebalancingSection( {date} ) {
    const [rebalancingInformationModalOpened, setRebalancingInformationModalOpened] = useState(false);

    return (
        <Box sx={{ display: "flex", flexDirection: "row", gap: 2, justifyContent: 'center' }}>
            <Button endIcon={<ModeStandbyIcon sx={{color: "white"}}/>} onClick={() => setRebalancingInformationModalOpened(true)} sx={{backgroundColor: "#7C0A02"}}>
                <Typography color='white'>REBALANCING INFORMATION</Typography>
            </Button>
            <RebalanceButton date={date}/>
            {rebalancingInformationModalOpened && (
                <Modal open={rebalancingInformationModalOpened} onClose={() => setRebalancingInformationModalOpened(false)}> 
                    <RebalancingInformationModalContent date={date} /> 
                </Modal>
            )}
        </Box>
    );
}
