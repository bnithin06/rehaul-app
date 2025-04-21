'use client';

import React from 'react';
import Link from 'next/link';

const Footer = () => {
  return (
    <footer className="bg-[#3C3B5A] text-[#F8F3E4] py-6 mt-12">
      <div className="container mx-auto px-4 flex flex-col md:flex-row justify-center items-center">

        {/* Copyright */}
        <div className="text-xs mt-4 md:mt-0 text-gray-400">&copy; {new Date().getFullYear()} ReHaul. All rights reserved.</div>
      </div>
    </footer>
  );
};

export default Footer;
