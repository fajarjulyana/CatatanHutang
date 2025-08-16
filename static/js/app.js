// Debt Tracker JavaScript functionality

document.addEventListener('DOMContentLoaded', function() {
    
    // Auto-submit filters when changed
    const filterForm = document.querySelector('form');
    if (filterForm) {
        const selects = filterForm.querySelectorAll('select');
        selects.forEach(select => {
            select.addEventListener('change', function() {
                // Don't auto-submit if it's the search form
                if (!this.closest('form').querySelector('input[name="search"]')) {
                    this.closest('form').submit();
                }
            });
        });
    }
    
    // Search form handling
    const searchInput = document.querySelector('input[name="search"]');
    if (searchInput) {
        let searchTimeout;
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                this.closest('form').submit();
            }, 500); // Debounce search for 500ms
        });
    }
    
    // Confirmation for debt deletion
    const deleteButtons = document.querySelectorAll('form[action*="delete_debt"] button');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Apakah Anda yakin ingin menghapus hutang ini? Tindakan ini tidak dapat dibatalkan.')) {
                e.preventDefault();
            }
        });
    });
    
    // Toggle paid status confirmation for large amounts
    const toggleButtons = document.querySelectorAll('form[action*="toggle_paid"] button');
    toggleButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            const row = this.closest('tr');
            const amountText = row.querySelector('td:nth-child(2)').textContent.trim();
            const amount = parseFloat(amountText.replace(/[$,]/g, ''));
            
            // Confirm for amounts over Rp 1,000,000
            if (amount > 1000000) {
                const action = this.querySelector('i').classList.contains('fa-check') ? 'tandai sebagai lunas' : 'tandai sebagai belum lunas';
                if (!confirm(`Apakah Anda yakin ingin ${action} hutang sebesar ${amountText}?`)) {
                    e.preventDefault();
                }
            }
        });
    });
    
    // Format currency inputs
    const currencyInputs = document.querySelectorAll('input[type="number"][step="0.01"]');
    currencyInputs.forEach(input => {
        input.addEventListener('blur', function() {
            const value = parseFloat(this.value);
            if (!isNaN(value) && value >= 0) {
                this.value = value.toFixed(2);
            }
        });
        
        // Prevent negative values
        input.addEventListener('input', function() {
            if (this.value < 0) {
                this.value = 0;
            }
        });
    });
    
    // Enhanced form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('input[required], select[required], textarea[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    field.classList.add('is-invalid');
                    isValid = false;
                } else {
                    field.classList.remove('is-invalid');
                }
            });
            
            // Validate amount field specifically
            const amountField = form.querySelector('input[name="amount"]');
            if (amountField) {
                const amount = parseFloat(amountField.value);
                if (isNaN(amount) || amount <= 0) {
                    amountField.classList.add('is-invalid');
                    isValid = false;
                } else {
                    amountField.classList.remove('is-invalid');
                }
            }
            
            if (!isValid) {
                e.preventDefault();
                // Scroll to first invalid field
                const firstInvalid = form.querySelector('.is-invalid');
                if (firstInvalid) {
                    firstInvalid.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    firstInvalid.focus();
                }
            }
        });
    });
    
    // Clear search functionality
    const searchForm = document.querySelector('form');
    if (searchForm && searchInput) {
        // Add clear button functionality if it exists
        const clearButton = document.createElement('button');
        clearButton.type = 'button';
        clearButton.className = 'btn btn-outline-secondary';
        clearButton.innerHTML = '<i class="fas fa-times"></i>';
        clearButton.title = 'Clear search';
        
        clearButton.addEventListener('click', function() {
            searchInput.value = '';
            searchForm.submit();
        });
        
        // Add clear button next to search input if search has value
        if (searchInput.value) {
            const inputGroup = searchInput.closest('.col-md-3');
            if (inputGroup) {
                const buttonGroup = document.createElement('div');
                buttonGroup.className = 'input-group';
                searchInput.parentNode.insertBefore(buttonGroup, searchInput);
                buttonGroup.appendChild(searchInput);
                
                const appendDiv = document.createElement('div');
                appendDiv.className = 'input-group-append';
                appendDiv.appendChild(clearButton);
                buttonGroup.appendChild(appendDiv);
            }
        }
    }
    
    // Tooltip initialization for Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert:not(.alert-danger)');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

// Utility functions
function formatCurrency(amount) {
    return new Intl.NumberFormat('id-ID', {
        style: 'currency',
        currency: 'IDR'
    }).format(amount);
}

function isOverdue(dueDate) {
    if (!dueDate) return false;
    const today = new Date();
    const due = new Date(dueDate);
    return due < today;
}

// Export functions for use in other scripts
window.DebtTracker = {
    formatCurrency,
    isOverdue
};
