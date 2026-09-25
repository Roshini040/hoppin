import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import VenueManagement from './pages/VenueManagement';
import UserManagement from './pages/UserManagement';
import Analytics from './pages/Analytics';

export default function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Dashboard</Link>
        <Link to="/venues">Venues</Link>
        <Link to="/users">Users</Link>
        <Link to="/analytics">Analytics</Link>
      </nav>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<Dashboard />} />
        <Route path="/venues" element={<VenueManagement />} />
        <Route path="/users" element={<UserManagement />} />
        <Route path="/analytics" element={<Analytics />} />
      </Routes>
    </BrowserRouter>
  );
}
