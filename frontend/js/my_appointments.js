const API_BASE = 'http://127.0.0.1:5000';

document.addEventListener('DOMContentLoaded', () => {
    const token = localStorage.getItem('accessToken');
    const list = document.getElementById('appointments-list');

    if (!token) {
        alert('You must be logged in to view appointments.');
        window.location.href = 'login.html';
        return;
    }

    fetch(`${API_BASE}/appointments/patient`, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`
        }
    })
    .then(res => res.json())
    .then(data => {
        if (Array.isArray(data) && data.length > 0) {
        data.forEach(appt => {
            const li = document.createElement('li');
            const date = new Date(appt.date).toLocaleDateString();
            li.textContent = `Doctor ID: ${appt.doctor_id} | Date: ${date} | Reason: ${appt.reason} | Status: ${appt.status}`;
            list.appendChild(li);
        });
    } else {
        list.textContent = 'No appointments found.';
    }
    })
    .catch(err => {
        console.error('Error loading appointments:', err);
        list.textContent = 'Failed to load appointments.';
    });
});
