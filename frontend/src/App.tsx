import React from 'react';
import './App.css';
import PortfolioCompositionSection from './components/portfolio_composition/PortfolioCompositionSection';
import RebalancingSection from './components/rebalancing/RebalancingSection';
import PortfolioGlobalInformationsSection from './components/portfolio_global/PortfolioGlobalInformationsSection';


function App() {
  return (
    <div className="App">
        <PortfolioCompositionSection />
        <RebalancingSection />
        <PortfolioGlobalInformationsSection />
    </div>
  );
}

export default App;