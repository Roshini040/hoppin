import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Register from './pages/Register';
import Dashboard from './pages/Dashboard';
import VenueManagement from './pages/VenueManagement';
import BookingsAndSlots from './pages/BookingsAndSlots';
import Revenue from './pages/Revenue';
import Reviews from './pages/Reviews';

export default function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Dashboard</Link>
        <Link to="/venue">Venue</Link>
        <Link to="/bookings">Bookings</Link>
        <Link to="/revenue">Revenue</Link>
        <Link to="/reviews">Reviews</Link>
      </nav>
      <Routes>
        <Route path="/register" element={<Register />} />
        <Route path="/" element={<Dashboard />} />
        <Route path="/venue" element={<VenueManagement />} />
        <Route path="/bookings" element={<BookingsAndSlots />} />
        <Route path="/revenue" element={<Revenue />} />
        <Route path="/reviews" element={<Reviews />} />
      </Routes>
    </BrowserRouter>
  );
}
