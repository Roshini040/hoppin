// Auto-generated from supabase/seed/seed_venues.sql (67 venues)
export interface Slot {
  id: string;
  time: string;
  price: number;
  available: boolean;
}

export interface Venue {
  id: string;
  name: string;
  category: 'club' | 'gym' | 'sports' | 'gaming' | 'pub' | 'restaurant' | string;
  city: 'Bengaluru' | 'Chennai' | string;
  area: string;
  priceTier: number;
  rating: number;
  reviewCount: number;
  tags: string[];
  description: string;
  isLive: boolean;
  photo: string;
  slots: Slot[];
}

export const VENUES_DATA: Venue[] = [
  {
    "id": "venue-1",
    "name": "Cubbon Park Yoga Flow Meetup",
    "category": "club",
    "city": "Bengaluru",
    "area": "Cubbon Park (State Central Library)",
    "priceTier": 1,
    "rating": 4.4,
    "reviewCount": 52,
    "tags": [
      "Yoga",
      "Gentle Movement",
      "Breathing Practices",
      "Beginner-friendly"
    ],
    "description": "Meets on Sundays at 6:30 AM at Cubbon Park for a 60-minute session combining gentle stretches, pranayama, relaxation, and group games.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-1-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-1-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-1-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 500,
        "available": true
      },
      {
        "id": "slot-1-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 600,
        "available": true
      },
      {
        "id": "slot-1-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 600,
        "available": false
      }
    ]
  },
  {
    "id": "venue-2",
    "name": "The Amateur League (TAL)",
    "category": "club",
    "city": "Bengaluru",
    "area": "Richards Town (Holy Ghost Church)",
    "priceTier": 2,
    "rating": 4.5,
    "reviewCount": 69,
    "tags": [
      "Football",
      "Amateur League",
      "Weekend Matches",
      "All Skill Levels"
    ],
    "description": "An 11-a-side semi-professional amateur football league hosting regular weekend matches throughout the year across two divisions for 24 teams.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1483721310020-03333e577078?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-2-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-2-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-2-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-2-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-2-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": true
      }
    ]
  },
  {
    "id": "venue-3",
    "name": "Aurum Luxury Fitness Club",
    "category": "gym",
    "city": "Bengaluru",
    "area": "Indiranagar (100 Feet Rd)",
    "priceTier": 3,
    "rating": 4.6,
    "reviewCount": 86,
    "tags": [
      "Luxury Gym",
      "Spa",
      "Sauna",
      "Strength Training",
      "Personal Training"
    ],
    "description": "A premium fitness club equipped with over 110 machines, recovery services, a Himalayan pink salt sauna, and personal trainers.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-3-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-3-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-3-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1500,
        "available": false
      },
      {
        "id": "slot-3-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1800,
        "available": true
      },
      {
        "id": "slot-3-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1800,
        "available": false
      }
    ]
  },
  {
    "id": "venue-4",
    "name": "Chisel Fitness",
    "category": "gym",
    "city": "Bengaluru",
    "area": "CV Raman Nagar",
    "priceTier": 2,
    "rating": 4.8,
    "reviewCount": 71,
    "tags": [
      "Strength Training",
      "Functional Fitness",
      "Cardio",
      "Core Workout"
    ],
    "description": "A modern neighborhood gym focusing on personalized strength programming, body toning, and cardio conditioning.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-4-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-4-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-4-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-4-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-4-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": true
      }
    ]
  },
  {
    "id": "venue-5",
    "name": "CrossFit Brave",
    "category": "gym",
    "city": "Bengaluru",
    "area": "Indiranagar",
    "priceTier": 2,
    "rating": 4.8,
    "reviewCount": 120,
    "tags": [
      "CrossFit",
      "HIIT",
      "Functional Training",
      "Olympic Weightlifting"
    ],
    "description": "A high-intensity CrossFit box providing community-driven functional movement workouts, Olympic weightlifting coaching, and daily WODs.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-5-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-5-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-5-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-5-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-5-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": false
      }
    ]
  },
  {
    "id": "venue-6",
    "name": "Cult Gym Indiranagar",
    "category": "gym",
    "city": "Bengaluru",
    "area": "Indiranagar",
    "priceTier": 2,
    "rating": 4.3,
    "reviewCount": 137,
    "tags": [
      "HRX",
      "Boxing",
      "Dance Fitness",
      "Strength & Conditioning",
      "Yoga"
    ],
    "description": "A tech-integrated flagship fitness center offering structured trainer-led group classes across Dance, HRX, Boxing, and Yoga formats.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-6-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-6-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-6-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": false
      },
      {
        "id": "slot-6-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-6-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": true
      }
    ]
  },
  {
    "id": "venue-7",
    "name": "Cyborg Fitness",
    "category": "gym",
    "city": "Bengaluru",
    "area": "Indiranagar / Whitefield",
    "priceTier": 2,
    "rating": 4.4,
    "reviewCount": 154,
    "tags": [
      "Mobility Training",
      "Cross-Training",
      "Yoga",
      "Group Fitness"
    ],
    "description": "A versatile boutique fitness studio specializing in cross-training, mobility workouts, and yoga classes tailored for all skill levels.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-7-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-7-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-7-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-7-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-7-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": false
      }
    ]
  },
  {
    "id": "venue-8",
    "name": "Fitness First",
    "category": "gym",
    "city": "Bengaluru",
    "area": "Indiranagar",
    "priceTier": 3,
    "rating": 4.5,
    "reviewCount": 171,
    "tags": [
      "Freestyle Playground",
      "TRX",
      "Les Mills",
      "BodyPump",
      "Battle Ropes"
    ],
    "description": "An innovative fitness club featuring a signature Freestyle Training Zone, suspension equipment, TRX, Les Mills classes, and nutrition counseling.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-8-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-8-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-8-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1500,
        "available": true
      },
      {
        "id": "slot-8-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1800,
        "available": true
      },
      {
        "id": "slot-8-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1800,
        "available": true
      }
    ]
  },
  {
    "id": "venue-9",
    "name": "Gold's Gym",
    "category": "gym",
    "city": "Bengaluru",
    "area": "Kalyan Nagar / Yelahanka",
    "priceTier": 3,
    "rating": 4.6,
    "reviewCount": 188,
    "tags": [
      "Strength Training",
      "Cardio",
      "Personal Training",
      "Diet Counseling"
    ],
    "description": "A multi-floor fitness facility featuring international strength equipment, certified trainers, customized nutrition planning, and lockers.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-9-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-9-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-9-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1500,
        "available": false
      },
      {
        "id": "slot-9-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1800,
        "available": true
      },
      {
        "id": "slot-9-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1800,
        "available": false
      }
    ]
  },
  {
    "id": "venue-10",
    "name": "Snap Fitness",
    "category": "gym",
    "city": "Bengaluru",
    "area": "Indiranagar / HSR Layout",
    "priceTier": 2,
    "rating": 4.7,
    "reviewCount": 205,
    "tags": [
      "24/7 Access",
      "Cardio",
      "Free Weights",
      "Functional Fitness"
    ],
    "description": "A 24/7 gym offering round-the-clock access to cardio equipment, free weights, and functional training areas for flexible schedules.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-10-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-10-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-10-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-10-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-10-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": true
      }
    ]
  },
  {
    "id": "venue-11",
    "name": "Arena Sports Complex",
    "category": "sports",
    "city": "Bengaluru",
    "area": "Indiranagar",
    "priceTier": 2,
    "rating": 4.8,
    "reviewCount": 222,
    "tags": [
      "Badminton",
      "Tennis",
      "Multi-Sport",
      "Fitness Facilities"
    ],
    "description": "A multi-sport complex offering indoor badminton courts, tennis courts, and fitness facilities accessible daily from 6 AM to 10 PM.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-11-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-11-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-11-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-11-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-11-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": false
      }
    ]
  },
  {
    "id": "venue-12",
    "name": "Holy Ghost Church Grounds",
    "category": "sports",
    "city": "Bengaluru",
    "area": "Richards Town",
    "priceTier": 1,
    "rating": 4.3,
    "reviewCount": 239,
    "tags": [
      "Football Pitch",
      "Match Grounds",
      "Outdoor Sports"
    ],
    "description": "Outdoor football match ground in Richards Town hosting weekly 11-a-side amateur football league matches.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-12-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-12-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-12-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 500,
        "available": false
      },
      {
        "id": "slot-12-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 600,
        "available": true
      },
      {
        "id": "slot-12-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 600,
        "available": true
      }
    ]
  },
  {
    "id": "venue-13",
    "name": "Koramangala Indoor Stadium",
    "category": "sports",
    "city": "Bengaluru",
    "area": "Koramangala / Indiranagar",
    "priceTier": 1,
    "rating": 4.4,
    "reviewCount": 46,
    "tags": [
      "Badminton",
      "Indoor Court",
      "Fitness Center"
    ],
    "description": "Indoor sports facility providing dedicated wooden badminton courts and a fitness arena for hourly booking.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1546519638-68e109498ffc?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-13-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-13-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-13-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 500,
        "available": true
      },
      {
        "id": "slot-13-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 600,
        "available": true
      },
      {
        "id": "slot-13-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 600,
        "available": false
      }
    ]
  },
  {
    "id": "venue-14",
    "name": "The Shuttle Court",
    "category": "sports",
    "city": "Bengaluru",
    "area": "Indiranagar",
    "priceTier": 2,
    "rating": 4.5,
    "reviewCount": 63,
    "tags": [
      "Badminton Court",
      "Wooden Flooring",
      "Indoor Sports"
    ],
    "description": "Dedicated indoor badminton courts with wooden flooring open for morning and evening play sessions.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1554068865-24cecd4e34b8?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-14-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-14-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-14-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-14-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-14-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": true
      }
    ]
  },
  {
    "id": "venue-15",
    "name": "Colosseum E-Sports",
    "category": "gaming",
    "city": "Bengaluru",
    "area": "Sadduguntepalya",
    "priceTier": 2,
    "rating": 4.6,
    "reviewCount": 80,
    "tags": [
      "E-Sports",
      "Gaming PCs",
      "Tournaments"
    ],
    "description": "Features high-performance gaming PCs, soundproof booths, and fast internet for competitive gaming and community tournaments.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1580234811497-9df7fd2f357e?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-15-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-15-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-15-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": false
      },
      {
        "id": "slot-15-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-15-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": false
      }
    ]
  },
  {
    "id": "venue-16",
    "name": "Fun City",
    "category": "gaming",
    "city": "Bengaluru",
    "area": "Mahadevapura (Phoenix Marketcity)",
    "priceTier": 2,
    "rating": 4.7,
    "reviewCount": 97,
    "tags": [
      "Arcade Games",
      "Kiddie Rides",
      "Family Gaming"
    ],
    "description": "A mall-based entertainment center offering arcade games, kiddie rides, and redemption machines for families.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-16-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-16-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-16-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-16-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-16-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": true
      }
    ]
  },
  {
    "id": "venue-17",
    "name": "IONA - Fun Ka Boss",
    "category": "gaming",
    "city": "Bengaluru",
    "area": "Whitefield (Virginia Mall)",
    "priceTier": 2,
    "rating": 4.8,
    "reviewCount": 114,
    "tags": [
      "VR Simulators",
      "Bowling",
      "Laser Tag",
      "Arcade"
    ],
    "description": "A modern entertainment hub inside Virginia Mall equipped with VR simulators, bowling alleys, laser tag, and arcade games.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1612287232230-65c27f3f269a?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-17-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-17-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-17-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-17-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-17-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": false
      }
    ]
  },
  {
    "id": "venue-18",
    "name": "WonderLa Arcade",
    "category": "gaming",
    "city": "Bengaluru",
    "area": "Kasavanahalli",
    "priceTier": 3,
    "rating": 4.3,
    "reviewCount": 131,
    "tags": [
      "Arcade",
      "VR Shooting",
      "Racing Simulators"
    ],
    "description": "An indoor amusement arcade featuring VR shooting, racing simulators, and skill-based games.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1610890716171-6b1bb98ffd09?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-18-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-18-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-18-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1500,
        "available": false
      },
      {
        "id": "slot-18-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1800,
        "available": true
      },
      {
        "id": "slot-18-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1800,
        "available": true
      }
    ]
  },
  {
    "id": "venue-19",
    "name": "1131 Bar + Kitchen By House Of Commons",
    "category": "pub",
    "city": "Bengaluru",
    "area": "Indiranagar",
    "priceTier": 3,
    "rating": 4.5,
    "reviewCount": 148,
    "tags": [
      "Rooftop",
      "Cocktails",
      "North Indian",
      "Indo-Chinese"
    ],
    "description": "A multi-level rooftop venue with large windows framing greenery, built for unhurried meals and drinks under open skies.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1538488254700-2e955b9c4500?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-19-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-19-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-19-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1500,
        "available": true
      },
      {
        "id": "slot-19-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1800,
        "available": true
      },
      {
        "id": "slot-19-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1800,
        "available": false
      }
    ]
  },
  {
    "id": "venue-20",
    "name": "21st Amendment Gastrobar",
    "category": "pub",
    "city": "Bengaluru",
    "area": "Indiranagar",
    "priceTier": 3,
    "rating": 4.3,
    "reviewCount": 165,
    "tags": [
      "Craft Beer",
      "Rooftop Views",
      "Gastrobar",
      "Live Performances"
    ],
    "description": "A rooftop gastrobar offering craft beers, creative cocktails, Moroccan grilled fish, and skyline views.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-20-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-20-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-20-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1500,
        "available": true
      },
      {
        "id": "slot-20-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1800,
        "available": true
      },
      {
        "id": "slot-20-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1800,
        "available": true
      }
    ]
  },
  {
    "id": "venue-21",
    "name": "Bob's Bar",
    "category": "pub",
    "city": "Bengaluru",
    "area": "Indiranagar",
    "priceTier": 1,
    "rating": 4.6,
    "reviewCount": 182,
    "tags": [
      "Old-school Pub",
      "Local Specialties",
      "Outdoor Seating"
    ],
    "description": "A laid-back, no-frills pub honoring old-school Bangalore with quick service, drinks, and regional specialties like Malnad-style pork.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1572116469696-31de0f17cc34?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-21-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-21-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-21-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 500,
        "available": false
      },
      {
        "id": "slot-21-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 600,
        "available": true
      },
      {
        "id": "slot-21-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 600,
        "available": false
      }
    ]
  },
  {
    "id": "venue-22",
    "name": "Doff Pub",
    "category": "pub",
    "city": "Bengaluru",
    "area": "Indiranagar",
    "priceTier": 2,
    "rating": 4.7,
    "reviewCount": 199,
    "tags": [
      "Sports Screening",
      "Rooftop",
      "Foosball",
      "Bar Games"
    ],
    "description": "A sports screening pub featuring big screens, foosball tables, clay-oven kebabs, and rooftop seating.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1543007630-9710e4a00a20?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-22-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-22-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-22-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-22-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-22-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": true
      }
    ]
  },
  {
    "id": "venue-23",
    "name": "Plan B",
    "category": "pub",
    "city": "Bengaluru",
    "area": "Indiranagar",
    "priceTier": 2,
    "rating": 4.8,
    "reviewCount": 216,
    "tags": [
      "Tap Beer",
      "Buffalo Wings",
      "Happy Hours"
    ],
    "description": "A popular resto bar and pub known for tap beers, creamy buffalo wings, and half-off specials on Tuesdays.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1538488254700-2e955b9c4500?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-23-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-23-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-23-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-23-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-23-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": false
      }
    ]
  },
  {
    "id": "venue-24",
    "name": "The Reservoire",
    "category": "pub",
    "city": "Bengaluru",
    "area": "Indiranagar",
    "priceTier": 2,
    "rating": 4.5,
    "reviewCount": 233,
    "tags": [
      "Cocktails",
      "Rooftop",
      "Pet-friendly",
      "Live Music"
    ],
    "description": "A Manhattan-style cocktail pub spanning two levels and a rooftop, offering over 200 cocktail varieties and pet-friendly spaces.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-24-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-24-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-24-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": false
      },
      {
        "id": "slot-24-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-24-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": true
      }
    ]
  },
  {
    "id": "venue-25",
    "name": "Tipsy Bull - The Bar Exchange",
    "category": "pub",
    "city": "Bengaluru",
    "area": "Indiranagar",
    "priceTier": 2,
    "rating": 4.2,
    "reviewCount": 40,
    "tags": [
      "Bar Exchange",
      "High-Energy",
      "Mechanical Bull",
      "Cocktails"
    ],
    "description": "A high-energy bar exchange concept featuring price-ticker lightboxes, dollar-bill counter wraps, and a mechanical bull.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1572116469696-31de0f17cc34?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-25-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-25-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-25-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-25-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-25-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": false
      }
    ]
  },
  {
    "id": "venue-26",
    "name": "Toit",
    "category": "pub",
    "city": "Bengaluru",
    "area": "Indiranagar",
    "priceTier": 2,
    "rating": 4.5,
    "reviewCount": 57,
    "tags": [
      "Craft Beer",
      "Brewpub",
      "Community Outreach"
    ],
    "description": "A landmark brewpub famous for unique craft beers like Nitro Stout and cider alongside pub-style food.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1543007630-9710e4a00a20?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-26-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-26-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-26-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-26-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-26-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": true
      }
    ]
  },
  {
    "id": "venue-27",
    "name": "Swiing Gourmet Table & Wine Bar",
    "category": "restaurant",
    "city": "Bengaluru",
    "area": "Indiranagar",
    "priceTier": 3,
    "rating": 4.6,
    "reviewCount": 74,
    "tags": [
      "Gourmet Dining",
      "Wine Bar",
      "Tropical Fusion"
    ],
    "description": "A 50-seater glasshouse restaurant and wine bar offering tropical-influenced gourmet fusion dishes by Chef Tarun Sibal.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1559339352-11d035aa65de?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-27-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-27-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-27-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1500,
        "available": false
      },
      {
        "id": "slot-27-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1800,
        "available": true
      },
      {
        "id": "slot-27-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1800,
        "available": false
      }
    ]
  },
  {
    "id": "venue-28",
    "name": "Vesparo",
    "category": "restaurant",
    "city": "Bengaluru",
    "area": "Indiranagar",
    "priceTier": 2,
    "rating": 4.1,
    "reviewCount": 91,
    "tags": [
      "Pan-Asian",
      "Continental",
      "Cocktails",
      "Island Bar"
    ],
    "description": "A high-energy pan-Asian and continental dining venue with a central island bar and dramatic indoor setting.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-28-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-28-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-28-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-28-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-28-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": true
      }
    ]
  },
  {
    "id": "venue-29",
    "name": "YUKI",
    "category": "restaurant",
    "city": "Bengaluru",
    "area": "Indiranagar",
    "priceTier": 2,
    "rating": 4.5,
    "reviewCount": 108,
    "tags": [
      "Pan-Asian",
      "Fine Dining",
      "Cocktails"
    ],
    "description": "A refined pan-Asian dining room featuring artful dish presentation and complementary cocktails in an unhurried atmosphere.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-29-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-29-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-29-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-29-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-29-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": false
      }
    ]
  },
  {
    "id": "venue-30",
    "name": "Bat Club",
    "category": "club",
    "city": "Chennai",
    "area": "Anna Nagar, Kilpauk & Marina Beach",
    "priceTier": 1,
    "rating": 4.3,
    "reviewCount": 125,
    "tags": [
      "Running",
      "Sunday Beach Run",
      "Social Breakfast"
    ],
    "description": "Sunday morning road and beach running club meeting across Anna Nagar and Kilpauk, followed by group breakfast socials.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-30-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-30-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-30-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 500,
        "available": false
      },
      {
        "id": "slot-30-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 600,
        "available": true
      },
      {
        "id": "slot-30-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 600,
        "available": true
      }
    ]
  },
  {
    "id": "venue-31",
    "name": "Chennai Runners (Bessie Flyers & Chapters)",
    "category": "club",
    "city": "Chennai",
    "area": "Besant Nagar (Elliot's Beach) & 18 Chapters",
    "priceTier": 1,
    "rating": 4.4,
    "reviewCount": 142,
    "tags": [
      "Running",
      "Beach Loop",
      "All Paces",
      "Tuesday/Thursday/Sunday 5:15 AM"
    ],
    "description": "Volunteer-run non-profit operating 18 chapters across Chennai; holds weekly group beach and road runs at 5:15 AM.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-31-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-31-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-31-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 500,
        "available": true
      },
      {
        "id": "slot-31-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 600,
        "available": true
      },
      {
        "id": "slot-31-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 600,
        "available": false
      }
    ]
  },
  {
    "id": "venue-32",
    "name": "Ciclo Cafe Community",
    "category": "club",
    "city": "Chennai",
    "area": "Kotturpuram",
    "priceTier": 2,
    "rating": 4.5,
    "reviewCount": 159,
    "tags": [
      "Cycling",
      "Social Rides",
      "Cafe Network",
      "Intermediate"
    ],
    "description": "Cycling cafe and cyclist networking hub hosting weekly group rides and social networking events for bicycle enthusiasts.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1483721310020-03333e577078?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-32-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-32-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-32-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-32-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-32-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": true
      }
    ]
  },
  {
    "id": "venue-33",
    "name": "CORSO Run Club",
    "category": "club",
    "city": "Chennai",
    "area": "Besant Nagar / Chennai Beachfront",
    "priceTier": 1,
    "rating": 4.6,
    "reviewCount": 176,
    "tags": [
      "Running",
      "3K Beach Run",
      "Social Games",
      "Beginner-friendly"
    ],
    "description": "Sunday beachfront running group combining a 3K run along Elliot's Beach with traditional outdoor social games like kho-kho.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-33-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-33-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-33-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 500,
        "available": false
      },
      {
        "id": "slot-33-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 600,
        "available": true
      },
      {
        "id": "slot-33-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 600,
        "available": false
      }
    ]
  },
  {
    "id": "venue-34",
    "name": "Dream Runners",
    "category": "club",
    "city": "Chennai",
    "area": "Besant Nagar, Boat Club, Marina, Anna Nagar, Velachery",
    "priceTier": 1,
    "rating": 4.7,
    "reviewCount": 193,
    "tags": [
      "Running",
      "Half-Marathon Prep",
      "Coached Sessions",
      "Beginner to Competitive"
    ],
    "description": "Community running network across 12+ chapters offering structured coached training twice weekly and hosting the Dream Runners Half Marathon.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-34-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-34-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-34-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 500,
        "available": true
      },
      {
        "id": "slot-34-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 600,
        "available": true
      },
      {
        "id": "slot-34-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 600,
        "available": true
      }
    ]
  },
  {
    "id": "venue-35",
    "name": "Tamilnadu Cycling Club (TCC)",
    "category": "club",
    "city": "Chennai",
    "area": "City-wide",
    "priceTier": 1,
    "rating": 4.8,
    "reviewCount": 210,
    "tags": [
      "Cycling",
      "Endurance",
      "Brevets",
      "Advanced"
    ],
    "description": "Long-standing cycling association organizing brevets, long-distance touring, and amateur road racing events across Tamil Nadu.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1483721310020-03333e577078?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-35-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-35-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-35-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 500,
        "available": true
      },
      {
        "id": "slot-35-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 600,
        "available": true
      },
      {
        "id": "slot-35-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 600,
        "available": false
      }
    ]
  },
  {
    "id": "venue-36",
    "name": "VAMOS Run Club",
    "category": "club",
    "city": "Chennai",
    "area": "Besant Nagar Beach & Anna Nagar",
    "priceTier": 1,
    "rating": 4.3,
    "reviewCount": 227,
    "tags": [
      "Running",
      "Beach Loops",
      "All Paces",
      "Night Runs"
    ],
    "description": "All-pace community run club holding weekend morning beach loops along Elliot's Beach and occasional social night runs.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-36-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-36-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-36-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 500,
        "available": false
      },
      {
        "id": "slot-36-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 600,
        "available": true
      },
      {
        "id": "slot-36-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 600,
        "available": true
      }
    ]
  },
  {
    "id": "venue-37",
    "name": "WCCG - We Are Chennai Cycling Group",
    "category": "club",
    "city": "Chennai",
    "area": "City-wide (16 chapters incl. Anna Nagar, Marina, OMR)",
    "priceTier": 1,
    "rating": 4.4,
    "reviewCount": 244,
    "tags": [
      "Cycling",
      "Road Cycling",
      "All Paces",
      "Community Rides"
    ],
    "description": "Premier city-wide cycling community with 16 local chapters, hosting weekly morning road rides, challenges, and core workouts.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-37-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-37-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-37-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 500,
        "available": true
      },
      {
        "id": "slot-37-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 600,
        "available": true
      },
      {
        "id": "slot-37-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 600,
        "available": false
      }
    ]
  },
  {
    "id": "venue-38",
    "name": "Cult Adyar",
    "category": "gym",
    "city": "Chennai",
    "area": "Adyar",
    "priceTier": 2,
    "rating": 5,
    "reviewCount": 51,
    "tags": [
      "Boxing",
      "Yoga",
      "Dance Fitness",
      "HIIT",
      "Strength"
    ],
    "description": "Offers trainer-guided group workout classes including HRX, Adidas Strength, Burn, Boxing, and Yoga with certified instructors.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-38-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-38-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-38-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-38-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-38-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": true
      }
    ]
  },
  {
    "id": "venue-39",
    "name": "Cult Alwarpet",
    "category": "gym",
    "city": "Chennai",
    "area": "Alwarpet",
    "priceTier": 2,
    "rating": 4.6,
    "reviewCount": 68,
    "tags": [
      "Group Classes",
      "Gym",
      "Elite Gym"
    ],
    "description": "Offers Elite gym access and scheduled trainer-led group workouts.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-39-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-39-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-39-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": false
      },
      {
        "id": "slot-39-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-39-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": false
      }
    ]
  },
  {
    "id": "venue-40",
    "name": "Cult Nungambakkam",
    "category": "gym",
    "city": "Chennai",
    "area": "Nungambakkam",
    "priceTier": 2,
    "rating": 4.7,
    "reviewCount": 85,
    "tags": [
      "Group Classes",
      "Fitness"
    ],
    "description": "Provides scheduled trainer-guided group workout formats and fitness training.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-40-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-40-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-40-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-40-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-40-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": true
      }
    ]
  },
  {
    "id": "venue-41",
    "name": "Cult T Nagar",
    "category": "gym",
    "city": "Chennai",
    "area": "T. Nagar",
    "priceTier": 2,
    "rating": 4.8,
    "reviewCount": 102,
    "tags": [
      "Group Classes",
      "Fitness"
    ],
    "description": "Features structured trainer-led group fitness classes across multiple formats.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-41-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-41-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-41-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-41-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-41-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": false
      }
    ]
  },
  {
    "id": "venue-42",
    "name": "Cult Velachery Chennai - Hybrid",
    "category": "gym",
    "city": "Chennai",
    "area": "Velachery",
    "priceTier": 2,
    "rating": 4.3,
    "reviewCount": 119,
    "tags": [
      "Group Classes",
      "Elite Gym",
      "Hybrid"
    ],
    "description": "A hybrid center offering Elite gym facilities alongside group workout classes.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-42-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-42-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-42-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": false
      },
      {
        "id": "slot-42-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-42-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": true
      }
    ]
  },
  {
    "id": "venue-43",
    "name": "Women's Gym - Indira Nagar, Adyar",
    "category": "gym",
    "city": "Chennai",
    "area": "Adyar / Indira Nagar",
    "priceTier": 1,
    "rating": 4.4,
    "reviewCount": 136,
    "tags": [
      "Aerobics",
      "Zumba",
      "HIIT",
      "Bodyweight Training",
      "Women-Only"
    ],
    "description": "An exclusive budget women's gym featuring small group sessions (under 7 people) and floor workouts on sports mat flooring.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-43-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-43-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-43-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 500,
        "available": true
      },
      {
        "id": "slot-43-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 600,
        "available": true
      },
      {
        "id": "slot-43-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 600,
        "available": false
      }
    ]
  },
  {
    "id": "venue-44",
    "name": "Plug N Play by Munchow",
    "category": "sports",
    "city": "Chennai",
    "area": "Perungudi",
    "priceTier": 2,
    "rating": 4.3,
    "reviewCount": 153,
    "tags": [
      "Cricket Nets",
      "Snooker",
      "VR Racing",
      "PS5",
      "Board Games"
    ],
    "description": "Multi-activity entertainment venue featuring indoor cricket nets, snooker tables, VR racing cockpits, and PS5 gaming consoles.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1554068865-24cecd4e34b8?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-44-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-44-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-44-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-44-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-44-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": true
      }
    ]
  },
  {
    "id": "venue-45",
    "name": "Gameistry",
    "category": "gaming",
    "city": "Chennai",
    "area": "Egmore",
    "priceTier": 1,
    "rating": 4.5,
    "reviewCount": 170,
    "tags": [
      "Board Games",
      "1300+ Games",
      "Game Gurus",
      "Family-Friendly"
    ],
    "description": "A retro-inspired board game venue with over 1,300 board games, on-site Game Gurus to explain rules, and casual cafe food.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1612287232230-65c27f3f269a?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-45-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-45-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-45-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 500,
        "available": false
      },
      {
        "id": "slot-45-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 600,
        "available": true
      },
      {
        "id": "slot-45-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 600,
        "available": false
      }
    ]
  },
  {
    "id": "venue-46",
    "name": "GameOn Cafe",
    "category": "gaming",
    "city": "Chennai",
    "area": "T. Nagar",
    "priceTier": 1,
    "rating": 4.7,
    "reviewCount": 187,
    "tags": [
      "Board Games",
      "Strategy Games",
      "Beverages"
    ],
    "description": "A dedicated board game cafe featuring a wide selection of strategy and creative games like Catan alongside beverages.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1610890716171-6b1bb98ffd09?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-46-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-46-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-46-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 500,
        "available": true
      },
      {
        "id": "slot-46-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 600,
        "available": true
      },
      {
        "id": "slot-46-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 600,
        "available": true
      }
    ]
  },
  {
    "id": "venue-47",
    "name": "Gamesync",
    "category": "gaming",
    "city": "Chennai",
    "area": "Velachery",
    "priceTier": 1,
    "rating": 4.8,
    "reviewCount": 204,
    "tags": [
      "Board Games",
      "Cozy Hangout",
      "Savouries"
    ],
    "description": "A cozy board game cafe providing games like Azul and Cluedo alongside savouries for group meet-ups.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1580234811497-9df7fd2f357e?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-47-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-47-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-47-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 500,
        "available": true
      },
      {
        "id": "slot-47-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 600,
        "available": true
      },
      {
        "id": "slot-47-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 600,
        "available": false
      }
    ]
  },
  {
    "id": "venue-48",
    "name": "The Board Game Lounge",
    "category": "gaming",
    "city": "Chennai",
    "area": "Adyar",
    "priceTier": 1,
    "rating": 4.3,
    "reviewCount": 221,
    "tags": [
      "Board Games",
      "Strategy Games",
      "Theme Games"
    ],
    "description": "An extensive board game lounge featuring strategy, book, and anime-themed titles like Dune Imperium and Cascadia.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-48-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-48-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-48-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 500,
        "available": false
      },
      {
        "id": "slot-48-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 600,
        "available": true
      },
      {
        "id": "slot-48-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 600,
        "available": true
      }
    ]
  },
  {
    "id": "venue-49",
    "name": "The Board Room",
    "category": "gaming",
    "city": "Chennai",
    "area": "Mylapore",
    "priceTier": 1,
    "rating": 4.4,
    "reviewCount": 238,
    "tags": [
      "Board Games",
      "Italian",
      "Cafe"
    ],
    "description": "A modern, minimalist board game cafe where guests can play games while dining on Italian pasta, cheese balls, and hot chocolate.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1612287232230-65c27f3f269a?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-49-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-49-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-49-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 500,
        "available": true
      },
      {
        "id": "slot-49-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 600,
        "available": true
      },
      {
        "id": "slot-49-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 600,
        "available": false
      }
    ]
  },
  {
    "id": "venue-50",
    "name": "Untangle - House of Puzzles",
    "category": "gaming",
    "city": "Chennai",
    "area": "Teynampet",
    "priceTier": 1,
    "rating": 4.5,
    "reviewCount": 45,
    "tags": [
      "Puzzles",
      "400+ Board Games",
      "Family-Friendly"
    ],
    "description": "A puzzle and board game sanctuary featuring over 1,200 puzzles and 400 board games for family gatherings.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1610890716171-6b1bb98ffd09?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-50-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-50-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-50-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 500,
        "available": true
      },
      {
        "id": "slot-50-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 600,
        "available": true
      },
      {
        "id": "slot-50-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 600,
        "available": true
      }
    ]
  },
  {
    "id": "venue-51",
    "name": "Shout Bar & Cafe",
    "category": "pub",
    "city": "Chennai",
    "area": "Porur",
    "priceTier": 2,
    "rating": 4.3,
    "reviewCount": 62,
    "tags": [
      "Party Games",
      "Trivia",
      "Indo-Chinese",
      "Bar"
    ],
    "description": "A loud, casual bar and cafe catering to big groups with party games, trivia, cards, and Indo-Chinese food.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1538488254700-2e955b9c4500?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-51-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-51-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-51-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": false
      },
      {
        "id": "slot-51-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-51-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": false
      }
    ]
  },
  {
    "id": "venue-52",
    "name": "Slounge - Lemon Tree Shimona",
    "category": "pub",
    "city": "Chennai",
    "area": "Ramapuram",
    "priceTier": 2,
    "rating": 4.3,
    "reviewCount": 79,
    "tags": [
      "Billiards",
      "Chess",
      "Bar Lounge",
      "Cocktails"
    ],
    "description": "A hotel bar lounge featuring chess, backgammon, and a billiards table accompanied by house cocktails and finger food.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-52-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-52-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-52-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-52-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-52-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": true
      }
    ]
  },
  {
    "id": "venue-53",
    "name": "The Madras Taproom",
    "category": "pub",
    "city": "Chennai",
    "area": "Egmore",
    "priceTier": 2,
    "rating": 4.4,
    "reviewCount": 96,
    "tags": [
      "Pool Table",
      "Board Games",
      "Taproom",
      "Industrial Pub"
    ],
    "description": "An industrial-style pub with exposed brick, pool tables, and board games like Sequence and Catan alongside North and South Indian food.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1572116469696-31de0f17cc34?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-53-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-53-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-53-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-53-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-53-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": false
      }
    ]
  },
  {
    "id": "venue-54",
    "name": "Watson's",
    "category": "pub",
    "city": "Chennai",
    "area": "T. Nagar",
    "priceTier": 2,
    "rating": 4.2,
    "reviewCount": 113,
    "tags": [
      "Industrial Pub",
      "Draught Beer",
      "North Indian"
    ],
    "description": "An industrial-style pub with high ceilings and spacious seating, serving draught beer and dishes like Beef Pepper Fry.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1543007630-9710e4a00a20?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-54-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-54-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-54-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": false
      },
      {
        "id": "slot-54-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-54-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": true
      }
    ]
  },
  {
    "id": "venue-55",
    "name": "Atte - Glocal Cafe",
    "category": "restaurant",
    "city": "Chennai",
    "area": "Besant Nagar",
    "priceTier": 1,
    "rating": 4.4,
    "reviewCount": 130,
    "tags": [
      "Board Games",
      "Open-Air",
      "Continental",
      "Bohemian Cafe"
    ],
    "description": "An artsy, open-air beachside cafe offering casual board games like Carrom, Uno, and Jenga alongside pasta, shakes, and resident dogs.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1559339352-11d035aa65de?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-55-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-55-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-55-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 500,
        "available": true
      },
      {
        "id": "slot-55-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 600,
        "available": true
      },
      {
        "id": "slot-55-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 600,
        "available": false
      }
    ]
  },
  {
    "id": "venue-56",
    "name": "The Old Potion House",
    "category": "restaurant",
    "city": "Chennai",
    "area": "Adyar",
    "priceTier": 2,
    "rating": 3.8,
    "reviewCount": 147,
    "tags": [
      "Fantasy Theme",
      "Spell-casting Games",
      "Interactive Mocktails",
      "Italian"
    ],
    "description": "A fantasy-themed Italian dining spot offering spell-casting and deduction games alongside potion mocktails.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-56-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-56-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-56-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-56-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-56-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": true
      }
    ]
  },
  {
    "id": "venue-57",
    "name": "Zha Cafe",
    "category": "restaurant",
    "city": "Chennai",
    "area": "Porur",
    "priceTier": 1,
    "rating": 4.3,
    "reviewCount": 164,
    "tags": [
      "Traditional Games",
      "Herbal Coffee",
      "Community Cafe"
    ],
    "description": "A quirky community cafe offering traditional Tamil board games such as Pallanguzhi and Aadu Puli Aattam alongside herbal Sukku coffee.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-57-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-57-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-57-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 500,
        "available": false
      },
      {
        "id": "slot-57-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 600,
        "available": true
      },
      {
        "id": "slot-57-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 600,
        "available": false
      }
    ]
  },
  {
    "id": "venue-58",
    "name": "Tiki Taka Football Academy & Turf",
    "category": "sports",
    "city": "Chennai",
    "area": "Kilpauk, T. Nagar, Velachery, Ampa Skywalk, Injambakkam & Mogappair West",
    "priceTier": 2,
    "rating": 4.7,
    "reviewCount": 181,
    "tags": [
      "Football",
      "Turf Rental",
      "Kids Academy",
      "Floodlit"
    ],
    "description": "Multi-branch football turf and academy chain with open-air and indoor floodlit 4v4/5v5 fields, AC viewing gallery, and a Toddlers Turf Camp for young kids. Turf rental ₹1,000-2,000/hour, Toddlers Camp ₹2,000/month.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1546519638-68e109498ffc?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-58-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-58-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-58-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-58-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-58-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": true
      }
    ]
  },
  {
    "id": "venue-59",
    "name": "FC Marina Turf & Football Academy",
    "category": "sports",
    "city": "Chennai",
    "area": "Vanagaram/Thiruverkadu, Thiruvanmiyur, Perumbakkam & Thalambur",
    "priceTier": 2,
    "rating": 4.8,
    "reviewCount": 198,
    "tags": [
      "Football",
      "Turf Rental",
      "Youth Coaching",
      "Floodlit"
    ],
    "description": "Multi-branch turf chain with floodlit 5-a-side and 7-a-side artificial pitches, changing rooms, washrooms, and an active youth football coaching academy.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1554068865-24cecd4e34b8?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-59-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-59-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-59-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-59-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-59-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": false
      }
    ]
  },
  {
    "id": "venue-60",
    "name": "Spark Football Academy (Spark Turf)",
    "category": "sports",
    "city": "Chennai",
    "area": "Puzhuthivakkam",
    "priceTier": 1,
    "rating": 4.3,
    "reviewCount": 215,
    "tags": [
      "Football",
      "Turf Rental",
      "Kids Academy"
    ],
    "description": "Box turf ground with locker rooms, parking, and a youth football academy. ₹800/hour weekdays, ₹1,000/hour weekends for 8 players.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-60-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-60-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 400,
        "available": true
      },
      {
        "id": "slot-60-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 500,
        "available": false
      },
      {
        "id": "slot-60-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 600,
        "available": true
      },
      {
        "id": "slot-60-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 600,
        "available": true
      }
    ]
  },
  {
    "id": "venue-61",
    "name": "Playpro7 Sport Turf",
    "category": "sports",
    "city": "Chennai",
    "area": "Chennai",
    "priceTier": 2,
    "rating": 4.4,
    "reviewCount": 232,
    "tags": [
      "Football",
      "Cricket",
      "FIFA-standard Turf",
      "Kids Coaching"
    ],
    "description": "FIFA-standard 5-a-side artificial football turf offering structured football and cricket coaching for kids.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-61-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-61-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-61-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-61-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-61-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": false
      }
    ]
  },
  {
    "id": "venue-62",
    "name": "El Clasico Football Turf & Club",
    "category": "sports",
    "city": "Chennai",
    "area": "Chromepet",
    "priceTier": 2,
    "rating": 4.5,
    "reviewCount": 39,
    "tags": [
      "Football",
      "Kids Academy",
      "Mini Fields"
    ],
    "description": "Compact mini football fields for children's development training and small-group play, plus a resident club running regular kids' coaching. Ground rental ₹1,200-1,500 per 2-4 hour session.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-62-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-62-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-62-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-62-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-62-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": true
      }
    ]
  },
  {
    "id": "venue-63",
    "name": "Estilio Sports Academy",
    "category": "sports",
    "city": "Chennai",
    "area": "Anna Nagar",
    "priceTier": 2,
    "rating": 4.6,
    "reviewCount": 56,
    "tags": [
      "Football",
      "Cricket",
      "Turf",
      "Coaching"
    ],
    "description": "Artificial turf venue offering organized football and cricket coaching plus open play.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1546519638-68e109498ffc?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-63-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-63-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-63-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": false
      },
      {
        "id": "slot-63-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-63-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": false
      }
    ]
  },
  {
    "id": "venue-64",
    "name": "Dugout Indoor Entertainment Arena",
    "category": "sports",
    "city": "Chennai",
    "area": "OMR (The Marina Mall) & Velachery (Grand Square Mall)",
    "priceTier": 2,
    "rating": 4.7,
    "reviewCount": 73,
    "tags": [
      "Cricket Nets",
      "Automated Bowling Machine",
      "Multi-Sport Turf",
      "Trampoline Zone",
      "Escape Rooms"
    ],
    "description": "7,000 sq ft indoor multi-sport turf arena with caged cricket nets and automated bowling machines for solo or group practice, plus a trampoline zone and escape rooms. Open 10 AM-11 PM daily.",
    "isLive": true,
    "photo": "https://images.unsplash.com/photo-1554068865-24cecd4e34b8?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-64-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-64-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-64-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-64-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-64-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": true
      }
    ]
  },
  {
    "id": "venue-65",
    "name": "SPR Sports Academy",
    "category": "sports",
    "city": "Chennai",
    "area": "Nolambur (Sriram Nagar Main Road)",
    "priceTier": 2,
    "rating": 4.8,
    "reviewCount": 90,
    "tags": [
      "Football Academy"
    ],
    "description": "Football coaching academy -- limited details available from sources, needs verification before going live.",
    "isLive": false,
    "photo": "https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-65-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-65-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-65-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-65-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-65-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": false
      }
    ]
  },
  {
    "id": "venue-66",
    "name": "Newel Sports Academy",
    "category": "sports",
    "city": "Chennai",
    "area": "Thiruverkadu (Govindaraj Nagar 3rd Street)",
    "priceTier": 2,
    "rating": 4.3,
    "reviewCount": 107,
    "tags": [
      "Football Academy"
    ],
    "description": "Football coaching academy -- limited details available from sources, needs verification before going live.",
    "isLive": false,
    "photo": "https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-66-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-66-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-66-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": false
      },
      {
        "id": "slot-66-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-66-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": true
      }
    ]
  },
  {
    "id": "venue-67",
    "name": "Leap Sports Academy",
    "category": "sports",
    "city": "Chennai",
    "area": "Padur (Srinivasa Nagar)",
    "priceTier": 2,
    "rating": 4.4,
    "reviewCount": 124,
    "tags": [
      "Football Academy"
    ],
    "description": "Football coaching academy -- limited details available from sources, needs verification before going live.",
    "isLive": false,
    "photo": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=800&q=80",
    "slots": [
      {
        "id": "slot-67-1",
        "time": "07:00 AM - 08:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-67-2",
        "time": "09:00 AM - 10:00 AM",
        "price": 800,
        "available": true
      },
      {
        "id": "slot-67-3",
        "time": "05:00 PM - 06:00 PM",
        "price": 1000,
        "available": true
      },
      {
        "id": "slot-67-4",
        "time": "07:00 PM - 08:00 PM",
        "price": 1200,
        "available": true
      },
      {
        "id": "slot-67-5",
        "time": "08:30 PM - 09:30 PM",
        "price": 1200,
        "available": false
      }
    ]
  }
];
