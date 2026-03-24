# OctoFit Tracker - Analysis and User Stories

## 1. Executive Summary

The OctoFit Tracker is a fitness tracking application designed to combat declining physical activity among Mergington High School students. By gamifying fitness tracking and incorporating social competition elements, the app aims to create positive peer pressure and maintain student engagement in physical activities beyond required PE classes.

## 2. Stakeholder Analysis

### 2.1 Primary Stakeholders

#### Paul Octo (Physical Education Teacher)
- **Role**: Product owner, domain expert
- **Goals**:
  - Monitor student physical activity levels
  - Identify students needing additional motivation
  - Create engaging fitness challenges
  - Track overall class fitness trends
- **Concerns**:
  - Student privacy and data protection
  - Age-appropriate content and features
  - Ease of use for non-technical users

#### Jessica Cat (IT Department Head)
- **Role**: Technical lead, infrastructure provider
- **Goals**:
  - Ensure system security and compliance
  - Maintain scalable and maintainable codebase
  - Leverage modern development practices
- **Concerns**:
  - Data security and FERPA compliance
  - System performance and reliability
  - Integration with school systems

#### Students (End Users)
- **Demographics**: Ages 14-18, mixed fitness levels
- **Goals**:
  - Easy fitness tracking
  - Social recognition for achievements
  - Fun and engaging experience
  - Personalized fitness guidance
- **Concerns**:
  - Privacy of personal fitness data
  - Fair competition
  - Not being judged for fitness levels

### 2.2 Secondary Stakeholders

#### School Administration
- Monitor overall student health trends
- Ensure compliance with educational policies

#### Parents
- Monitor children's activity levels
- Support healthy lifestyle choices

## 3. User Personas

### 3.1 Sarah - The Casual Exerciser
**Age**: 16
**Fitness Level**: Beginner
**Background**: Sarah enjoys walking and occasional yoga but struggles with motivation for consistent exercise.
**Goals**: Build healthy habits, earn recognition for small achievements
**Pain Points**: Intimidated by advanced fitness tracking, wants simple interface
**Tech Savvy**: Moderate - uses social media daily

### 3.2 Mike - The Competitive Athlete
**Age**: 17
**Fitness Level**: Advanced
**Background**: Runs track team, lifts weights regularly
**Goals**: Compete with peers, track detailed performance metrics, lead team challenges
**Pain Points**: Wants advanced features, frustrated by oversimplified apps
**Tech Savvy**: High - uses fitness apps and wearables

### 3.3 Coach Paul - The Educator
**Age**: 45
**Fitness Level**: Intermediate
**Background**: PE teacher with 8+ years experience
**Goals**: Monitor class progress, create motivational challenges, identify struggling students
**Pain Points**: Limited time for manual tracking, needs automated reports
**Tech Savvy**: Basic - comfortable with common software

## 4. Functional Requirements

### 4.1 User Management
- **FR-1.1**: Users shall be able to create accounts with email, username, and password
- **FR-1.2**: Users shall be able to log in and log out securely
- **FR-1.3**: Users shall be able to update their profile information (name, grade, fitness level)
- **FR-1.4**: Users shall be able to reset passwords via email
- **FR-1.5**: System shall support role-based access (student, teacher)

### 4.2 Activity Tracking
- **FR-2.1**: Users shall be able to log activities with type, duration, and optional distance
- **FR-2.2**: System shall automatically calculate points and estimated calories burned
- **FR-2.3**: Users shall be able to view their activity history
- **FR-2.4**: Users shall be able to edit or delete their logged activities
- **FR-2.5**: System shall support multiple activity types (running, walking, strength training, cycling, yoga)

### 4.3 Social Features
- **FR-3.1**: Users shall be able to create and join teams
- **FR-3.2**: Team captains shall be able to manage team membership
- **FR-3.3**: Users shall be able to view team statistics and member activities
- **FR-3.4**: System shall display team and individual leaderboards

### 4.4 Gamification
- **FR-4.1**: System shall award achievement badges for milestones
- **FR-4.2**: Users shall earn points for completed activities
- **FR-4.3**: System shall track activity streaks (consecutive days)
- **FR-4.4**: Users shall be able to view their earned badges and achievements

### 4.5 Challenges and Competitions
- **FR-5.1**: Teachers shall be able to create fitness challenges
- **FR-5.2**: Users shall be able to join active challenges
- **FR-5.3**: System shall track challenge progress and declare winners
- **FR-5.4**: Challenges shall support individual and team participation

### 4.6 Reporting and Analytics
- **FR-6.1**: Users shall be able to view personal fitness statistics
- **FR-6.2**: Teachers shall be able to view class-wide analytics
- **FR-6.3**: System shall generate reports on student participation and progress
- **FR-6.4**: Teachers shall be able to identify students with declining activity

### 4.7 Personalized Recommendations
- **FR-7.1**: System shall suggest activities based on user's fitness level
- **FR-7.2**: System shall provide workout suggestions based on goals
- **FR-7.3**: Users shall be able to set fitness goals and track progress

## 5. Non-Functional Requirements

### 5.1 Performance
- **NFR-1.1**: Page load times shall be under 2 seconds
- **NFR-1.2**: API response times shall be under 500ms for 95% of requests
- **NFR-1.3**: System shall support up to 1000 concurrent users
- **NFR-1.4**: Mobile interface shall be responsive on devices 320px and wider

### 5.2 Security
- **NFR-2.1**: All user data shall be encrypted in transit and at rest
- **NFR-2.2**: System shall comply with FERPA privacy regulations
- **NFR-2.3**: Passwords shall be hashed using industry-standard algorithms
- **NFR-2.4**: Session tokens shall expire after 24 hours of inactivity
- **NFR-2.5**: Failed login attempts shall be rate-limited

### 5.3 Usability
- **NFR-3.1**: Interface shall follow WCAG 2.1 AA accessibility guidelines
- **NFR-3.2**: Activity logging shall take no more than 30 seconds
- **NFR-3.3**: Navigation shall be consistent across all screens
- **NFR-3.4**: Error messages shall be clear and actionable

### 5.4 Reliability
- **NFR-4.1**: System shall have 99.5% uptime
- **NFR-4.2**: Data backup shall occur daily with 30-day retention
- **NFR-4.3**: System shall gracefully handle database connection failures
- **NFR-4.4**: All user data shall be recoverable in case of system failure

### 5.5 Maintainability
- **NFR-5.1**: Code shall follow PEP 8 style guidelines
- **NFR-5.2**: Test coverage shall be at least 80%
- **NFR-5.3**: Documentation shall be updated with each feature release
- **NFR-5.4**: System shall support rolling deployments without downtime

## 6. User Stories

### 6.1 Authentication & Profile Management

**US-1.1**: As a new student, I want to create an account so that I can start tracking my fitness activities.
- **Acceptance Criteria**:
  - Form includes fields for email, username, password, grade level
  - Password strength requirements are enforced
  - Email verification is sent upon registration
  - Error messages guide user through corrections

**US-1.2**: As a returning user, I want to log in securely so that I can access my fitness data.
- **Acceptance Criteria**:
  - Login form accepts email/username and password
  - "Remember me" option available
  - Invalid credentials show appropriate error
  - Successful login redirects to dashboard

**US-1.3**: As a user, I want to update my profile so that my information stays current.
- **Acceptance Criteria**:
  - Editable fields: name, grade, fitness level, profile picture
  - Changes save immediately
  - Validation prevents invalid data
  - Success message confirms update

### 6.2 Activity Logging

**US-2.1**: As an active student, I want to log my workout so that I can track my progress.
- **Acceptance Criteria**:
  - Activity types: running, walking, strength, cycling, yoga
  - Required: type, duration
  - Optional: distance, notes, photos
  - Points calculated automatically
  - Activity appears in history immediately

**US-2.2**: As a user, I want to view my activity history so that I can see my fitness journey.
- **Acceptance Criteria**:
  - List view with date, type, duration, points
  - Sortable by date, type, points
  - Filterable by time period
  - Pagination for large lists
  - Total statistics displayed

**US-2.3**: As a user, I want to edit my logged activities so that I can correct mistakes.
- **Acceptance Criteria**:
  - Edit form pre-populated with existing data
  - All fields editable except date created
  - Points recalculated on save
  - Confirmation dialog for changes

### 6.3 Social Features

**US-3.1**: As a student, I want to create a team so that I can compete with friends.
- **Acceptance Criteria**:
  - Team creation form with name and description
  - Creator becomes team captain
  - Team appears in available teams list
  - Captain can set team goals

**US-3.2**: As a student, I want to join a team so that I can participate in group challenges.
- **Acceptance Criteria**:
  - Browse teams with member count and total points
  - Join request sent to captain
  - Notification when request approved/denied
  - Team membership reflected in profile

**US-3.3**: As a team member, I want to view team progress so that I can see how we're doing.
- **Acceptance Criteria**:
  - Team dashboard shows member list with individual points
  - Total team points displayed
  - Recent team activities listed
  - Team ranking on leaderboard

### 6.4 Gamification

**US-4.1**: As a motivated student, I want to earn badges so that I feel accomplished.
- **Acceptance Criteria**:
  - Badges for: first workout, 7-day streak, 100 points earned
  - Badge notifications when earned
  - Badge gallery in profile
  - Badge progress indicators for upcoming achievements

**US-4.2**: As a competitive student, I want to see leaderboards so that I can compare my progress.
- **Acceptance Criteria**:
  - Individual leaderboard by total points
  - Team leaderboard by team points
  - Filterable by time period (week, month, all-time)
  - User's rank highlighted
  - Top 10 displayed with avatars

### 6.5 Teacher Features

**US-5.1**: As a teacher, I want to create challenges so that I can motivate students.
- **Acceptance Criteria**:
  - Challenge creation form with title, description, dates, target
  - Support for individual and team challenges
  - Automatic winner determination
  - Challenge appears in student dashboards

**US-5.2**: As a teacher, I want to view class analytics so that I can identify trends.
- **Acceptance Criteria**:
  - Dashboard with participation rates
  - Individual student activity summaries
  - Class-wide fitness level distribution
  - Exportable reports in CSV/PDF format

**US-5.3**: As a teacher, I want to monitor at-risk students so that I can provide support.
- **Acceptance Criteria**:
  - Alert system for students with declining activity
  - Individual student detail views
  - Contact information for follow-up
  - Progress tracking over time

## 7. Use Cases

### 7.1 Primary Use Cases

#### Use Case 1: Daily Activity Logging
**Actor**: Student
**Preconditions**: User is logged in
**Main Flow**:
1. User navigates to activity logging screen
2. User selects activity type
3. User enters duration and optional details
4. System calculates points and calories
5. User submits activity
6. System saves activity and updates user totals
7. User receives confirmation and sees updated dashboard

#### Use Case 2: Team Formation
**Actor**: Student
**Preconditions**: User is logged in
**Main Flow**:
1. User navigates to teams section
2. User selects "Create Team"
3. User enters team name and description
4. System creates team with user as captain
5. User invites friends via username or email
6. Invited users receive notifications
7. Users accept invitations and join team

#### Use Case 3: Challenge Participation
**Actor**: Student
**Preconditions**: Active challenge exists, user is logged in
**Main Flow**:
1. User views available challenges
2. User selects challenge to join
3. System adds user to challenge participants
4. User logs activities during challenge period
5. System tracks progress toward challenge goals
6. At challenge end, system determines winners
7. Winners receive badges and notifications

#### Use Case 4: Teacher Monitoring
**Actor**: Teacher
**Preconditions**: Teacher account with elevated permissions
**Main Flow**:
1. Teacher logs in to admin dashboard
2. Teacher views class participation statistics
3. Teacher identifies students with low activity
4. Teacher generates individual student reports
5. Teacher creates targeted challenges for underperforming students

## 8. Business Rules

### 8.1 Points System
- **BR-1.1**: Running activities earn 2 points per minute
- **BR-1.2**: Walking activities earn 1 point per minute
- **BR-1.3**: Strength training earns 3 points per minute
- **BR-1.4**: Distance bonus: 0.5 points per kilometer for applicable activities
- **BR-1.5**: Fitness level multiplier: Beginner (1.0x), Intermediate (1.2x), Advanced (1.5x)

### 8.2 Achievement System
- **BR-2.1**: First Workout: Awarded after logging initial activity
- **BR-2.2**: Streak badges: 7, 14, 30 consecutive days
- **BR-2.3**: Volume badges: 50, 100, 500 total points earned
- **BR-2.4**: Team badges: First team join, Team victory

### 8.3 Privacy Rules
- **BR-3.1**: Student data visible only to teachers and team members
- **BR-3.2**: Individual activity details private unless shared
- **BR-3.3**: Leaderboards show usernames only, no personal information
- **BR-3.4**: Teachers can view aggregated class data only

### 8.4 Challenge Rules
- **BR-4.1**: Challenges run for minimum 7 days, maximum 30 days
- **BR-4.2**: Individual challenges based on personal points earned
- **BR-4.3**: Team challenges based on combined team points
- **BR-4.4**: Ties broken by total activities logged

## 9. Constraints and Assumptions

### 9.1 Technical Constraints
- Must run on school-provided devices and networks
- Limited to web-based interface (no native mobile apps initially)
- Must integrate with existing school authentication systems (future)
- Database must be hosted on school-approved infrastructure

### 9.2 Business Constraints
- Development must not interfere with regular school operations
- Must comply with COPPA and FERPA regulations
- Initial rollout limited to Mergington High School
- Budget constraints limit third-party service integrations

### 9.3 Assumptions
- Students have access to smartphones or computers for app use
- Teachers have basic computer literacy
- School provides technical support for deployment
- Parent permission obtained for student participation
- Internet connectivity available during school hours

## 10. Risk Analysis

### 10.1 High Risk Items
- **Privacy Compliance**: Risk of FERPA violations
  - Mitigation: Regular security audits, data minimization
- **User Adoption**: Students may not engage with the app
  - Mitigation: User testing, iterative design, teacher involvement
- **Technical Performance**: System slowdowns with high concurrent users
  - Mitigation: Performance testing, scalable architecture

### 10.2 Medium Risk Items
- **Data Accuracy**: Inaccurate fitness calculations
  - Mitigation: Validation against established formulas, user feedback
- **Competition Fairness**: Advanced users dominating leaderboards
  - Mitigation: Level-based point multipliers, diverse challenge types

### 10.3 Low Risk Items
- **Feature Creep**: Adding too many features
  - Mitigation: Strict requirement prioritization, phased releases

## 11. Success Metrics

### 11.1 User Engagement Metrics
- Daily active users: Target 60% of enrolled students
- Average activities logged per user per week: Target 3-4
- Team participation rate: Target 40% of users in teams
- Challenge completion rate: Target 70% of participants

### 11.2 Technical Metrics
- System uptime: Target 99.5%
- Average response time: Target <500ms
- User-reported bugs: Target <5 per month
- Test coverage: Target 80%

### 11.3 Educational Impact Metrics
- Student self-reported exercise frequency increase: Target 25%
- Teacher-reported improvement in class participation: Target positive feedback
- Achievement badge redemption rate: Target 80%
- Long-term usage retention: Target 50% after 6 months

This analysis document provides the foundation for the OctoFit Tracker development, ensuring all features align with educational goals and technical requirements.