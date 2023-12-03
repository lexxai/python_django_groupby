# python_django_groupby



## DJANGO реалізація.

```
> poetry init
> poetry shell
> poetry add django
> django-admin startproject groupby
> cd groupby
> python manage.py migrate
```

groupby\loganalyze\models.py:
```
class Log(models.Model):
    date = models.DateTimeField(default=timezone.now)
    host = models.CharField(max_length=128)
    request = models.CharField(max_length=128)
    username = models.CharField(max_length=128)

    class Meta:
        indexes = [
            models.Index(fields=["host"], name="host_idx")
        ]
```

```
> python manage.py makemigrations
Migrations for 'loganalyze':
  loganalyze\migrations\0001_initial.py
    - Create model Log

> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, loganalyze, sessions
Running migrations:
  Applying loganalyze.0001_initial... OK 
```

