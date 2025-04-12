"use client";

import React, { useState } from "react";
import { Menu, X } from "lucide-react"; // Lucide icons

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => setIsOpen(!isOpen);

  return (
    <nav className="bg-[#3C3B5A] text-[#F8F3E4] shadow-md">
      <div className="container mx-auto flex justify-between items-center px-4 py-3">
        {/* Logo */}
        <div className="text-2xl font-bold tracking-wide">ReHaul</div>

        {/* Desktop Menu */}
        <ul className="hidden md:flex space-x-8 font-medium">
          <NavItem title="Home" />
          <NavItem title="Services" />
          <NavItem title="Pricing" />
          <NavItem title="Contact" />
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