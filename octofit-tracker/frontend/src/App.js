
import logo from '../public/octofitapp-small.png';

function App() {
  return (
    <div>
      <nav className="navbar navbar-expand-lg navbar-dark">
        <div className="container-fluid">
          <NavLink className="navbar-brand d-flex align-items-center" to="/">
            <img src={logo} alt="OctoFit Logo" className="octofit-logo me-2" />
            OctoFit Tracker
          </NavLink>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <NavLink className="nav-link" to="/activities">Activities</NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/leaderboard">Leaderboard</NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/teams">Teams</NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/users">Users</NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/workouts">Workouts</NavLink>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <div className="container mt-4">
        <Routes>
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/" element={
            <div className="card">
              <div className="card-body">
                <h1 className="display-4 mb-3">Welcome to OctoFit Tracker!</h1>
                <p className="lead">Track your fitness activities, join teams, view leaderboards, and more.</p>
                <a href="/activities" className="btn btn-primary me-2">View Activities</a>
                <a href="/leaderboard" className="btn btn-success me-2">Leaderboard</a>
                <a href="/teams" className="btn btn-info me-2">Teams</a>
                <a href="/users" className="btn btn-warning me-2">Users</a>
                <a href="/workouts" className="btn btn-secondary">Workouts</a>
              </div>
            </div>
          } />
        </Routes>
      </div>
    </div>
  );
}

export default App;
