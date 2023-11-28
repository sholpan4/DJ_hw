import subprocess
import os


project_name = "hw_project"
subprocess.run(["django-admin", "startproject", project_name])

os.chdir("hw_project")
subprocess.run(["python", "manage.py", "runserver"])

subprocess.run(["python", "-m", "venv", "env"])

subprocess.run(["pip", "freeze", ">", "requirements.txt"], shell=True)