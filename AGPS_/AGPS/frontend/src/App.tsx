import React, { useState } from 'react';
import './App.css';
import PortfolioCompositionSection from './components/portfolio_composition/PortfolioCompositionSection';
import RebalancingSection from './components/rebalancing/RebalancingSection';
import PortfolioGlobalInformationsSection from './components/portfolio_global/PortfolioGlobalInformationsSection';
import Box from '@mui/material/Box';
import { DateTimePicker } from '@mui/x-date-pickers/DateTimePicker';
import PortfolioInformationProvider from './components/PortfolioInformationProvider';

const INITAL_DATE = '05/07/2000';

function App() {
  const [date, setDate] = useState(new Date(INITAL_DATE))
  return (
    <Box className="App" sx={{ display: "flex", flexDirection: "column", gap: 2 }}>
        <DateTimePicker
          label="Choose a day"
          value={date}
          views={['year', 'month', 'day']}
          onChange={(newValue) => newValue && setDate(newValue)}
        />
        <PortfolioInformationProvider date={date}>
          <PortfolioCompositionSection />
          <RebalancingSection />
          <PortfolioGlobalInformationsSection />
        </PortfolioInformationProvider>
    </Box>
  );
}

export default App;