import { createBrowserRouter, RouterProvider } from "react-router-dom"
import App from "./App";
import React from "react";
import IndexPage from "./components/indexes/IndexPage";


function AppRouterProvider() {
    const router = createBrowserRouter([
        {
            path: "/",
            element: <App />
        },
        {
            path: "/indexes",
            element: <IndexPage />
        }
    ])

    return <RouterProvider router={router} />
}

export default AppRouterProvider
