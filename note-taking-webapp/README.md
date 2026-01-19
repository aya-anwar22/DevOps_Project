# Note-Taking Web App - DevOps Project

##  Project Overview
This project is a **note-taking web application** deployed on an AWS EC2 instance running RHEL 10.  
It demonstrates real-world **DevOps practices**, including infrastructure setup, database configuration, web server deployment, and automated backup.

The project was developed as part of the **Digital Egypt Pioneers Initiative**.

---

##  Tech Stack
- **Backend:** Python (Flask)
- **Database:** MariaDB
- **Web Server:** Nginx
- **OS:** RHEL 10 (EC2 t2.micro)
- **Backup:** EBS volume mounted on `/backup`
- **Deployment Tools:** Bash scripts, environment variables, Git

---

##  Project Structure


note-taking-webapp/
│
├── app/
│   ├── **__init__**.py
│   ├── run.py
│   ├── config.py
│   ├── models.py
│   ├── routes.py
│   └── templates/
│       └── index.html
│
├── scripts/
│   ├── install_mariadb.sh
│   ├── backup_db.sh
│   └── setup_server.sh
│
├── nginx/
│   └── flask_app.conf
│
├── database/
│   └── schema.sql
│
├── screenshots/
│   ├── app_running.png
│   ├── backup_volume.png
│   └── mariadb_data.png
│
├── requirements.txt
├── .env
├── README.md
└── LICENSE

````

---

##  Project Objectives
1. Deploy a Flask web application on an EC2 instance.
2. Configure a MariaDB database and connect it to the web app.
3. Implement Nginx as a reverse proxy for the Flask app.
4. Mount an EBS volume and automate database backups.
5. Demonstrate real-world DevOps practices including scripts, environment variables, and structured deployment.

---

##  Setup Instructions

### 1. EC2 & RHEL Setup
- Launch EC2 t2.micro with **RHEL 10**
- Open ports **22 (SSH)** and **80 (HTTP)**
- SSH into the instance using your key pair

### 2. Install Dependencies
```bash
# Make scripts executable
chmod +x scripts/*.sh

# Run setup script
./scripts/setup_server.sh
````

### 3. Install MariaDB

```bash
./scripts/install_mariadb.sh
```

* Create database and tables using `database/schema.sql`
* Update `.env` file with DB credentials

### 4. Run Flask App

```bash
cd app
pip install -r ../requirements.txt
export FLASK_APP=app.py
flask run --host=0.0.0.0
```

### 5. Configure Nginx

* Place `nginx/flask_app.conf` in `/etc/nginx/conf.d/`
* Reload Nginx: `sudo systemctl reload nginx`

### 6. Backup Setup

* Create and attach EBS volume
* Mount it to `/backup`
* Run backup script manually or via cron:

```bash
./scripts/backup_db.sh
```

---

##  Example Usage

**User Input:**

```
[ Write your note here... ]
[ Save Note ]
```
