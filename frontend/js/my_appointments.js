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
    .then(res => {
        if (!res.ok) throw new Error("Network response was not ok");
        return res.json();
    })
    .then(data => {
        if (Array.isArray(data) && data.length > 0) {
            data.forEach(appt => {
                const li = document.createElement('li');
                const date = new Date(appt.date).toLocaleString();

                li.innerHTML = `
                    <div class="appointment-card">
                        <h3>Dr. ${appt.doctor_name || appt.doctor_id}</h3>
                        <p><strong>Date:</strong> ${date}</p>
                        <p><strong>Reason:</strong> ${appt.reason}</p>
                        <p><strong>Status:</strong> <span class="status ${appt.status.toLowerCase()}">${appt.status}</span></p>
                    </div>
                `;
                list.appendChild(li);
            });
        } else {
            list.innerHTML = '<li class="empty">No appointments found.</li>';
        }
    })
    .catch(err => {
        console.error('Error loading appointments:', err);
        list.innerHTML = '<li class="error">Failed to load appointments.</li>';
    });
});
function logout() {
    localStorage.removeItem('accessToken');
    window.location.href = 'login.html';
}

function appointment() {
    window.location.href = 'appointments.html';
}