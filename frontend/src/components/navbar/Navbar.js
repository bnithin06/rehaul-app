'use client';

import React, { useState, useContext } from 'react';
import { Menu, X, UserCircle } from 'lucide-react';
import Link from 'next/link';
import AuthContext from '@/context/AuthContext';

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [showDropdown, setShowDropdown] = useState(false); // for profile dropdown
  const { user, logoutUser } = useContext(AuthContext);

  const toggleMenu = () => setIsOpen(!isOpen);
  const toggleDropdown = () => setShowDropdown(!showDropdown);

  return (
    <nav className="bg-[#3C3B5A] text-[#F8F3E4] shadow-md relative">
      <div className="container mx-auto flex justify-between items-center px-4 py-3">
        {/* Logo */}
        <div className="text-2xl font-bold tracking-wide">ReHaul</div>

        {/* Desktop Menu */}
        <ul className="hidden md:flex space-x-8 font-medium items-center">
          <NavItem title="Home" />
          <NavItem title="Services" />
          <NavItem title="Pricing" />
          <NavItem title="Contact" />

          {user ? (
            <li className="relative">
              <button onClick={toggleDropdown} className="focus:outline-none">
                <UserCircle size={28} className="text-[#F8F3E4]" />
              </button>

              {showDropdown && (
                <ul className="absolute right-0 mt-2 w-40 bg-white text-[#3C3B5A] rounded-md shadow-lg z-50">
                  <li className="px-4 py-2 hover:bg-gray-100">
                    <Link href="/profile">Your Profile</Link>
                  </li>
                  <li className="px-4 py-2 hover:bg-gray-100 cursor-pointer" onClick={logoutUser}>
                    Logout
                  </li>
                </ul>
              )}
            </li>
          ) : (
            <>
              <li>
                <Link href="/login" className="hover:text-[#AED6AC] transition-colors duration-200">
                  Sign In
                </Link>
              </li>
              <li>
                <Link href="/signup" className="hover:text-[#AED6AC] transition-colors duration-200">
                  Sign Up
                </Link>
              </li>
            </>
          )}
        </ul>

        {/* Mobile Menu Button */}
        <div className="md:hidden">
          <button onClick={toggleMenu} aria-label="Toggle Menu">
            {isOpen ? <X size={28} className="text-[#F8F3E4]" /> : <Menu size={28} className="text-[#F8F3E4]" />}
          </button>
        </div>
      </div>

      {/* Mobile Menu */}
      {isOpen && (
        <div className="md:hidden bg-[#89ABA2] text-[#3C3B5A]">
          <ul className="flex flex-col items-center space-y-5 py-6 font-medium">
            <NavItem title="Home" />
            <NavItem title="Services" />
            <NavItem title="Pricing" />
            <NavItem title="Contact" />

            {user ? (
              <>
                <li>
                  <Link href="/profile">Your Profile</Link>
                </li>
                <li onClick={logoutUser} className="cursor-pointer">
                  Logout
                </li>
              </>
            ) : (
              <>
                <li>
                  <Link href="/login">Sign In</Link>
                </li>
                <li>
                  <Link href="/signup">Sign Up</Link>
                </li>
              </>
            )}
          </ul>
        </div>
      )}
    </nav>
  );
};

const NavItem = ({ title }) => (
  <li className="cursor-pointer hover:text-[#AED6AC] transition-colors duration-200">
    <a href={`#${title.toLowerCase()}`}>{title}</a>
  </li>
);

export default Navbar;
