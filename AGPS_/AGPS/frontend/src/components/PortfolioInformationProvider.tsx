import React from 'react';

import { usePortfolioInformationQuery } from '../utils/queries'

  
export default function PortfolioInformationProvider({ date, children }) {
    const { isLoading, error, data } = usePortfolioInformationQuery({ date })

    if (isLoading) { return <p className="loading-message">Loading...</p> }

    if (error) { 
        const errorMessage = (error as { message?: string })?.message || 'An unknown error occurred';
        return <p className="error-message">{errorMessage}</p>;
    }

    return (
        <>
            {React.Children.map(children, (child) =>
                React.cloneElement(child, { portfolioData: data })
            )}
        </>
    );
}
