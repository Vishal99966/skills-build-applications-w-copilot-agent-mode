import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="text-center">
      <div className="hero-section py-5">
        <h1 className="display-4 mb-4">Welcome to OctoFit Tracker</h1>
        <p className="lead mb-4">
          Track your fitness activities, join teams, and compete with friends at Mergington High School!
        </p>
        <div className="row justify-content-center">
          <div className="col-md-8">
            <div className="card shadow">
              <div className="card-body">
                <h5 className="card-title">Get Started Today</h5>
                <p className="card-text">
                  Join thousands of students who are making fitness fun and staying active together.
                </p>
                <div className="d-flex justify-content-center gap-3">
                  <Link to="/register" className="btn btn-primary btn-lg">
                    Sign Up Free
                  </Link>
                  <Link to="/login" className="btn btn-outline-primary btn-lg">
                    Login
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="features-section py-5">
        <h2 className="mb-4">Features</h2>
        <div className="row">
          <div className="col-md-4 mb-4">
            <div className="card h-100">
              <div className="card-body text-center">
                <h5 className="card-title">📊 Activity Tracking</h5>
                <p className="card-text">
                  Log your workouts, track progress, and earn points for staying active.
                </p>
              </div>
            </div>
          </div>
          <div className="col-md-4 mb-4">
            <div className="card h-100">
              <div className="card-body text-center">
                <h5 className="card-title">👥 Team Competition</h5>
                <p className="card-text">
                  Join teams, compete in challenges, and climb the leaderboards together.
                </p>
              </div>
            </div>
          </div>
          <div className="col-md-4 mb-4">
            <div className="card h-100">
              <div className="card-body text-center">
                <h5 className="card-title">🏆 Achievements</h5>
                <p className="card-text">
                  Unlock badges, track streaks, and celebrate your fitness milestones.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;