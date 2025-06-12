# Digital Advisor - Flask Website Framework

A modern, responsive Flask web framework designed for digital advisory services. This framework provides easily customizable templates for creating blogs, info pages, and tech websites with a professional digital advisor theme.

## Features

- **Modern Design**: Clean, professional design with a digital advisor theme
- **Responsive Layout**: Mobile-first design using Bootstrap 5
- **Multiple Page Types**: 
  - Home page with hero section and features
  - Blog page with post listings and sidebar
  - About page with team and company information
  - Services page showcasing technical offerings
- **Easy Customization**: Template-based structure for easy content modifications
- **Interactive Elements**: JavaScript enhancements for better user experience

## Quick Start

### Prerequisites
- Python 3.7+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/loujr/fiveservers.git
cd fiveservers
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and visit: `http://localhost:5000`

## Project Structure

```
fiveservers/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/            # Jinja2 templates
│   ├── base.html         # Base template with navigation and footer
│   ├── index.html        # Home page
│   ├── blog.html         # Blog page
│   ├── about.html        # About/info page
│   └── services.html     # Services/tech page
├── static/               # Static files
│   ├── css/
│   │   └── style.css     # Custom styles
│   ├── js/
│   │   └── script.js     # Custom JavaScript
│   └── images/           # Image assets
└── website/              # Legacy files (can be removed)
```

## Customization Guide

### Modifying Content

1. **Home Page**: Edit `templates/index.html` to customize the hero section, features, and call-to-action
2. **Blog**: Modify `templates/blog.html` and update the blog posts data in `app.py`
3. **About Page**: Update `templates/about.html` with your team information and company details
4. **Services**: Customize `templates/services.html` and the services data in `app.py`

### Styling

- **Colors**: Update CSS variables in `static/css/style.css` under `:root`
- **Fonts**: Change the Google Fonts link in `templates/base.html`
- **Layout**: Modify Bootstrap classes in templates for different layouts

### Adding New Pages

1. Create a new template in `templates/`
2. Add a route in `app.py`
3. Update navigation in `templates/base.html`

## Development

### Running in Development Mode
```bash
python app.py
```
The app runs with debug mode enabled by default.

### Production Deployment
For production, use a WSGI server like Gunicorn:
```bash
pip install gunicorn
gunicorn app:app
```

## Technologies Used

- **Backend**: Flask 3.0, Python 3.12+
- **Frontend**: Bootstrap 5, Font Awesome 6, Google Fonts
- **JavaScript**: Vanilla JS with modern ES6+ features
- **Styling**: Custom CSS with CSS Grid and Flexbox

## Browser Support

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
