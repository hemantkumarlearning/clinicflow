const API_BASE = 'http://127.0.0.1:5000';

document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;

    const res = await fetch(`${API_BASE}/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });

    const data = await res.json();

    if (res.ok && data.access_token) {
        localStorage.setItem('accessToken', data.access_token);
        localStorage.setItem('userRole', data.role); 
        if (data.role === 'admin') {
            window.location.href = 'admin_dashboard.html';
        } else if (data.role === 'patient') {
            window.location.href = 'appointments.html';
        }
        else if (data.role === 'receptionist') {
            window.location.href = 'receptionist.html';
        }
        else {
            alert('Unknown role: ' + data.role);
        }
    } else {
    alert('Login failed');
    }
    
});
