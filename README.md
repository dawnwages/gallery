# GALLERY APP
Refer to [Notes](notes.md) for progress updates, next steps and thoughts on mini assigment. This took ~18 hours to create, with more time I'd build out more features.

This is a proof of concept from [feature instructions](/gallery/Features_README.md) describing a gallery to display from given [JSON](/gallery/data.json).

- Python
- Django
- Vue (CDN)

## Installation
- clone repo `https://github.com/dawnwages/gallery.git` 
- `virtualenv --python=python3 venv`
- `pip install --upgrade pip`
- `pip install requirements.txt` * this app is run on wagtail - which is not a necessary requirement in its current state.
- cd into `gallery` directory and run `.manage.py createsuperuser` to create a admin user
- cd into `gallery` directory and run `./manage.py runserver`
- app will be running at [http://localhost:8000/](http://localhost:8000/)
- app will be running at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

#### www.dawnwages.info/apps