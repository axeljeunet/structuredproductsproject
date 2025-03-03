import { QueryClient, useQuery } from '@tanstack/react-query';
import getAPIUrl from './url';

const QUERY_CLIENT = new QueryClient();

function usePortfolioInformationQuery({ datetime }) {
    return useQuery({
        queryKey: ['information', { datetime }],
        queryFn: async () => {
            const res = await fetch(getAPIUrl("information"), {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ datetime })
            });

            const resJson = await res.json();

            if(!res.ok) {
                throw new Error(resJson.message);
            }

            return resJson;
        }
    });
}

function usePortfolioRebalancingInformationQuery({ datetime }) {
    return useQuery({
        queryKey: ['rebalancingInformation', { datetime }],
        queryFn: async () => {
            const res = await fetch(getAPIUrl("rebalancingInformation"), {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ datetime })
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
    QUERY_CLIENT
}