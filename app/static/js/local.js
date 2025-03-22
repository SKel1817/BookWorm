// Placeholder JS file

// Cookie management functions
const BookWormCookies = {
    // Cookie constants
    COOKIE_CONSENT_NAME: 'bookworm_cookie_consent',
    FOCUS_MINUTES_NAME: 'bookworm_focus_minutes',
    GARDEN_PLANTS_NAME: 'bookworm_garden_plants',
    
    // Check if cookies are accepted
    cookiesAccepted: function() {
        return this.getCookie(this.COOKIE_CONSENT_NAME) === 'accepted';
    },
    
    // Set a cookie with expiration days
    setCookie: function(name, value, days) {
        // Don't set non-consent cookies if cookies are not accepted
        if (!this.cookiesAccepted() && name !== this.COOKIE_CONSENT_NAME) return;
        
        let expires = '';
        if (days) {
            const date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = '; expires=' + date.toUTCString();
        }
        document.cookie = name + '=' + encodeURIComponent(value) + expires + '; path=/';
    },
    
    // Get a cookie value by name
    getCookie: function(name) {
        const nameEQ = name + '=';
        const ca = document.cookie.split(';');
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) === ' ') c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) === 0) return decodeURIComponent(c.substring(nameEQ.length, c.length));
        }
        return null;
    },
    
    // Delete a cookie
    deleteCookie: function(name) {
        document.cookie = name + '=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
    }
};

// Initialize theme based on saved preference or system preference
document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('theme-toggle');
    
    // Check for saved theme preference or use system preference
    const savedTheme = BookWormCookies.cookiesAccepted() ? 
        BookWormCookies.getCookie('bookworm_theme') : null;
        
    if (savedTheme === 'dark' || 
        (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.documentElement.classList.add('dark');
    } else {
        document.documentElement.classList.remove('dark');
    }
    
    // Toggle theme when button is clicked
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const isDark = document.documentElement.classList.toggle('dark');
            
            if (BookWormCookies.cookiesAccepted()) {
                BookWormCookies.setCookie('bookworm_theme', isDark ? 'dark' : 'light', 365);
            }
        });
    }
    
    // Show cookie consent if needed
    if (BookWormCookies.getCookie(BookWormCookies.COOKIE_CONSENT_NAME) === null) {
        const cookieConsent = document.getElementById('cookie-consent');
        if (cookieConsent) {
            cookieConsent.classList.remove('hidden');
        }
    }
});

console.log('Local JS file loaded');