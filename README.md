# File Exchanger
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
    </li>
    <li>
      <a href="#project-structure">Project Structure</a>
    </li>
    <li>
      <a href="#database">Database</a>
      <ul>
        <li><a href="#table-structures">Table Structures</a></li>
      </ul>
    </li>
    <li>
      <a href="#server-functions">Server Functions</a>
    </li>
    <li>
      <a href="#contact">Contact</a>
    </li>
  </ol>
</details>

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
### Prerequisites
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

### Installation

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
### File download 
![](media/userDownload.gif)


### File upload & configuration 
![](media/adminPanel.gif)


### Authorization & registration
![](media/registration&authorization.gif)




## Project Structure
```bash
< PROJECT ROOT >
   |
   |-- app/
   |    |
   |    | -- models.py                     # Database Tables
   |    | -- routes.py                     # Main functions to work with client
   |    | -- utils.py                      # Helpers to manipulate date, files  
   |    | -- __init__.py                   # Initialization of flask app, connection to database
   |    | -- accountsData.db               # Database
   |    |
   |    |-- storage/                       # Stores files that were sent to server
   |    |
   |    |-- static/
   |    |    |-- css/                  
   |    |    |    |
   |    |    |    |-- desktop.css          # Used by pages, provides adaptability of interface to the bigger screens
   |    |    |    |-- reset.css            # Used by pages, sets basic html-elements parameters to 0
   |    |    |    |-- style.css            # Used by pages, responsible  for design 
   |    |    |-- js/                  
   |    |    |    |
   |    |    |    |-- auth.js              # Responsible for keeping user authorized after closing window
   |    |    |    |-- download.js          # Responsible for downloading files by user and admin
   |    |    |    |-- elementsUtil.js      # Responsible for file upload and configuration by admin
   |    |
   |    |-- templates/
   |    |    |    
   |    |    |-- index.html                # Main page
   |    |    |-- login.html                # Authorization page
   |    |    |-- register.html             # Registration page
   |    |    |-- admin.html                # Modified main page for admin
   |    |    |
   |    |    |
   |    |    |
   |
   |-- run.py                              # Starts the app 
   |
   |-- ************************************************************************
```
## Database
Database includes tables:
<ul>
  <li>ACCOUNT - represents users and admins</li>
  <li>FILE - represents files that exist in storage</li>
  <li>LOG - records file downloads commited by users</li>
</ul>

### Table Structures

ACCOUNT

  ```sh
  CREATE TABLE ACCOUNT( ID INT PRIMARY KEY NOT NULL, LOGIN CHAR (320) NOT NULL, PASSWORD CHAR (320) NOT NULL, ROLE CHAR (10));
  ```
Accounts can have only one from two roles: admin, user. User account can be created though registration and authorization pages. Such accounts are presented as a (password=a), user(password=user), test(password=test)
However, admin status may be obtained only by new member insertion in ACCOUNT table. Project already has one basic representative: <b>admin(password=admin)</b>


FILE

  ```sh
  CREATE TABLE FILE(ID INT PRIMARY KEY NOT NULL, NAME CHAR(100) NOT NULL, SIZE CHAR(100) NOT NULL, DATE CHAR(100) NOT NULL, DISPLAY CHAR(10) NOT NULL, DOWNLOADS INT NOT NULL);
  ```
Files can be displayed or hidden by administrator via interface. 

LOG
  ```sh
  CREATE TABLE LOG(ID INT PRIMARY KEY NOT NULL, LOGIN CHAR(320) NOT NULL, FILE CHAR(100) NOT NULL, TIME CHAR(20) NOT NULL);
  ```
Logs are created automatically by each download.

## Server functions
<ul>
  <li>home() - sends data to main page index.html or admin.html according to user status. Is triggered after redirection to the main page</li>
  <li>login() - checks weather user exists in database. Is triggered in login.html</li>
  <li>logout() - removes user`s cookies from page. Is triggered after pressing button on index.html</li>
  <li>register() - checks and adds new user to database. Is triggered in register.html</li>
  <li>upload() - saves file from client to server`s storage directory. After that, record will automatically apear in database. Is triggered after pressing button "upload" on admin.html and recieving JSON from elementsUtil.js</li>
  <li>admin() - sends data to admin.html. Is triggered after redirection to the admin page</li>
  <li>updateRecordStatus() - changes DISPLAY parameter of file in database. Is triggered after pressing "eye-buttons" on admin page</li>
  <li>download() - sends file from server to client after recieving JSON. Is triggered after pressing "download button" on admin and main pages</li>
  <li>delete() - removes file from storage. After that, record will automatically deleted. Is triggered after pressing "delete button" on admin page</li>
</ul>

<!-- CONTACT -->
## Contact

Daniil Khortov- daniil.khortov.2005@gmail.com

Project Link: https://github.com/DaniilKhortov/file_exchanger_KhortovDP.git
