/* eslint-disable no-unused-vars */
import * as React from "react";
import { createRoot } from "react-dom/client";
import {
  createBrowserRouter,
  RouterProvider,
  Route,
  Link,
} from "react-router-dom";
import Home from "./omponents/Home";
import { ContactList } from "./omponents/ContactList";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
  },
  {
    path: "/contact",
    element: <ContactList />,
  },
]);

createRoot(document.getElementById("root")).render(
  <RouterProvider router={router} />
);
