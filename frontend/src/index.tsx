import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { QueryClientProvider } from '@tanstack/react-query';
import { QUERY_CLIENT } from './utils/queries';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
      <QueryClientProvider client={QUERY_CLIENT}>
        <App />
      </QueryClientProvider>
  </React.StrictMode>
);
