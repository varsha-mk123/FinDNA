import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import DataImport from './pages/DataImport';
import Header from './components/common/Header';
import Sidebar from './components/common/Sidebar';

function App() {
  return (
    <Router>
      <div className="flex h-screen">
        <Sidebar />
        <div className="flex-1 flex flex-col">
          <Header />
          <main className="flex-1 p-6">
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/import" element={<DataImport />} />
            </Routes>
          </main>
        </div>
      </div>
    </Router>
  );
}

export default App;