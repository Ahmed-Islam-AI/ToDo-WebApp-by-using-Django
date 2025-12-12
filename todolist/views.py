from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
from django.templatetags.static import static
from todolist.models import Task

# Create your views here.
def todolist(request):
    # return HttpResponse("Hello World")
    # dic = {
    #     "task": "Task 1"
    # }
    # return JsonResponse(dic)
    
    # showing the data from the 
    all_task = Task.objects.all()   
    context = {
        'page_title': 'Todo List',
        'all_task': all_task
    }


    return render(request, "todolist.html", context)   # instead of context we can also pass empty dictionary {}



def homepage(request):
    return render(request, "main.html", {}) 


def contact(request):
    return render(request, "contact.html", {})

def about(request):
    return render(request, "about.html", {})
