import React, { useState } from 'react';
import './App.css';
import PortfolioCompositionSection from './components/portfolio_composition/PortfolioCompositionSection';
import RebalancingSection from './components/rebalancing/RebalancingSection';
import PortfolioGlobalInformationsSection from './components/portfolio_global/PortfolioGlobalInformationsSection';
import Box from '@mui/material/Box';
import PortfolioInformationProvider from './components/PortfolioInformationProvider';
import DateInformation from './components/DateInformation';

const INITAL_YEAR = 2009;
const INITAL_MONTH_INDEX = 0
const INITAL_DAY = 5

function App() {
  const [date, setDate] = useState(new Date(Date.UTC(INITAL_YEAR, INITAL_MONTH_INDEX, INITAL_DAY)))

  const handleDateChange = (newValue) => {
    if (newValue) {
      setDate(new Date(Date.UTC(newValue.getUTCFullYear(), newValue.getUTCMonth(), newValue.getUTCDate())));
    }
  }

  return (
    <Box className="App" sx={{ display: "flex", flexDirection: "column", gap: 2 }}>
        <DateInformation date={date} setDate={handleDateChange} />
        <PortfolioInformationProvider date={date}>
          <PortfolioCompositionSection />
          <RebalancingSection date={date} />
          <PortfolioGlobalInformationsSection />
        </PortfolioInformationProvider>
    </Box>
  );
}

export default App;