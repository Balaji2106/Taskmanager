# Task Management Web Application

## Overview

The Task Management Web Application is a simple application that allows users to create, read, update, and delete tasks. It features a RESTful API built with Django and a frontend using HTML, CSS, and JavaScript. Users can manage their tasks efficiently through an intuitive interface.

## Features

- **Create Tasks**: Add new tasks with titles and descriptions.
- **Read Tasks**: View all tasks in a list format.
- **Update Tasks**: Edit existing tasks to change their titles and descriptions.
- **Delete Tasks**: Remove tasks that are no longer needed.
- **Responsive Design**: The application is designed to work on both desktop and mobile devices.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL 
- **API**: RESTful API

## Getting Started

### Prerequisites

- Python 3.x
- Django
- MySQL (or SQLite)
- Node.js (for development, if using npm packages)

### Installation

1. **Clone the Repository**:
   git clone https://github.com/yourusername/task-management-app.git
   cd task-management-app

2.  Set Up Virtual Environment:
	python -m venv venv
	source venv/bin/activate  # On Windows use venv\Scripts\activate

3.  Install Dependencies:
	
	pip install -r requirements.txt

4. Run the Development Server:
	
	python manage.py runserver


Usage
	Adding Tasks: Fill out the form on the homepage to add a new task.
	Viewing Tasks: All tasks will be displayed in a list format.
	Editing Tasks: Click the "Edit" button next to a task to update it.
	Deleting Tasks: Click the "Delete" button to remove a task.


API Endpoints
The application exposes the following API endpoints:

	/api/tasks/	        GET	    Fetch all tasks.
	/api/tasks/<id>/	GET	    Fetch a single task by ID.
	/api/tasks/	        POST	    Add  a new task.
	/api/tasks/<id>/	PUT	    Update a task by ID.
	/api/tasks/<id>/	DELETE	    Delete a task by ID.


Acknowledgments
	Django
	MySQL
	JavaScript

