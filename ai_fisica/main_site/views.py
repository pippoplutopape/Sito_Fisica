from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main_site/index.html', {
        'question':request.session["question"],
        })

def ask_ai(request):
    request.session["question"] = ""
    if request.method == 'POST':
        request.session["question"] = request.POST.get('question')
    return redirect("/")