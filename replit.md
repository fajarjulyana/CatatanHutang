# Fajar Mandiri Store - Sistem Pencatat Hutang

## Overview

A Flask-based debt tracking application for Fajar Mandiri Store to manage and monitor customer debts and store obligations. The system allows users to add, edit, delete, and track debts with features like payment status tracking, overdue debt identification, and comprehensive filtering and sorting capabilities. The application provides a dashboard view with summary statistics and detailed debt management functionality tailored for Indonesian small business operations.

## User Preferences

- Preferred communication style: Simple, everyday language
- Interface Language: Bahasa Indonesia (Indonesian)
- Currency: Indonesian Rupiah (Rp)
- Database: SQLite for development
- Business Name: Fajar Mandiri Store
- Application Purpose: Small business debt tracking system
- Currency Input: Simplified integer input without decimals (.00)
- Date Input: Manual date picker with quick buttons (Today, +1 Week, +1 Month)
- Alerts: Automatic alerts for overdue and due-soon debts

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 templates with Bootstrap 5 dark theme
- **CSS Framework**: Bootstrap 5 with custom CSS overrides for enhanced styling
- **JavaScript**: Vanilla JavaScript for client-side interactions including auto-submit filters, debounced search, and confirmation dialogs
- **Icons**: Font Awesome integration for consistent iconography
- **Responsive Design**: Mobile-first approach using Bootstrap's grid system

### Backend Architecture
- **Web Framework**: Flask with modular route organization
- **Form Handling**: Flask-WTF for secure form processing with CSRF protection
- **Input Validation**: WTForms validators for client and server-side validation
- **Session Management**: Flask's built-in session handling with configurable secret keys
- **Middleware**: ProxyFix for handling reverse proxy headers

### Data Layer
- **ORM**: SQLAlchemy with Flask-SQLAlchemy integration
- **Database**: SQLite (debt_tracker.db) configured for Indonesian locale
- **Connection Pooling**: Configured with connection recycling and pre-ping for reliability
- **Schema Design**: Single Debt model with automatic timestamp tracking and calculated properties
- **Currency**: Indonesian Rupiah formatting with dot separators for thousands

### Key Features
- **Debt Management**: CRUD operations for debt entries with manual date entry
- **Status Tracking**: Boolean flag for paid/unpaid status with toggle functionality
- **Due Date Monitoring**: Automatic overdue debt detection with color-coded alerts
- **Search and Filtering**: Text search across creditor names and descriptions
- **Sorting**: Multi-column sorting by amount, due date, creditor name, and creation date
- **Summary Statistics**: Real-time calculation of total outstanding, paid, and aggregate debt amounts
- **Currency Input**: Simplified integer input without decimal places for Indonesian Rupiah
- **Alert System**: Visual warnings for overdue and due-soon debts
- **Responsive Design**: Mobile-friendly interface with adaptive columns

### Security Considerations
- CSRF protection on all forms
- Input validation and sanitization
- Environment-based configuration for sensitive data
- Session security with configurable secret keys

### Deployment Architecture
- **WSGI Server**: Built-in Flask development server (production would require Gunicorn/uWSGI)
- **Static Files**: Direct serving via Flask for CSS, JavaScript, and other assets
- **Environment Configuration**: Support for production environment variables
- **Database Migrations**: Automatic table creation on application startup

## External Dependencies

### Python Packages
- **Flask**: Core web framework for routing and request handling
- **Flask-SQLAlchemy**: Database ORM and model management
- **Flask-WTF**: Form handling and CSRF protection
- **WTForms**: Form validation and rendering
- **Werkzeug**: WSGI utilities and middleware

### Frontend Dependencies
- **Bootstrap 5**: CSS framework with Replit dark theme variant
- **Font Awesome 6**: Icon library for UI consistency
- **Custom CSS**: Application-specific styling enhancements

### Database
- **SQLite**: Primary database (debt_tracker.db) with Indonesian locale support
- **Minimum Amount**: Set to Rp 1.000 for realistic Indonesian currency values

### Development Tools
- **Python Logging**: Configured for debug-level logging during development
- **Flask Debug Mode**: Hot reloading and enhanced error pages for development