# python_django_groupby

![](doc/db_01.png)


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

## Import DATA. DBeaver

![](doc/db_02.png)

Add index.template: groupby\loganalyze\templates\loganalyze\index.html

## Django view

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index GroupBy</title>
</head>
<body>
  <h1>HELLO GroupBy</h1>
</body>
</html>
```


groupby\loganalyze\views.py:
```
from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, 'loganalyze/index.html')
```

groupby\loganalyze\urls.py:

```
from django.urls import path
from . import views

app_name = 'loganalyze'

urlpatterns = [
    path('', views.main, name='main'),
]
```

groupby\groupby\urls.py:

```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('loganalyze.urls')),
]
```

```
> python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 03, 2023 - 19:38:03
Django version 4.2.7, using settings 'groupby.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

![](doc/web-01.png)

Tune view:
```
from django.shortcuts import render
from .models import Log

# Create your views here.
def main(request):
    data = Log.objects.all()
    context=  {"data":data}
    return render(request, 'loganalyze/index.html', context=context)
```

Tune template:
```
  <table class="table table-sm table-bordered table-striped col-auto">
    <thead>
      <tr>
        <th scope="col">id</th>
        <th scope="col">date</th>
        <th scope="col">host</th>
        <th scope="col">request</th>
        <th scope="col">username</th>
      </tr>
    </thead>
    <tbody>
      {% for row in data %}
      <tr>
        <th scope="row">{{row.id}}</td>
        <td>{{row.date}}</td>
        <td>{{row.host}}</td>
        <td>{{row.request}}</td>
        <td>{{row.username}}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
```

![](doc/web-02.png)

View, search username "user1":
```
    data = Log.objects.filter(username__exact = "user1")
```

![](doc/web-03.png)


View, search username "user1" and group by "host" by use Django raw sql request:
```
    data = Log.objects.raw("SELECT x.* FROM loganalyze_log x WHERE x.username = %s GROUP BY x.host", ["user1"])

```

![](doc/web-04.png)
