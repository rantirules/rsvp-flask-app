# Event RSVP and Guest List Organizer
<p text-align="center"> <strong> Welcome to the Event RSVP and Guest List Organizer! RSVP for our upcoming event and let us know how many guests you're bringing! </strong></p>

This repository contains the source code for an event management web application. Users can RSVP for upcoming events, indicate the number of guests they're bringing, and provide any special requests or dietary restrictions. The application is built using Flask and integrates with a database to store RSVP information.



<img width="1000" alt="image" src="https://github.com/rantirules/rsvp-flask-app/assets/13412593/c8ee3c47-8247-4700-bc66-0dc8006b1e59">
<!-- <img width="500" alt="image" src="https://github.com/rantirules/rsvp-flask-app/assets/13412593/ba6ddc7a-95cf-4f63-9422-ddcc6d70381b"> -->


## Getting Started
To run the project, follow these steps:

1. <strong>Navigate to the Project Directory:</strong>

```
cd /path/to/event-rsvp-organizer
```
2. **Activate the Virtual Environment:**


```bash
pipenv shell
```
3. **Install Dependencies:**


```
pipenv install -r requirements.txt
```
4. **Run the Development Server:**


```
pipenv run dev
```
This will start the development server, and you can access the application at http://127.0.0.1:5000.

## Other considerations
Make sure .env file is in application directory like so

```bash
├── Pipfile
├── Pipfile.lock
├── README.md
├── app.py
├── application
│   ├── __init__.py
│   ├── .env
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   └── templates
```
Your .env file should look like the following
```
DATABASE_URL=<Your database url>
SECRET=<Generated secret>
```
Secrets can be generated by running the following commands in your shell
```bash
$ python
>>> import secrets
>>> secrets.token_hex(16)
```


## License
This project is licensed under the [MIT License](https://opensource.org/license/mit/).

Thank you for using Event RSVP and Guest List Organizer! 

Happy RSVP-ing! 🎉


