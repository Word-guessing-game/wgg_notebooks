import * as React from "react"
import { Outlet } from "react-router-dom"
import NavBar from "../components/navBar"

export default function Layout() {
  return (
    <div>
      <NavBar />
      <hr />
      <Outlet />
    </div>
  )
}
