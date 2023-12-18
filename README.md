Full stack application using Nextjs, Django and SQLite3.
To run the application you need to first make an empty database file in the job-api directory called "sb.sqlite3"
Before running the application run this command in the job-api directory:
`python3 manage.py initialize_db`
This scrapes the data from the internet so that it can be read by the frontend later. This will take a few minutes

The application is dockerized using docker compose. 

You can tun the application using the command:

For windows
`docker-compose build`
`docker-compose up`

For Mac/Linux
`docker compose build`
`docker compose up`

Obs!
You might need root privileges to run the application.

The application runs on port 3000

