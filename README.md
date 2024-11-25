# File Exchanger
## About The Project
The essence of the project is a web application that can download files from the device to the server and vice versa. In addition, project supports the concept of users and administrators as main roles.

### Built With
Languages:
* [![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=000)](#)
*	[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
* [![HTML](https://img.shields.io/badge/HTML-%23E34F26.svg?logo=html5&logoColor=white)](#)
* 	[![CSS](https://img.shields.io/badge/CSS-1572B6?logo=css3&logoColor=fff)](#)

Frameworks:
* [![Flask](https://img.shields.io/badge/Flask-000?logo=flask&logoColor=fff)](#)

Databases:
* [![SQLite](https://img.shields.io/badge/SQLite-%2307405e.svg?logo=sqlite&logoColor=white)](#)

## Getting Started
###Prerequisites
* Flask
  ```sh
  pip install Flask
  ```
* SQLAlchemy
  ```sh
  pip install SQLAlchemy
  ```
* SQLAlchemy for Flask  
  ```sh
  pip install Flask-SQLAlchemy
  ```

###Installation

1. Clone the repository
   ```sh
   git clone https://github.com/DaniilKhortov/file_exchanger_KhortovDP.git
   ```
2. Install libraries
  ```sh
  pip install Flask-SQLAlchemy
  ```
3.Change git remote
  ```sh
  git remote set-url origin https://github.com/DaniilKhortov/file_exchanger_KhortovDP.git
  ```


## Usage







##Project Structure
```bash
< PROJECT ROOT >
   |
   |-- app/
   |    |
   |    | -- config.py                     # App Configuration
   |    | -- models.py                     # Database Tables 
   |    | -- forms.py                      # App Forms: login, registration
   |    | -- util.py                       # Helpers to manipulate date, files  
   |    | -- views.py                      # App Routing
   |    | -- __init__.py                   # Bundle all above sections and expose the Flask APP 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/
   |    |    |
   |    |    |-- includes/                 # Page chunks, components
   |    |    |    |
   |    |    |    |-- navigation.html      # Top bar
   |    |    |    |-- sidebar.html         # Left sidebar
   |    |    |    |-- scripts.html         # JS scripts common to all pages
   |    |    |    |-- footer.html          # The common footer
   |    |    |
   |    |    |-- layouts/                  # App Layouts (the master pages)
   |    |    |    |
   |    |    |    |-- base.html            # Used by common pages like index, UI
   |    |    |
   |    |    |-- accounts/                 # Auth Pages (login, register)
   |    |    |    |
   |    |    |    |-- login.html           # Use layout `base-fullscreen.html`
   |    |    |    |-- register.html        # Use layout `base-fullscreen.html`  
   |    |    |
   |    |  index.html                      # The default page
   |    |  page-404.html                   # Error 404 page (page not found)
   |    |  page-500.html                   # Error 500 page (server error)
   |    |    *.html                        # All other pages provided by the UI Kit
   |
   |-- requirements.txt                    # Application Dependencies
   |
   |-- run.py                              # Start the app in development and production
   |
   |-- ************************************************************************
```

