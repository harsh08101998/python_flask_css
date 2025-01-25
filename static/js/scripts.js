// Simple script to display an alert when the contact page loads
document.addEventListener('DOMContentLoaded', () => {
    if (window.location.pathname === '/contact') {
        alert('Welcome to the Contact page! Feel free to reach out.');
    }
});

// Smooth scrolling for navigation links (if needed in the future)
document.querySelectorAll('a.nav-link').forEach(anchor => {
    anchor.addEventListener('click', function (event) {
        event.preventDefault();
        const targetId = this.getAttribute('href');
        if (targetId.startsWith('#')) {
            document.querySelector(targetId).scrollIntoView({
                behavior: 'smooth',
            });
        }
    });
});

