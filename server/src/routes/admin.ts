import { Router } from 'express';
import { store } from '../services/store';

export const adminRouter = Router();

// In-memory RBAC state
interface ClubAnnouncement {
  id: string;
  clubId: string;
  clubName: string;
  author: string;
  message: string;
  timestamp: string;
  pinned: boolean;
}

interface VenueSlotStatus {
  id: string;
  venueId: string;
  venueName: string;
  resourceName: string; // Court 1, VIP Table 4, etc.
  type: 'turf' | 'table' | 'court' | 'shelf';
  status: 'available' | 'booked' | 'maintenance';
  currentBookingRef?: string;
  customerName?: string;
  hourlyRate: number;
}

let ANNOUNCEMENTS: ClubAnnouncement[] = [
  {
    id: 'ann-1',
    clubId: 'c01',
    clubName: 'Bessie Flyers Run Club',
    author: 'Karthik (Captain)',
    message: '🌅 Tomorrow 5:15 AM Sunrise Run: Weather is 26°C with cool offshore breeze. Rendezvous at Besant Nagar police booth. Hydration station ready at 3.5km. Dosas & filter coffee at Murugan Idli after!',
    timestamp: 'Today, 06:30 PM',
    pinned: true
  },
  {
    id: 'ann-2',
    clubId: 'c02',
    clubName: 'Cubbon Park Sunrise Yoga',
    author: 'Priya Sharma',
    message: 'Sunday 6:30 AM session is in the Bamboo Grove behind State Central Library. Please bring your own mat & water bottle.',
    timestamp: 'Yesterday, 04:15 PM',
    pinned: false
  }
];

let VENUE_RESOURCES: VenueSlotStatus[] = [
  {
    id: 'res-1',
    venueId: 'v01',
    venueName: 'Indiranagar Arena Turf',
    resourceName: 'Pitch 1 (FIFA 5v5 Turf)',
    type: 'turf',
    status: 'booked',
    currentBookingRef: 'HOP-BLR-8921',
    customerName: 'Rohit Verma (4/10 checked in)',
    hourlyRate: 1400
  },
  {
    id: 'res-2',
    venueId: 'v01',
    venueName: 'Indiranagar Arena Turf',
    resourceName: 'Pitch 2 (7v7 Floodlit Pitch)',
    type: 'turf',
    status: 'available',
    hourlyRate: 1800
  },
  {
    id: 'res-3',
    venueId: 'v02',
    venueName: 'Toit Brewpub Indiranagar',
    resourceName: 'Rooftop Table 4 (Craft Tap)',
    type: 'table',
    status: 'booked',
    currentBookingRef: 'HOP-BLR-4412',
    customerName: 'Ananya S (Party of 6)',
    hourlyRate: 500
  },
  {
    id: 'res-4',
    venueId: 'v02',
    venueName: 'Toit Brewpub Indiranagar',
    resourceName: 'Main Brewery Table 8',
    type: 'table',
    status: 'available',
    hourlyRate: 500
  },
  {
    id: 'res-5',
    venueId: 'v03',
    venueName: 'Gameistry Board Game Lounge',
    resourceName: 'VIP Table Alpha (1,300+ Games)',
    type: 'shelf',
    status: 'available',
    hourlyRate: 350
  }
];

let CLUB_APPLICATIONS = [
  {
    id: 'app-1',
    clubName: 'OMR Sunrise Striders',
    city: 'Chennai (MAA)',
    area: 'Sholinganallur / ECR Link',
    category: 'running',
    applicant: 'Ganesh Nathan',
    expectedMembers: 60,
    status: 'pending',
    appliedDate: '24 Sep 2026'
  },
  {
    id: 'app-2',
    clubName: 'HSR Layout Padel Tribe',
    city: 'Bengaluru (BLR)',
    area: 'HSR Sector 2',
    category: 'sports',
    applicant: 'Rohan Mittal',
    expectedMembers: 45,
    status: 'pending',
    appliedDate: '23 Sep 2026'
  }
];

// 1. GET /api/admin/roles
adminRouter.get('/roles', (req, res) => {
  res.json({
    roles: [
      {
        id: 'super_admin',
        title: 'Super Admin (Platform)',
        subtitle: 'Global Hoppin HQ · Bengaluru & Chennai',
        name: 'Aravind S (Platform Director)',
        permissions: ['global_analytics', 'venue_verification', 'club_approval', 'payout_settlements', 'system_audit']
      },
      {
        id: 'group_admin',
        title: 'Group Admin (Youth & Run Clubs)',
        subtitle: 'Bessie Flyers Run Club · Chennai Health Hub',
        name: 'Karthik & Ananya (Club Captains)',
        permissions: ['club_roster', 'schedule_runs', 'broadcast_bulletins', 'award_streaks', 'attendance_scanner']
      },
      {
        id: 'restaurant_admin',
        title: 'Restaurant & Venue Admin',
        subtitle: 'Toit Brewpub & Indiranagar Arena Turf',
        name: 'Mukesh V (Operations Manager)',
        permissions: ['court_slot_matrix', 'live_occupancy', 'ticket_checkin_qr', 'pricing_surge', 'daily_settlements']
      }
    ]
  });
});

// 2. GET /api/admin/data
adminRouter.get('/data', (req, res) => {
  const role = (req.query.role as string) || 'super_admin';

  if (role === 'super_admin') {
    return res.json({
      role: 'super_admin',
      metrics: {
        totalGrossVolume: '₹28,45,200',
        activeVenuesCount: store.venues.length || 67,
        activeClubsCount: 18,
        totalBookingsMonth: 1842,
        platformFeeCollected: '₹99,580',
        activeUsersChennai: 2410,
        activeUsersBLR: 3180
      },
      pendingApprovals: CLUB_APPLICATIONS,
      recentAuditLogs: [
        { time: '10:04 AM', event: 'Venue Payout', desc: 'Settled ₹18,400 to Indiranagar Arena Turf' },
        { time: '09:42 AM', event: 'Club Verified', desc: 'Approved Cubbon Park Sunrise Yoga listing' },
        { time: '08:15 AM', event: 'Peak Surge Active', desc: 'Friday Night Turf multiplier set to 1.15x' }
      ]
    });
  }

  if (role === 'group_admin') {
    return res.json({
      role: 'group_admin',
      club: {
        id: 'c01',
        name: 'Bessie Flyers Run Club',
        city: 'Chennai (MAA)',
        area: "Elliot's Beach, Besant Nagar",
        activeMembers: 142,
        activeStreakWeeks: 18,
        nextMeetup: 'Tomorrow (Saturday), 05:15 AM · Elliot’s Beach Police Booth',
        routeDistance: '5K / 10K Beach & Coastal Boulevard',
        confirmedAttendees: 142,
        paceGroups: ['4:45 min/km (Speed)', '5:30 min/km (Cruiser)', '6:30 min/km (Social / Walk)']
      },
      announcements: ANNOUNCEMENTS,
      recentRSVPs: [
        { name: 'Roshini S', email: 'roshini@okaxis', time: '10 mins ago', streak: '5 Days 🔥' },
        { name: 'Vikram Menon', email: 'vikram@corso.run', time: '25 mins ago', streak: '12 Days 🔥' },
        { name: 'Ananya R', email: 'ananya@bessie.run', time: '1 hour ago', streak: '18 Days 🔥' }
      ]
    });
  }

  if (role === 'restaurant_admin') {
    return res.json({
      role: 'restaurant_admin',
      venue: {
        name: 'Indiranagar Arena & Toit Taproom',
        city: 'Bengaluru (BLR)',
        todayGross: '₹18,400',
        settledToBank: '₹14,200',
        pendingSettlement: '₹4,200',
        occupancyRate: '88% Peak Tonight'
      },
      resources: VENUE_RESOURCES,
      pricingSurge: {
        peakHourly: 1400,
        regularHourly: 1000,
        weekendMultiplier: '1.25x'
      }
    });
  }

  res.status(400).json({ error: 'Unknown role' });
});

// 3. POST /api/admin/venue/status (Toggle court or table status)
adminRouter.post('/venue/status', (req, res) => {
  const { resourceId, status } = req.body;
  const resItem = VENUE_RESOURCES.find(r => r.id === resourceId);
  if (!resItem) return res.status(404).json({ error: 'Resource not found' });

  resItem.status = status || (resItem.status === 'available' ? 'booked' : 'available');
  res.json({ success: true, resource: resItem, message: `Status updated to ${resItem.status}` });
});

// 4. POST /api/admin/club/announcement (Broadcast bulletin to run club members)
adminRouter.post('/club/announcement', (req, res) => {
  const { message, author, clubName } = req.body;
  if (!message) return res.status(400).json({ error: 'Message is required' });

  const newAnn: ClubAnnouncement = {
    id: 'ann-' + (ANNOUNCEMENTS.length + 1),
    clubId: 'c01',
    clubName: clubName || 'Bessie Flyers Run Club',
    author: author || 'Club Captain',
    message: String(message).trim(),
    timestamp: 'Just now',
    pinned: true
  };
  ANNOUNCEMENTS.unshift(newAnn);
  res.json({ success: true, announcement: newAnn, message: 'Announcement broadcasted to 142 club members!' });
});

// 5. POST /api/admin/ticket/checkin (Verify booking reference)
adminRouter.post('/ticket/checkin', (req, res) => {
  const { ticketRef } = req.body;
  if (!ticketRef) return res.status(400).json({ error: 'Ticket reference is required' });

  const cleanRef = String(ticketRef).trim().toUpperCase();
  res.json({
    success: true,
    verified: true,
    ticketRef: cleanRef,
    guestName: 'Verified Guest',
    venue: 'Indiranagar Arena Turf / Toit Brewpub',
    slots: 'Confirmed & Valid',
    message: `Ticket ${cleanRef} validated! Guest checked in successfully.`
  });
});

// 6. POST /api/admin/club/verify (Super Admin approves / rejects community club)
adminRouter.post('/club/verify', (req, res) => {
  const { appId, action } = req.body;
  const app = CLUB_APPLICATIONS.find(a => a.id === appId);
  if (!app) return res.status(404).json({ error: 'Application not found' });

  app.status = action === 'approve' ? 'approved' : 'rejected';
  res.json({
    success: true,
    application: app,
    message: `Club "${app.clubName}" ${app.status} successfully!`
  });
});
