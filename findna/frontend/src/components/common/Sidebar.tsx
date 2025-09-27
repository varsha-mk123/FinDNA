import React from 'react';
import { Link, useLocation } from 'react-router-dom';

const Sidebar: React.FC = () => {
  const location = useLocation();

  const menuItems = [
    { path: '/', label: 'Dashboard' },
    { path: '/import', label: 'Import Data' },
  ];

  return (
    <div className="w-64 bg-gray-800 text-white">
      <nav className="mt-10">
        <ul>
          {menuItems.map((item) => (
            <li key={item.path} className="mb-2">
              <Link
                to={item.path}
                className={`block px-4 py-2 rounded-lg ${
                  location.pathname === item.path ? 'bg-gray-700' : 'hover:bg-gray-700'
                }`}
              >
                {item.label}
              </Link>
            </li>
          ))}
        </ul>
      </nav>
    </div>
  );
};

export default Sidebar;