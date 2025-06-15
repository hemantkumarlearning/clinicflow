const API_BASE = 'http://127.0.0.1:5000'; // Change this to your backend URL
const token = localStorage.getItem('accessToken'); // Assume JWT is stored after login

async function loadPendingAppointments() {
    try {
        const res = await fetch(`${API_BASE}/appointments/pending`, {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        if (!res.ok) {
            throw new Error('Failed to fetch appointments');
        }

        const appointments = await res.json();
        const tbody = document.getElementById('appointmentsBody');
        tbody.innerHTML = '';

        appointments.forEach(app => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${app.id}</td>
                <td>${app.patient_id}</td>
                <td>${app.doctor_id}</td>
                <td>${app.date}</td>
                <td>${app.reason}</td>
                <td><button onclick="confirmAppointment(${app.id})">Confirm</button></td>
            `;
            tbody.appendChild(row);
        });
    } catch (err) {
        alert(err.message);
    }
}

async function confirmAppointment(id) {
    if (!confirm("Are you sure you want to confirm this appointment?")) return;

    try {
        const res = await fetch(`${API_BASE}/appointments/${id}/confirm`, {
            method: 'PATCH',
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        if (!res.ok) {
            const error = await res.json();
            throw new Error(error.msg || 'Failed to confirm appointment');
        }

        alert("Appointment confirmed!");
        loadPendingAppointments(); // Reload after confirmation
    } catch (err) {
        alert(err.message);
    }
}
function logout() {
    localStorage.removeItem('accessToken');
    window.location.href = 'login.html';
}
// Initial load
loadPendingAppointments();
