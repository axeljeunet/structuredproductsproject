import React from 'react';
import './App.css';
import PortfolioCompositionSection from './components/portfolio_composition/PortfolioCompositionSection';
import RebalancingSection from './components/rebalancing/RebalancingSection';
import PortfolioGlobalInformationsSection from './components/portfolio_global/PortfolioGlobalInformationsSection';
import Box from '@mui/material/Box';


function App() {
  return (
    <Box className="App" sx={{ display: "flex", flexDirection: "column", gap: 2 }}>
        <PortfolioCompositionSection />
        <RebalancingSection />
        <PortfolioGlobalInformationsSection />
    </Box>
  );
}

export default App;