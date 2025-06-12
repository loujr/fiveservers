from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Home page route"""
    return render_template('index.html', 
                         page_title='Digital Advisor | Home',
                         page_type='home')

@app.route('/blog')
def blog():
    """Blog page route"""
    # Sample blog posts
    posts = [
        {
            'title': 'The Future of Digital Advisory Services',
            'date': '2024-01-15',
            'excerpt': 'Exploring how AI and automation are transforming the advisory landscape...',
            'author': 'Digital Team'
        },
        {
            'title': 'Best Practices for Tech Infrastructure',
            'date': '2024-01-10',
            'excerpt': 'Learn about modern approaches to building scalable tech solutions...',
            'author': 'Tech Team'
        },
        {
            'title': 'Data-Driven Decision Making',
            'date': '2024-01-05',
            'excerpt': 'How to leverage analytics for better business outcomes...',
            'author': 'Analytics Team'
        }
    ]
    return render_template('blog.html', 
                         page_title='Digital Advisor | Blog',
                         page_type='blog',
                         posts=posts)

@app.route('/about')
def about():
    """About/Info page route"""
    return render_template('about.html', 
                         page_title='Digital Advisor | About',
                         page_type='about')

@app.route('/services')
def services():
    """Services/Tech page route"""
    services_list = [
        {
            'name': 'Digital Strategy Consulting',
            'description': 'Comprehensive digital transformation guidance',
            'icon': 'strategy'
        },
        {
            'name': 'Technology Implementation',
            'description': 'End-to-end tech solution deployment',
            'icon': 'tech'
        },
        {
            'name': 'Data Analytics & AI',
            'description': 'Advanced analytics and machine learning solutions',
            'icon': 'analytics'
        },
        {
            'name': 'Cloud Infrastructure',
            'description': 'Scalable cloud architecture and migration',
            'icon': 'cloud'
        }
    ]
    return render_template('services.html', 
                         page_title='Digital Advisor | Services',
                         page_type='services',
                         services=services_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)