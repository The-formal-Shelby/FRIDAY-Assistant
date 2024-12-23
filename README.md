# FRIDAY-Assistant
A Python-based personal voice assistant that helps you with daily tasks and interactions. Friday is designed to be your digital companion, capable of performing various operations through simple text commands.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Friday - Personal Voice Assistant</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        /* Reset and Base Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Navigation */
        nav {
            background: #2c3e50;
            padding: 1rem;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
        }

        nav .logo h1 {
            color: white;
            font-size: 1.5rem;
            float: left;
        }

        nav ul {
            float: right;
            list-style: none;
        }

        nav ul li {
            display: inline-block;
            margin-left: 1rem;
        }

        nav ul li a {
            color: white;
            text-decoration: none;
            font-size: 1.1rem;
        }

        nav ul li a:hover {
            color: #3498db;
        }

        /* Hero Section */
        .hero {
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('https://source.unsplash.com/random/1920x1080?technology');
            background-size: cover;
            background-position: center;
            height: 100vh;
            display: flex;
            align-items: center;
            text-align: center;
            color: white;
            padding-top: 80px;
        }

        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
        }

        /* Features Section */
        .features {
            padding: 5rem 0;
            background: #f9f9f9;
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .feature-card {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.3s ease;
        }

        .feature-card:hover {
            transform: translateY(-5px);
        }

        .feature-card i {
            font-size: 2.5rem;
            color: #3498db;
            margin-bottom: 1rem;
        }

        /* Requirements Section */
        .requirements {
            padding: 5rem 0;
        }

        .req-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .req-box {
            background: #f8f9fa;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        .req-box ul {
            list-style-position: inside;
            margin-top: 1rem;
        }

        /* Installation Section */
        .installation {
            padding: 5rem 0;
            background: #f9f9f9;
        }

        .install-steps {
            background: #2c3e50;
            padding: 2rem;
            border-radius: 10px;
            margin-top: 2rem;
        }

        .install-steps pre {
            overflow-x: auto;
        }

        .install-steps code {
            color: #fff;
            font-family: 'Courier New', Courier, monospace;
        }

        /* Footer */
        footer {
            background: #2c3e50;
            color: white;
            text-align: center;
            padding: 1rem 0;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            nav .logo,
            nav ul {
                float: none;
                text-align: center;
            }

            nav ul {
                margin-top: 1rem;
            }

            nav ul li {
                display: block;
                margin: 0.5rem 0;
            }

            .hero h1 {
                font-size: 2rem;
            }
        }

        /* Section Headers */
        section h2 {
            text-align: center;
            margin-bottom: 2rem;
            color: #2c3e50;
            font-size: 2.5rem;
        }
    </style>
</head>
<body>
    <header>
        <nav>
            <div class="logo">
                <h1>Friday Assistant</h1>
            </div>
            <ul>
                <li><a href="#overview">Overview</a></li>
                <li><a href="#features">Features</a></li>
                <li><a href="#requirements">Requirements</a></li>
                <li><a href="#installation">Installation</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="overview" class="hero">
            <div class="container">
                <h1>Your Personal Voice Assistant</h1>
                <p>Meet Friday, your intelligent companion for daily tasks and interactions</p>
            </div>
        </section>

        <section id="features" class="features">
            <div class="container">
                <h2>Key Features</h2>
                <div class="feature-grid">
                    <div class="feature-card">
                        <i class="fas fa-microphone"></i>
                        <h3>Voice Interaction</h3>
                        <p>Natural voice responses using pyttsx3</p>
                    </div>
                    <div class="feature-card">
                        <i class="fas fa-globe"></i>
                        <h3>Web Navigation</h3>
                        <p>Quick access to popular websites and applications</p>
                    </div>
                    <div class="feature-card">
                        <i class="fas fa-clock"></i>
                        <h3>Time Management</h3>
                        <p>Date and time information at your command</p>
                    </div>
                    <div class="feature-card">
                        <i class="fas fa-calculator"></i>
                        <h3>Utilities</h3>
                        <p>Calculator, Wikipedia search, and more</p>
                    </div>
                </div>
            </div>
        </section>

        <section id="requirements" class="requirements">
            <div class="container">
                <h2>System Requirements</h2>
                <div class="req-container">
                    <div class="req-box">
                        <h3>Hardware Requirements</h3>
                        <ul>
                            <li>Microphone (for future voice input)</li>
                            <li>Speakers or Headphones</li>
                            <li>2GB RAM minimum</li>
                            <li>Internet Connection</li>
                        </ul>
                    </div>
                    <div class="req-box">
                        <h3>Software Requirements</h3>
                        <ul>
                            <li>Python 3.7 or higher</li>
                            <li>Windows/Linux/MacOS</li>
                            <li>Required Python packages</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <section id="installation" class="installation">
            <div class="container">
                <h2>Installation Guide</h2>
                <div class="install-steps">
                    <pre><code>
# Clone the repository
git clone https://github.com/yourusername/friday-assistant.git

# Navigate to the project directory
cd friday-assistant

# Install required packages
pip install -r requirements.txt

# Run Friday
python friday.py
                    </code></pre>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2024 Friday Assistant. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
