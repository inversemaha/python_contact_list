# Django Contactlist App

A simple contact list (contactlist) web application built with Django. You can add, search, edit, and delete contacts.

## Features
- Add new contacts (name, relationship, phone, email, address)
- Search contacts by name
- View contact profiles
- Edit and delete contacts
- Responsive UI with FontAwesome icons

## Project Structure
```
contactlist/
├── .git/              # Git repository data
├── contact/           # Django app for contacts
├── contactlist/       # Django project settings and configuration
├── db.sqlite3         # SQLite database file
├── manage.py          # Django management script
├── README.md          # Project documentation
├── static/            # Static files (CSS, JS, images)
├── templates/         # HTML templates
```

## Getting Started

### Prerequisites
- Python 3.x installed on your system
- Django installed (see below)

### Setup and Run
1. Install dependencies:
   ```bash
   pip install django
   ```
2. Run migrations:
   ```bash
   python manage.py migrate
   ```
3. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```
5. Access the app at [http://localhost:8000](http://localhost:8000)

## Usage
- Use the search bar to find contacts by name.
- Click the plus icon to add a new contact.
- Click a contact to view their profile.
- Edit or delete contacts from their profile page.

## License
MIT

---
For any issues or contributions, please open an issue or pull request on GitHub.
