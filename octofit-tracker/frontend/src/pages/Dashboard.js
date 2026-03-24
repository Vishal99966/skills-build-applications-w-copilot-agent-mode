import React, { useState, useEffect, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../services/api';

const Dashboard = () => {
  const [user, setUser] = useState(null);
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('access_token');
    if (!token) {
      navigate('/login');
      return;
    }

    fetchDashboardData();
  }, [navigate]);

  const fetchDashboardData = useCallback(async () => {
    try {
      const [userResponse, statsResponse] = await Promise.all([
        api.get('/users/profile/'),
        api.get('/users/stats/')
      ]);

      setUser(userResponse.data);
      setStats(statsResponse.data);
    } catch (error) {
      console.error('Error fetching dashboard data:', error);
      if (error.response?.status === 401) {
        navigate('/login');
      }
    } finally {
      setLoading(false);
    }
  }, [navigate]);

  if (loading) {
    return (
      <div className="text-center">
        <div className="spinner-border" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
      </div>
    );
  }

  if (!user) {
    return <div>Please log in to view your dashboard.</div>;
  }

  return (
    <div>
      <h1 className="mb-4">Welcome back, {user.first_name}!</h1>

      <div className="row mb-4">
        <div className="col-md-8">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Your Stats</h5>
              {stats && (
                <div className="row">
                  <div className="col-md-3">
                    <div className="text-center">
                      <h3 className="text-primary">{stats.total_activities}</h3>
                      <p>Total Activities</p>
                    </div>
                  </div>
                  <div className="col-md-3">
                    <div className="text-center">
                      <h3 className="text-success">{stats.total_points}</h3>
                      <p>Total Points</p>
                    </div>
                  </div>
                  <div className="col-md-3">
                    <div className="text-center">
                      <h3 className="text-info">{stats.total_duration_minutes}min</h3>
                      <p>Total Duration</p>
                    </div>
                  </div>
                  <div className="col-md-3">
                    <div className="text-center">
                      <h3 className="text-warning">{stats.achievement_count}</h3>
                      <p>Achievements</p>
                    </div>
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
        <div className="col-md-4">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Quick Actions</h5>
              <div className="d-grid gap-2">
                <button className="btn btn-primary">Log New Activity</button>
                <button className="btn btn-outline-primary">View Activities</button>
                <button className="btn btn-outline-primary">Join Team</button>
                <button className="btn btn-outline-primary">View Leaderboard</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="row">
        <div className="col-md-6">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">This Week</h5>
              {stats && (
                <div>
                  <p>Activities: {stats.this_week.activities_count}</p>
                  <p>Points Earned: {stats.this_week.points_earned}</p>
                </div>
              )}
            </div>
          </div>
        </div>
        <div className="col-md-6">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Recent Achievements</h5>
              <p>No recent achievements to display.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;