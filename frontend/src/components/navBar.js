import React from 'react';
import {
  Nav,
  NavLink,
  Bars,
  NavMenu,
  NavBtn,
  NavBtnLink,
} from './NavbarElements';

export default function NavBar() {
  return (
    <>
      <Nav>
        <Bars />

        <NavMenu>
          <NavLink to='/'>
            Home
          </NavLink>
          <NavLink to='/about'>
            About
          </NavLink>
        </NavMenu>
        <NavBtn>
          <NavBtnLink to='/signin'>Sign In</NavBtnLink>
        </NavBtn>
      </Nav>
    </>
  )
}
