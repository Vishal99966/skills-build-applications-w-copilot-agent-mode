# OctoFit Tracker - Detailed Design Document

## 1. Introduction

### 1.1 Purpose
The OctoFit Tracker is a fitness tracking application designed specifically for Mergington High School students to promote physical activity, healthy competition, and personalized fitness guidance. The app addresses the declining physical activity levels among students outside of required PE classes by making fitness tracking engaging and socially interactive.

### 1.2 Scope
The application will include:
- User authentication and profiles
- Activity logging and tracking (running, walking, strength training)
- Team creation and management
- Competitive leaderboard
- Personalized workout suggestions
- Achievement badges and gamification elements
- Teacher monitoring and reporting capabilities

### 1.3 Target Users
- Primary: High school students (ages 14-18)
- Secondary: Physical education teachers for monitoring and guidance

## 2. System Architecture

### 2.1 Technology Stack
- **Frontend**: React.js with modern hooks and context API
- **Backend**: Python Django REST Framework
- **Database**: MongoDB with Djongo ORM
- **Authentication**: Django Allauth with social login capabilities
- **API Communication**: RESTful APIs with CORS support
- **Development Environment**: GitHub Codespaces

### 2.2 Architecture Diagram
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React Frontend│◄──►│ Django REST API │◄──►│    MongoDB      │
│                 │    │                 │    │                 │
│ - User Interface│    │ - Business Logic│    │ - User Data     │
│ - Activity Forms│    │ - Authentication│    │ - Activities    │
│ - Dashboards    │    │ - Data Validation│    │ - Teams         │
│ - Leaderboards  │    │ - API Endpoints │    │ - Achievements  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### 2.3 Component Structure

#### Frontend Components
```
src/
├── components/
│   ├── auth/
│   │   ├── LoginForm.js
│   │   ├── RegisterForm.js
│   │   └── Profile.js
│   ├── activities/
│   │   ├── ActivityForm.js
│   │   ├── ActivityList.js
│   │   └── ActivityDetail.js
│   ├── teams/
│   │   ├── TeamCreate.js
│   │   ├── TeamJoin.js
│   │   └── TeamDashboard.js
│   ├── leaderboard/
│   │   ├── Leaderboard.js
│   │   └── AchievementBadges.js
│   └── dashboard/
│       ├── StudentDashboard.js
│       └── TeacherDashboard.js
├── services/
│   ├── api.js
│   └── auth.js
└── context/
    ├── AuthContext.js
    └── ActivityContext.js
```

#### Backend Structure
```
backend/
├── octofit_tracker/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── users/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   └── urls.py
│   ├── activities/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   └── urls.py
│   ├── teams/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   └── urls.py
│   └── achievements/
│       ├── models.py
│       ├── views.py
│       ├── serializers.py
│       └── urls.py
└── requirements.txt
```

## 3. Database Design

### 3.1 MongoDB Collections

#### Users Collection
```javascript
{
  _id: ObjectId,
  username: String,
  email: String,
  first_name: String,
  last_name: String,
  date_of_birth: Date,
  grade_level: String,
  profile_picture: String,
  fitness_level: String, // beginner, intermediate, advanced
  total_points: Number,
  created_at: Date,
  updated_at: Date
}
```

#### Activities Collection
```javascript
{
  _id: ObjectId,
  user_id: ObjectId,
  activity_type: String, // running, walking, strength, cycling, etc.
  duration: Number, // in minutes
  distance: Number, // in km (optional)
  calories_burned: Number,
  points_earned: Number,
  notes: String,
  date_logged: Date,
  created_at: Date
}
```

#### Teams Collection
```javascript
{
  _id: ObjectId,
  name: String,
  description: String,
  captain_id: ObjectId,
  member_ids: [ObjectId],
  team_points: Number,
  created_at: Date,
  updated_at: Date
}
```

#### Achievements Collection
```javascript
{
  _id: ObjectId,
  user_id: ObjectId,
  achievement_type: String, // first_workout, streak_7_days, etc.
  title: String,
  description: String,
  points_awarded: Number,
  badge_image: String,
  unlocked_at: Date
}
```

#### Challenges Collection
```javascript
{
  _id: ObjectId,
  title: String,
  description: String,
  challenge_type: String, // individual, team
  start_date: Date,
  end_date: Date,
  target_metric: String, // total_distance, total_points, etc.
  target_value: Number,
  participants: [ObjectId],
  winners: [ObjectId],
  created_at: Date
}
```

## 4. API Design

### 4.1 Authentication Endpoints
- `POST /api/auth/login/` - User login
- `POST /api/auth/register/` - User registration
- `POST /api/auth/logout/` - User logout
- `GET /api/auth/user/` - Get current user info

### 4.2 User Management Endpoints
- `GET /api/users/profile/` - Get user profile
- `PUT /api/users/profile/` - Update user profile
- `GET /api/users/{id}/stats/` - Get user statistics

### 4.3 Activity Endpoints
- `GET /api/activities/` - List user activities
- `POST /api/activities/` - Create new activity
- `GET /api/activities/{id}/` - Get activity details
- `PUT /api/activities/{id}/` - Update activity
- `DELETE /api/activities/{id}/` - Delete activity

### 4.4 Team Endpoints
- `GET /api/teams/` - List available teams
- `POST /api/teams/` - Create new team
- `GET /api/teams/{id}/` - Get team details
- `PUT /api/teams/{id}/` - Update team
- `POST /api/teams/{id}/join/` - Join team
- `POST /api/teams/{id}/leave/` - Leave team

### 4.5 Leaderboard Endpoints
- `GET /api/leaderboard/individual/` - Individual leaderboard
- `GET /api/leaderboard/teams/` - Team leaderboard
- `GET /api/leaderboard/achievements/` - Achievement leaderboard

### 4.6 Challenge Endpoints
- `GET /api/challenges/` - List active challenges
- `GET /api/challenges/{id}/` - Get challenge details
- `POST /api/challenges/{id}/participate/` - Join challenge

## 5. Frontend Design

### 5.1 User Interface Design Principles
- **Teen-friendly design**: Bright colors, clean layout, intuitive navigation
- **Mobile-first approach**: Responsive design for phones and tablets
- **Accessibility**: WCAG 2.1 AA compliance
- **Performance**: Lazy loading, code splitting, optimized images

### 5.2 Key Screens

#### Login/Register Screen
- Simple form with email/username and password
- Option for "Remember me"
- Link to registration for new users

#### Dashboard
- Welcome message with user's name
- Today's activity summary
- Quick action buttons (Log Activity, View Teams, Check Leaderboard)
- Recent achievements
- Upcoming challenges

#### Activity Logging
- Activity type selection (dropdown)
- Duration input (time picker)
- Distance input (for applicable activities)
- Notes field (optional)
- Photo upload option
- Auto-calculation of points and calories

#### Team Management
- Browse available teams
- Create new team (captain role)
- Join existing team
- View team members and stats
- Team chat functionality (future feature)

#### Leaderboard
- Individual ranking table
- Team ranking table
- Achievement showcase
- Filtering by time period (week, month, all-time)

### 5.3 State Management
- React Context for global state (authentication, user data)
- Local component state for forms and UI interactions
- Redux Toolkit for complex state management (if needed)

## 6. Backend Design

### 6.1 Django Apps Structure
- **users**: User management, profiles, authentication
- **activities**: Activity logging, validation, calculations
- **teams**: Team creation, membership management
- **achievements**: Badge system, achievement tracking
- **challenges**: Challenge management, winner determination
- **reports**: Analytics and reporting for teachers

### 6.2 Business Logic

#### Points Calculation System
```python
def calculate_activity_points(activity_type, duration, distance=None, user_level=None):
    base_points = {
        'running': 2,
        'walking': 1,
        'cycling': 1.5,
        'strength': 3,
        'yoga': 1.5
    }
    
    points = base_points.get(activity_type, 1) * duration
    
    # Bonus for distance-based activities
    if distance and activity_type in ['running', 'walking', 'cycling']:
        points += distance * 0.5
    
    # Level multiplier
    level_multiplier = {'beginner': 1.0, 'intermediate': 1.2, 'advanced': 1.5}
    points *= level_multiplier.get(user_level, 1.0)
    
    return round(points, 2)
```

#### Achievement System
- **Streak achievements**: 7-day, 14-day, 30-day activity streaks
- **Volume achievements**: Total distance, total activities
- **Team achievements**: Team participation, team victories
- **Personal records**: Best single activity, most active month

### 6.3 Security Considerations
- JWT token authentication
- Password hashing with Django's auth system
- Input validation and sanitization
- Rate limiting on API endpoints
- CORS configuration for frontend access
- Data encryption for sensitive information

## 7. Deployment and Infrastructure

### 7.1 Development Environment
- GitHub Codespaces for consistent development
- Python virtual environment
- MongoDB local instance or cloud service

### 7.2 Production Deployment
- Docker containerization
- Cloud hosting (AWS, Google Cloud, or Azure)
- CI/CD pipeline with GitHub Actions
- Environment-specific configurations

### 7.3 Monitoring and Analytics
- Error logging and monitoring
- User activity analytics
- Performance metrics
- Teacher reporting dashboard

## 8. Testing Strategy

### 8.1 Unit Testing
- Django test framework for backend
- Jest/React Testing Library for frontend
- Test coverage target: 80%+

### 8.2 Integration Testing
- API endpoint testing
- Database integration tests
- End-to-end user flows

### 8.3 User Acceptance Testing
- Teacher validation of features
- Student beta testing
- Usability testing

## 9. Future Enhancements

### Phase 2 Features
- Wearable device integration (Fitbit, Apple Watch)
- Social features (activity sharing, comments)
- Advanced analytics and insights
- Parent portal for monitoring
- Integration with school systems

### Phase 3 Features
- AI-powered workout recommendations
- Virtual coaching sessions
- Tournament system
- Mobile app (React Native)
- Offline functionality

## 10. Conclusion

The OctoFit Tracker represents a comprehensive solution to address declining physical activity among high school students. By combining gamification, social features, and teacher oversight, the app creates an engaging environment that encourages consistent fitness habits. The chosen technology stack provides scalability, maintainability, and a modern user experience suitable for the target demographic.

This detailed design document serves as the blueprint for implementation, ensuring all stakeholders understand the system architecture, features, and development approach.