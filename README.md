# weather_app_cloud_deployment
Python backend communicating with OpenWeather API. HTML + Javascript frontend website. Test deployed to Heroku using Docker and GitHub actions.


## Main tasks and lessons learned by doing:

1. Create flask server with outbound api calls to obtain weather information

2. Add frontend static content to display weather

3. Create Docker container

4. Deploy app to Heroku

5. Continuous deployments with GitHub actions

## Skills that have been practiced:


1.Python, Flask, Jinja templating

2.Heroku

3.GitHub actions

4.Docker

5.Coding and research skills

6.Bootstrap styling


## :fire: Final production - Proof of Concept:

https://weatherapifinland.herokuapp.com


## Requirements


- Python

- Code editor of your choice

- Virtual environment (optional)

- Docker

- Heroku CLI

## Helpful Commands

- `python3 -m venv env`

- `source ENV/bin/activate`

- `pip install flask requests python-dotenv`

- `pip list`

- `export FLASK_ENV=development`

- `flask run`


### Docker:
- `pip freeze > requirements.txt`

- `docker build . -t app`

- `docker image ls`

- `docker run -p 5000:5000 --env-file .env app`


### Heroku
- `heroku login`

- `heroku git:remote -a weatherapifinland` (to connect heroku app git)

- `git add .`

- `git commit -m "added heroku.yml file"`

- `heroku create weatherapifinland` (if name is taken, choose another)

- `heroku config:set BASE_URL=https://api.openweathermap.org/data/2.5 --app weatherapifinland` (set environment variables)

- `heroku stack:set container --app weatherapifinland`

- `git push heroku master` (to Manual push to heroku - not required as we use GitHub actions, after committing your changes to git)

- `git push --force heroku develop:master` (to 'force' push code to heroku when the main code is not at git master/main)

- `git push heroku develop:main` (to push code to heroku from a git branch without force)


