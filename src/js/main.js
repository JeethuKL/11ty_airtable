// Placeholder JS file to prevent 404 and MIME errors.
// Add your custom scripts here if needed.

// Mobile menu functionality
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuButton = document.querySelector('.mobile-menu-button');
    const mobileMenu = document.querySelector('#mobile-menu');
    const menuIcon = mobileMenuButton.querySelector('svg:first-child');
    const closeIcon = mobileMenuButton.querySelector('svg:last-child');
    
    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', function() {
            const isOpen = !mobileMenu.classList.contains('hidden');
            
            if (isOpen) {
                // Close menu
                mobileMenu.classList.add('hidden');
                menuIcon.classList.remove('hidden');
                closeIcon.classList.add('hidden');
                mobileMenuButton.setAttribute('aria-expanded', 'false');
            } else {
                // Open menu
                mobileMenu.classList.remove('hidden');
                menuIcon.classList.add('hidden');
                closeIcon.classList.remove('hidden');
                mobileMenuButton.setAttribute('aria-expanded', 'true');
            }
        });
    }
    
    // Close mobile menu when clicking outside
    document.addEventListener('click', function(event) {
        if (!mobileMenuButton.contains(event.target) && !mobileMenu.contains(event.target)) {
            mobileMenu.classList.add('hidden');
            menuIcon.classList.remove('hidden');
            closeIcon.classList.add('hidden');
            mobileMenuButton.setAttribute('aria-expanded', 'false');
        }
    });
    
    // Close mobile menu on window resize (desktop)
    window.addEventListener('resize', function() {
        if (window.innerWidth >= 768) {
            mobileMenu.classList.add('hidden');
            menuIcon.classList.remove('hidden');
            closeIcon.classList.add('hidden');
            mobileMenuButton.setAttribute('aria-expanded', 'false');
        }
    });
});

// Smooth scrolling for anchor links
document.addEventListener('DOMContentLoaded', function() {
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href === '#') return;
            
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                
                const headerHeight = document.querySelector('header').offsetHeight;
                const targetPosition = target.offsetTop - headerHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
});

// Loading animations
document.addEventListener('DOMContentLoaded', function() {
    // Add fade-in animation to elements with specific classes
    const animatedElements = document.querySelectorAll('.animate-fade-in, .animate-slide-up, .animate-scale-in');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0) scale(1)';
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    animatedElements.forEach(el => {
        // Set initial state
        el.style.opacity = '0';
        if (el.classList.contains('animate-slide-up')) {
            el.style.transform = 'translateY(20px)';
        } else if (el.classList.contains('animate-scale-in')) {
            el.style.transform = 'scale(0.95)';
        }
        
        // Add transition
        el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        
        // Observe element
        observer.observe(el);
    });
});

// Form validation and enhancement
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                const errorMessage = field.parentNode.querySelector('.error-message');
                
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('border-red-500', 'focus:border-red-500', 'focus:ring-red-500');
                    
                    if (!errorMessage) {
                        const error = document.createElement('p');
                        error.className = 'error-message text-red-500 text-sm mt-1';
                        error.textContent = 'This field is required';
                        field.parentNode.appendChild(error);
                    }
                } else {
                    field.classList.remove('border-red-500', 'focus:border-red-500', 'focus:ring-red-500');
                    if (errorMessage) {
                        errorMessage.remove();
                    }
                }
            });
            
            if (!isValid) {
                e.preventDefault();
            }
        });
    });
});

// Copy to clipboard functionality
function copyToClipboard(text) {
    if (navigator.clipboard && window.isSecureContext) {
        return navigator.clipboard.writeText(text);
    } else {
        // Fallback for older browsers
        const textArea = document.createElement('textarea');
        textArea.value = text;
        textArea.style.position = 'absolute';
        textArea.style.opacity = '0';
        document.body.appendChild(textArea);
        textArea.select();
        return new Promise((resolve, reject) => {
            try {
                document.execCommand('copy') ? resolve() : reject();
                document.body.removeChild(textArea);
            } catch (error) {
                reject(error);
                document.body.removeChild(textArea);
            }
        });
    }
}

// Add copy buttons to code blocks
document.addEventListener('DOMContentLoaded', function() {
    const codeBlocks = document.querySelectorAll('pre code');
    
    codeBlocks.forEach(codeBlock => {
        const pre = codeBlock.parentElement;
        const wrapper = document.createElement('div');
        wrapper.className = 'relative';
        
        const copyButton = document.createElement('button');
        copyButton.className = 'absolute top-2 right-2 bg-gray-800 text-white text-xs px-2 py-1 rounded opacity-75 hover:opacity-100 transition-opacity';
        copyButton.textContent = 'Copy';
        
        copyButton.addEventListener('click', function() {
            copyToClipboard(codeBlock.textContent).then(() => {
                copyButton.textContent = 'Copied!';
                setTimeout(() => {
                    copyButton.textContent = 'Copy';
                }, 2000);
            }).catch(() => {
                copyButton.textContent = 'Error';
                setTimeout(() => {
                    copyButton.textContent = 'Copy';
                }, 2000);
            });
        });
        
        pre.parentNode.insertBefore(wrapper, pre);
        wrapper.appendChild(pre);
        wrapper.appendChild(copyButton);
    });
});

// Performance monitoring
if ('performance' in window) {
    window.addEventListener('load', function() {
        setTimeout(function() {
            const perfData = window.performance.timing;
            const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
            
            // Log to analytics if available
            if (typeof gtag !== 'undefined') {
                gtag('event', 'page_load_time', {
                    value: pageLoadTime
                });
            }
        }, 0);
    });
} 