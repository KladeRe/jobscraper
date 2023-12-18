# Full stack application using Nextjs, Django and SQLite3.
To run the application you need to first make an empty database file in the job-api directory called "sb.sqlite3"

You can run the application using the command:

For windows
`docker-compose build`
`docker-compose up`

For Mac/Linux
`docker compose build`
`docker compose up`

Obs!
You might need root privileges to run the application.

The application runs on port 3000

In case you want to make this application update once per day it is recommeded to use a scheduling tool
for example cron (Linux) or Task Scheduler (Windows)
In Linux one example could be

`crontab -e`
Add the following line to run the script every day at a specific time (e.g., 2:00 AM)
0 2 * * * /path/to/your/run.sh

