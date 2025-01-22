import React from 'react';
import './App.css';
import PortfolioCompositionSection from './components/portfolio_composition/PortfolioCompositionSection';
import RebalancingSection from './components/rebalancing/RebalancingSection';


function App() {
  return (
    <div className="App">
        <PortfolioCompositionSection />
        <RebalancingSection />
    </div>
  );
}

export default App;