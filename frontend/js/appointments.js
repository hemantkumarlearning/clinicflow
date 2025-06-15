const API_BASE = 'http://127.0.0.1:5000';

document.addEventListener('DOMContentLoaded', () => {
    const token = localStorage.getItem('accessToken');
    if (!token) {
        alert('You must be logged in to view this page.');
        window.location.href = 'login.html';
        return;
    }

    const doctorSelect = document.getElementById('doctor-select');
    const form = document.getElementById('appointment-form');

    // Fetch doctors and populate the dropdown
    async function loadDoctors() {
        try {
            const res = await fetch(`${API_BASE}/doctors`, {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            });

            const data = await res.json();

            if (res.ok) {
                data.doctors.forEach(doctor => {
                    const option = document.createElement('option');
                    option.value = doctor.id;
                    option.textContent = `${doctor.name} (${doctor.specialty})`;
                    doctorSelect.appendChild(option);
                });
            } else {
                alert(data.msg || 'Failed to load doctors');
            }

        } catch (err) {
            console.error('Error fetching doctors:', err);
            alert('Failed to load doctors');
        }
    }

    loadDoctors();

    // Appointment booking logic
    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const doctorId = doctorSelect.value;
        const date = document.getElementById('appointment-date').value;
        const reason = document.getElementById('reason').value;

        try {
            const res = await fetch(`${API_BASE}/appointments`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({
                    doctor_id: parseInt(doctorId),
                    date,
                    reason
                })
            });

            const data = await res.json();

            if (res.ok) {
                alert('Appointment booked successfully!');
                window.location.href = 'my_appointments.html';
            } else {
                alert(data.msg || 'Failed to book appointment');
            }

        } catch (err) {
            console.error(err);
            alert('An error occurred while booking the appointment');
        }
    });

    const viewBtn = document.getElementById('view-appointments-btn');
    viewBtn.addEventListener('click', () => {
        const token = localStorage.getItem('accessToken');

        if (!token) {
            alert('You must be logged in to view your appointments.');
            window.location.href = 'login.html';
        } else {
            window.location.href = 'my_appointments.html';
        }
    });
});
function logout() {
    localStorage.removeItem('accessToken');
    window.location.href = 'login.html';
}