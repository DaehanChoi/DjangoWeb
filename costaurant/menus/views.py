from django.shortcuts import render
from datetime import datetime
from django.http import Http404

# Create your views here.
def index(request):
    today = datetime.now().date()
    context = {'today': today}
    return render(request, 'menus/index.html', context)


def detail(request, menu):
    context = {'name' : 'chicken'}
    if menu == "chicken":
        return render(request, "menus/detail.html", context=context)
    else:
        raise Http404("이런건없음")