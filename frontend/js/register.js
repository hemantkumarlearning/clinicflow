const API_BASE = 'http://127.0.0.1:5000';

document.getElementById('register-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const username = document.getElementById('reg-username').value.trim()
    const password = document.getElementById('reg-password').value;
    const name = document.getElementById('reg-name').value.trim();
    const dobInput = document.getElementById('reg-dob').value; // expected: YYYY-MM-DDTHH:MM
    const gender = document.getElementById('reg-gender').value.trim();

    // const dobDate = dobInput.split('T')[0]; // "2025-12-25T10:30" → "2025-12-25"

    const payload = {
            username,
            password,
            name,
            dobInput,
            gender
    };
    const res = await fetch(`${API_BASE}/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });

    if (res.ok) {
        alert('Registered successfully! You can now log in.');
        window.location.href = 'login.html';
    } else {
        alert('Registration failed');
    }
});
