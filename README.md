Kaviya Library - Django project (static data)
--------------------------------------------
What's included:
- Django project 'kaviya_library'
- App 'catalog' using static data (catalog/data.py) for authors and books
- Templates and static files
- Authentication: login/logout using Django's built-in views

How to run:
1. Create and activate a virtualenv with Python 3.11+.
2. Install requirements: pip install -r requirements.txt
3. Run migrations (required for auth/admin): python manage.py migrate
4. Create a superuser (optional, to use admin): python manage.py createsuperuser
5. Run server: python manage.py runserver
6. Open http://127.0.0.1:8000/catalog/

Notes:
- Book and author lists are static (catalog/data.py) so you don't need to populate DB to see content.
- Admin models exist if you want to create real Author/Book instances in DB.
