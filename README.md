# WageDaily

WageDaily is a web platform that connects employers with daily wage workers, facilitating job postings and bookings in a streamlined manner.
![](static/img2)
## Overview

WageDaily aims to solve the problem of connecting daily wage workers with potential employers. The platform allows employers to post job requests with details such as job type, location, wage, and number of workers required. Workers can then browse these opportunities and book jobs that match their skills and preferences.

## Screenshots
![img](assets/1.png)
![img](assets/2.png)

## Features

- **User Authentication**: Secure signup and login functionality
- **Job Request Management**: Create, view, and manage job requests
- **Dashboard**: Personalized dashboard for users
- **Booking System**: Simple process for workers to book available jobs
- **Responsive Design**: Works on desktop and mobile devices

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Frontend**: HTML, CSS, JavaScript
- **Containerization**: Docker

## Installation & Setup

### Prerequisites
- Python 3.8+
- Docker and Docker Compose (for containerized setup)
- PostgreSQL (if running locally without Docker)

### Local Development Setup

1. Clone the repository
   ```bash
   git clone https://your-repository-url/wage-daily.git
   cd wage-daily
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Set environment variables (if needed)
   ```bash
   # On Windows
   set DATABASE_URL=postgresql://username:password@localhost:5432/wagedaily
   # On macOS/Linux
   export DATABASE_URL=postgresql://username:password@localhost:5432/wagedaily
   ```

5. Run the application
   ```bash
   python app.py
   ```
   The application will be available at http://localhost:5001

### Docker Setup

1. Build and start the containers
   ```bash
   docker-compose up -d
   ```
   The application will be available at http://localhost:5001

## Project Structure

```
wage-daily/
│
├── .dist/                 # Distribution files
├── .venv/                 # Virtual environment
├── static/                # Static files (CSS, JS, images)
├── templates/             # HTML templates
│   ├── about.html
│   ├── add_request.html
│   ├── base.html
│   ├── booking_confirmed.html
│   ├── dashboard.html
│   ├── home.html
│   ├── index.html
│   ├── login.html
│   ├── request_details.html
│   └── signup.html
├── .gitattributes
├── .gitignore
├── app.py                 # Main application file
├── docker-compose.yml     # Docker configuration
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

## Usage

### For Employers
1. Create an account or log in
2. Navigate to the dashboard
3. Create a new job request with all required details
4. Track booking status of your job requests

### For Workers
1. Create an account or log in
2. Browse available job requests
3. View job details and book jobs
4. Receive confirmation of booking


## License

[MIT License](LICENSE)

## Contact

Project Link: [https://github.com/username/wage-daily](https://github.com/username/wage-daily)
