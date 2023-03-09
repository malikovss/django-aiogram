# Django/Aiogram template

## Steps

- Click [Use this template](https://github.com/malikovss/django-aiogram/generate)
- Copy [.env.example](.env.example) to `.env` and change variables to your
- Create virtual environment and install requirements
- Run `python manage.py migrate`
- Create super user `python manage.py createsuperuser`
- To run the bot in development run `python manage.py runbot` and `uvicorn main.asgi:application`
- To run the bot in production just run `uvicorn main.asgi:application`