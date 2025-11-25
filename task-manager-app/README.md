# Task Manager App (React + Flask + MongoDB)

A full-stack task manager app using React.js for frontend and Python Flask for backend.  
MVC architecture, deployable on AWS with CI/CD pipeline.

## Features
- Add, view, delete tasks
- MVC design pattern
- MongoDB Atlas as database
- Frontend hosted on AWS S3 + CloudFront
- Backend hosted on AWS EC2
- CI/CD using GitHub Actions

## Project Structure
```
task-manager-app/
│
├── backend/
│   ├── controllers/
│   │   └── task_controller.py
│   ├── models/
│   │   └── task_model.py
│   ├── routes/
│   │   └── task_routes.py
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   └── package.json
│
├── .github/workflows/
│   └── ci-cd.yml
└── README.md

```

## Backend Setup
```bash
cd backend
pip install -r requirements.txt
export MONGO_URI=<your_mongo_uri>
python app.py
```

## Frontend Setup
```bash
cd frontend
npm install
npm start
```

### Deployment
- Frontend: AWS S3 + CloudFront
- Backend: AWS EC2 (Gunicorn + Flask)
- MongoDB: Atlas cluster

### CI/CD
- Github Actions workflow installs dependencies, runs tests, builds frontend
