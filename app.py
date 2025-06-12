from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Home page route"""
    return render_template('index.html', 
                         page_title='fiveservers | Home',
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
                         page_title='fiveservers | Blog',
                         page_type='blog',
                         posts=posts)

@app.route('/about')
def about():
    """About/Info page route"""
    return render_template('about.html', 
                         page_title='fiveservers | About',
                         page_type='about')

@app.route('/services')
def services():
    """Services/Tech page route"""
    services_list = [
        {
            'name': 'Strategic Digital Advising',
            'description': 'Executive-level guidance for digital transformation initiatives with proven methodologies',
            'icon': 'brain',
            'features': [
                'Digital transformation roadmap development',
                'Technology stack assessment and optimization',
                'Change management and adoption strategies',
                'ROI analysis and success metrics planning'
            ]
        },
        {
            'name': 'Precision Software Contracting',
            'description': 'Custom software development and system integration delivered with excellence',
            'icon': 'code',
            'features': [
                'Full-stack web and mobile applications',
                'API development and microservices architecture',
                'Legacy system modernization',
                'Quality assurance and testing automation'
            ]
        },
        {
            'name': 'Cloud Infrastructure Contracting',
            'description': 'Scalable cloud architecture design, deployment, and optimization',
            'icon': 'cloud',
            'features': [
                'Multi-cloud strategy and implementation',
                'DevOps pipeline automation',
                'Infrastructure as Code (IaC)',
                'Security and compliance frameworks'
            ]
        },
        {
            'name': 'Data & AI Solutions',
            'description': 'Advanced analytics, machine learning, and artificial intelligence implementations',
            'icon': 'chart-line',
            'features': [
                'Predictive analytics and business intelligence',
                'Machine learning model development',
                'Data pipeline architecture',
                'AI strategy and ethical implementation'
            ]
        }
    ]
    return render_template('services.html', 
                         page_title='fiveservers | Services',
                         page_type='services',
                         services=services_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)