
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>This is MyFirst Application")



def about(request):
    return HttpResponse("<h2>This is About Page<h2>")