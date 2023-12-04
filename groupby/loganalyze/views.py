from django.shortcuts import render
from .models import Log

# Create your views here.
def main(request):
    data = Log.objects.all()
    context=  {"data":data}
    return render(request, 'loganalyze/index.html', context=context)
