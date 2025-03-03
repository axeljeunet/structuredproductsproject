import React, { useState } from 'react';
import './App.css';
import PortfolioCompositionSection from './components/portfolio_composition/PortfolioCompositionSection';
import RebalancingSection from './components/rebalancing/RebalancingSection';
import PortfolioGlobalInformationsSection from './components/portfolio_global/PortfolioGlobalInformationsSection';
import Box from '@mui/material/Box';
import PortfolioInformationProvider from './components/PortfolioInformationProvider';
import DateInformation from './components/DateInformation';

const INITAL_DATE = '05/07/2000';

function App() {
  const [date, setDate] = useState(new Date(INITAL_DATE))

  return (
    <Box className="App" sx={{ display: "flex", flexDirection: "column", gap: 2 }}>
        <DateInformation date={date} setDate={setDate} />
        <PortfolioInformationProvider date={date}>
          <PortfolioCompositionSection />
          <RebalancingSection />
          <PortfolioGlobalInformationsSection />
        </PortfolioInformationProvider>
    </Box>
  );
}

export default App;