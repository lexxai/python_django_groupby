from django.shortcuts import render
from django.db.models import Min

from .models import Log

# Create your views here.
def main(request):
    # data = Log.objects.all()
    # data = Log.objects.filter(username__exact = "user1")
    # data = Log.objects.raw("SELECT x.* FROM loganalyze_log x WHERE x.username = %s GROUP BY x.host", ["user1"])

    data0 = Log.objects.filter(username__exact = "user1")
    grouped_records = data0.values('host').distinct().annotate(min_id=Min("id")) 
    data =  Log.objects.filter(id__in=grouped_records.values_list("min_id", flat=True))

    context=  {"data":data}
    return render(request, 'loganalyze/index.html', context=context)
