# OctoFit Tracker

A comprehensive fitness tracking application designed for Mergington High School students to promote physical activity through gamification and social competition.

## Features

- **User Authentication**: Secure registration and login system
- **Activity Tracking**: Log various fitness activities with automatic point calculation
- **Team Management**: Create and join teams for group competitions
- **Leaderboards**: Individual and team ranking systems
- **Achievements**: Badge system for milestones and streaks
- **Challenges**: Teacher-created fitness challenges
- **Analytics**: Comprehensive reporting for teachers

## Technology Stack

- **Backend**: Django REST Framework with MongoDB
- **Frontend**: React.js with Bootstrap
- **Authentication**: JWT tokens
- **Database**: MongoDB with Djongo ORM

## Project Structure

```
octofit-tracker/
├── backend/                 # Django backend
│   ├── octofit_tracker/     # Main Django project
│   ├── users/              # User management app
│   ├── activities/         # Activity tracking app
│   ├── teams/              # Team management app
│   ├── achievements/       # Achievement system app
│   ├── challenges/         # Challenge management app
│   └── requirements.txt    # Python dependencies
└── frontend/               # React frontend
    ├── src/
    │   ├── components/     # Reusable components
    │   ├── pages/         # Page components
    │   └── services/      # API services
    └── public/            # Static assets
```

## Setup Instructions

### Prerequisites

- Python 3.8+
- Node.js 14+
- MongoDB
- Git

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd octofit-tracker/backend
   ```

2. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MongoDB:**
   - Ensure MongoDB is running on localhost:27017
   - Or update `DATABASES` in `settings.py` for your MongoDB configuration

5. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start development server:**
   ```bash
   python manage.py runserver
   ```
   The backend will be available at http://localhost:8000

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd octofit-tracker/frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start development server:**
   ```bash
   npm start
   ```
   The frontend will be available at http://localhost:3000

### Environment Configuration

Create a `.env` file in the frontend directory for API configuration:

```env
REACT_APP_API_BASE_URL=http://localhost:8000
```

## API Documentation

### Authentication Endpoints

- `POST /api/auth/login/` - User login
- `POST /api/auth/registration/` - User registration
- `POST /api/auth/logout/` - User logout

### User Management

- `GET /api/users/profile/` - Get user profile
- `PUT /api/users/profile/` - Update user profile
- `GET /api/users/stats/` - Get user statistics

### Activity Tracking

- `GET /api/activities/` - List user activities
- `POST /api/activities/` - Create new activity
- `GET /api/activities/{id}/` - Get activity details
- `PUT /api/activities/{id}/` - Update activity
- `DELETE /api/activities/{id}/` - Delete activity

## Development Workflow

1. **Phase 1**: Core Authentication (User Registration, Login, Profile)
2. **Phase 2**: Activity Tracking Core (Log, View, Edit activities)
3. **Phase 3**: Gamification (Badge system)
4. **Phase 4**: Social Features (Team creation/management)
5. **Phase 5**: Competition (Leaderboards)
6. **Phase 6**: Teacher Tools (Challenges, Analytics, Monitoring)

## Testing

### Backend Testing
```bash
cd octofit-tracker/backend
python manage.py test
```

### Frontend Testing
```bash
cd octofit-tracker/frontend
npm test
```

## Deployment

### Backend Deployment
1. Set `DEBUG = False` in settings.py
2. Configure production database
3. Set up proper CORS settings
4. Use a production WSGI server (gunicorn)

### Frontend Deployment
1. Build production bundle:
   ```bash
   npm run build
   ```
2. Serve static files from the `build` directory
3. Configure API base URL for production

## Contributing

1. Follow the development plan phases
2. Write tests for new features
3. Ensure code follows PEP 8 (backend) and ESLint (frontend) standards
4. Update documentation for API changes

## License

This project is developed for educational purposes at Mergington High School.