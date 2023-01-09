import * as React from "react"
import { Routes, Route } from "react-router-dom"
import Layout from "./pages/layout"
import Home from "./pages/home"
import About from "./pages/about"
import NotFound from "./pages/notFound"

export default function Router() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="about" element={<About />} />
        <Route path="*" element={<NotFound />} />
      </Route>
    </Routes>
  )
}
