from django.shortcuts import render
from .models import Log

# Create your views here.
def main(request):
    # data = Log.objects.all()
    # data = Log.objects.filter(username__exact = "user1")
    data = Log.objects.raw("SELECT x.* FROM loganalyze_log x WHERE x.username = %s GROUP BY x.host", ["user1"])
    context=  {"data":data}
    return render(request, 'loganalyze/index.html', context=context)
