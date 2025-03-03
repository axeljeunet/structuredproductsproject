import { QueryClient, useQuery } from '@tanstack/react-query';
import getAPIUrl from './url';

const QUERY_CLIENT = new QueryClient();

function usePortfolioInformationQuery({ date }) {
    return useQuery({
        queryKey: ['information', { date }],
        queryFn: async () => {
            const res = await fetch(getAPIUrl("information"), {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ date: date.toISOString() })
            });

            const resJson = await res.json();

            if(!res.ok) {
                throw new Error(resJson.message);
            }

            return resJson;
        }
    });
}

function usePortfolioRebalancingInformationQuery({ date }) {
    return useQuery({
        queryKey: ['rebalancingInformation', { date }],
        queryFn: async () => {
            const res = await fetch(getAPIUrl("rebalancingInformation"), {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ date: date.toISOString() })
            });

            const resJson = await res.json();

            if(!res.ok) {
                throw new Error(resJson.message);
            }

            return resJson;
        }
    });
}

export {
    usePortfolioInformationQuery,
    usePortfolioRebalancingInformationQuery,
    QUERY_CLIENT
}