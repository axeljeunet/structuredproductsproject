function useRebalanceMutation( { datetime } ) {
    return useMutation(
        {
            mutationFn: async () => {
                const res = await fetch(getAPIUrl("rebalance"), {
                      method: 'POST',
                      headers: { 'Content-Type': 'application/json' },
                      body: JSON.stringify({ datetime })
                });

                const resJson = await res.json();

                if (!res.ok) {
                    throw new Error(resJson.message);
                }

                return resJson;
            },
            onSuccess: () => {
                QUERY_CLIENT.invalidateQueries({ queryKey: ['information', { datetime }] })
                QUERY_CLIENT.invalidateQueries({ queryKey: ['rebalancingInformation', { datetime }] })
            }
        });
}