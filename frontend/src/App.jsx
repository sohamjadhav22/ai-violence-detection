import { useEffect, useState } from 'react';
import { Link, Route, Routes } from 'react-router-dom';
import axios from 'axios';

const api = axios.create({ baseURL: 'http://localhost:8000/api' });

function Dashboard() {
  const [incidents, setIncidents] = useState([]);
  useEffect(() => {
    api.get('/incidents').then((res) => setIncidents(res.data));
  }, []);

  return (
    <div className="min-h-screen bg-slate-950 p-8 text-slate-100">
      <div className="mb-8 flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-semibold">Violence Detection Dashboard</h1>
          <p className="text-slate-400">Real-time CCTV monitoring and incident response</p>
        </div>
      </div>

      <div className="grid gap-4 md:grid-cols-3">
        <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
          <p className="text-sm text-slate-400">Live Cameras</p>
          <p className="mt-2 text-3xl font-bold">4</p>
        </div>
        <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
          <p className="text-sm text-slate-400">Incidents</p>
          <p className="mt-2 text-3xl font-bold">{incidents.length}</p>
        </div>
        <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
          <p className="text-sm text-slate-400">Alerts</p>
          <p className="mt-2 text-3xl font-bold">2</p>
        </div>
      </div>

      <div className="mt-8 rounded-xl border border-slate-800 bg-slate-900 p-6">
        <h2 className="text-xl font-semibold">Recent Incidents</h2>
        <ul className="mt-4 space-y-3">
          {incidents.map((incident) => (
            <li key={incident.id} className="rounded-lg border border-slate-800 bg-slate-950 p-4">
              <div className="flex items-center justify-between">
                <span className="font-medium">{incident.incident_type}</span>
                <span className="text-sm text-red-400">{incident.confidence.toFixed(2)}</span>
              </div>
              <p className="mt-1 text-sm text-slate-400">Camera {incident.camera_id} • {incident.description}</p>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default function App() {
  return (
    <div>
      <nav className="border-b border-slate-800 bg-slate-900 px-8 py-4">
        <div className="flex items-center justify-between">
          <Link to="/" className="text-lg font-semibold text-white">Violence Detection</Link>
          <div className="space-x-4 text-sm text-slate-300">
            <Link to="/">Dashboard</Link>
            <Link to="/cameras">Cameras</Link>
          </div>
        </div>
      </nav>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/cameras" element={<div className="p-8 text-slate-100">Camera management coming soon.</div>} />
      </Routes>
    </div>
  );
}
