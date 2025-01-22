import React, { useState } from 'react';
import ModeStandbyIcon from '@mui/icons-material/ModeStandby';
import Button from '@mui/material/Button';
import SendIcon from '@mui/icons-material/Send';
import RebalancingInformationModalContent from './RebalancingInformationModalContent';
import Modal from '@mui/material/Modal';
import Typography from '@mui/material/Typography';
  
export default function RebalancingSection() {
    const [rebalancingInformationModalOpened, setRebalancingInformationModalOpened] = useState(false);

    return (
        <>
            <Button endIcon={<ModeStandbyIcon />} onClick={() => setRebalancingInformationModalOpened(true)}>
                <Typography>REBALANCING INFORMATION</Typography>
            </Button>
            <Button endIcon={<SendIcon />}>
                <Typography>REBALANCE</Typography>
            </Button>
            {rebalancingInformationModalOpened && (
                <Modal open={rebalancingInformationModalOpened} onClose={() => setRebalancingInformationModalOpened(false)}> 
                    <RebalancingInformationModalContent /> 
                </Modal>
            )}
        </>
    );
}
