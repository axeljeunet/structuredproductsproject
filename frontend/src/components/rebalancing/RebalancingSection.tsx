import React, { useState } from 'react';
import ModeStandbyIcon from '@mui/icons-material/ModeStandby';
import Button from '@mui/material/Button';
import SendIcon from '@mui/icons-material/Send';
import RebalancingInformationModalContent from './RebalancingInformationModalContent';
import Modal from '@mui/material/Modal';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
  
export default function RebalancingSection() {
    const [rebalancingInformationModalOpened, setRebalancingInformationModalOpened] = useState(false);

    return (
        <Box sx={{ display: "flex", flexDirection: "row", gap: 2, justifyContent: 'center' }}>
            <Button endIcon={<ModeStandbyIcon sx={{color: "white"}}/>} onClick={() => setRebalancingInformationModalOpened(true)} sx={{backgroundColor: "#7C0A02"}}>
                <Typography color='white'>REBALANCING INFORMATION</Typography>
            </Button>
            <Button endIcon={<SendIcon sx={{color: "white"}} />} sx={{backgroundColor: "purple"}}>
                <Typography sx={{color: "white"}}>REBALANCE</Typography>
            </Button>
            {rebalancingInformationModalOpened && (
                <Modal open={rebalancingInformationModalOpened} onClose={() => setRebalancingInformationModalOpened(false)}> 
                    <RebalancingInformationModalContent /> 
                </Modal>
            )}
        </Box>
    );
}
