# Django/Aiogram template

## Steps

- Click [Use this template](https://github.com/malikovss/django-aiogram/generate)
- Copy [.env.example](.env.example) to `.env` and change variables to yours
- Create virtual environment and install [requirements](requirements.txt)
- Run `python manage.py migrate`
- Create super user `python manage.py createsuperuser`
- To run the bot in development run `python manage.py runbot` and `uvicorn main.asgi:application`
- To run the bot in production just run `uvicorn main.asgi:application`