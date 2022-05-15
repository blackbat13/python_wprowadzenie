Przykładowa aplikacja django oparta na tutorialu: https://docs.djangoproject.com/en/4.0/intro/tutorial01/

### Instrukcja:
- Uruchomienie: `python manage.py runserver`
- Utworzenie nowej aplikacji: `python manage.py startapp polls`
- Utworzenie migracji: `python manage.py makemigrations polls`
- Podejrzenie sql migracji: `python manage.py sqlmigrate polls 0001`
- Przeprowadzenie migracji: `python manage.py migrate`
- Utworzenie nowego administratora: `python manage.py createsuperuser`
