import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import { QueryClientProvider } from '@tanstack/react-query';
import { QUERY_CLIENT } from './utils/queries';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns';
import AppRouterProvider from './AppRouterProvider';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
      <QueryClientProvider client={QUERY_CLIENT}>
        <LocalizationProvider dateAdapter={AdapterDateFns}>
          <AppRouterProvider />
        </LocalizationProvider>
      </QueryClientProvider>
  </React.StrictMode>
);
