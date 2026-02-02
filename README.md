Movie Watch List
A vibe-coded web application built with Django (by way of ClaudeAI/Copilot and Gemini) that allows users to search for movies, manage a personal watchlist, and track their viewing progress.

Features
User Authentication: Secure signup and login system.

Movie Search: Find movies using title-based searches.

Watchlist Management: Add movies to a personal list and mark them as "Watched."

Movie Details: View detailed information about movies, including ratings and descriptions.

Responsive Design: Optimized for both desktop and mobile viewing.

Prerequisites
Before you begin, ensure you have the following installed on your local machine:

Python 3.8+

pip (Python package manager)

Virtualenv (Recommended)

Optional: A TMDB API Key (if the project integrates with The Movie Database).

Installation & Setup
1. Clone the Repository
Bash
git clone https://github.com/ryandenardis/movie-watch-list.git
cd movie-watch-list
2. Create a Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies.

Bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Environment Configuration
Create a .env file in the root directory (or update settings.py) to manage sensitive information:

Code snippet
DEBUG=True
SECRET_KEY=your_django_secret_key
# If using TMDB API
TMDB_API_KEY=your_api_key_here
5. Database Migrations
Set up the local SQLite database and create the necessary tables.

Bash
python manage.py makemigrations
python manage.py migrate
Running the Application
1. Create a Superuser
To access the Django Admin interface and manage movie data manually:

Bash
python manage.py createsuperuser
2. Start the Development Server
Bash
python manage.py runserver
3. Access the App
Open your web browser and navigate to:

Application: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/admin/

Usage Guide
Searching for Movies
Navigate to the Home page.

Use the search bar to enter a movie title.

Browse the results and click on a movie to see more details.

Managing Your Watchlist
Add to List: On a movie's detail page, click the "Add to Watchlist" button.

View List: Navigate to your profile or "My Watchlist" section to see saved movies.

Mark as Watched: Toggle the status of a movie once you have finished viewing it.

Remove: Click the remove icon/button to take a movie off your list.

Project Structure
movie_project/: Project configuration (settings, URLs).

movies/ (or similar app name): Contains models (Movie, Watchlist), views, and logic.

templates/: HTML files for the frontend.

static/: CSS, JavaScript, and image assets.

Contributing
Fork the project.

Create your feature branch (git checkout -b feature/AmazingFeature).

Commit your changes (git commit -m 'Add some AmazingFeature').

Push to the branch (git push origin feature/AmazingFeature).

Open a Pull Request.
