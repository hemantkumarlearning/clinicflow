const API_BASE = 'http://127.0.0.1:5000';

document.addEventListener('DOMContentLoaded', () => {
    const token = localStorage.getItem('accessToken');
    const role = localStorage.getItem('userRole');

    if (role !== 'admin') {
        alert('Access denied: Admins only');
        window.location.href = 'login.html';
        return;
    }

    // Show forms
    document.getElementById('show-doctor-form').addEventListener('click', () => {
        document.getElementById('doctor-form').style.display = 'block';
        document.getElementById('receptionist-form').style.display = 'none';
    });

    document.getElementById('show-receptionist-form').addEventListener('click', () => {
        document.getElementById('receptionist-form').style.display = 'block';
        document.getElementById('doctor-form').style.display = 'none';
    });

    // Submit doctor form
    document.getElementById('create-doctor-form').addEventListener('submit', async (e) => {
        e.preventDefault();

        const payload = {
            name: document.getElementById('doc-name').value,
            specialty: document.getElementById('doc-specialty').value,
            username: document.getElementById('doc-username').value,
            password: document.getElementById('doc-password').value,
            // role: 'doctor'
        };

        const res = await fetch(`${API_BASE}/users/doctor`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify(payload)
        });

        const data = await res.json();
        alert(data.msg || 'Doctor created');
    });

    // Submit receptionist form
    document.getElementById('create-receptionist-form').addEventListener('submit', async (e) => {
        e.preventDefault();

        const payload = {
            // name: document.getElementById('rec-name').value,
            username: document.getElementById('rec-username').value,
            password: document.getElementById('rec-password').value,
            // role: 'receptionist'
        };

        const res = await fetch(`${API_BASE}/users/receptionist`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify(payload)
        });

        const data = await res.json();
        alert(data.msg || 'Receptionist created');
    });
});
function logout() {
    localStorage.removeItem('accessToken');
    window.location.href = 'login.html';
}