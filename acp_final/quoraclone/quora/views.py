from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import Question, Profile, Answer, Vote
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .forms import RegisterForm,QuestionForm


# @csrf_protect
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)  
#         if form.is_valid():  
#             user = authenticate(username=form.username, password=form.password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponseRedirect("/")
#                 else:
#                     return HttpResponse("You're account is disabled.")
#             else:
#                 messages.error(request, "Invalid username or password")
#                 return render(request, "quora\login.html", {})
        

#     form = LoginForm()
#     # return HttpResponse("quora\login.html",form)
#     return render(request, "quora\login.html", context={
#         "form": form
#     })


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            p = Profile(user = user)
            p.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('quora/login')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'quora/register.html', context)


def index(request):
    # list all questions
    if request.user.is_authenticated == False:
        return HttpResponseRedirect("login/")
    queryset_list = Question.objects.all().order_by("-timestamp")
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(question__icontains=query)
            | Q(description__icontains=query)
            | Q(user__user__username__icontains=query)
        ).distinct()
    #paginator = Paginator(queryset_list, 10)
    queryset = queryset_list
    page = request.GET.get("page")
    username = "Login"
    if User.is_active:
        username = User.username
    # try:
    #     queryset = paginator.page(page)
    # except PageNotAnInteger:
    #     queryset = paginator.page(1)
    # except EmptyPage:
    #     queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "page": "page",
        "username": username,
        "home": "active",
        "home_views": "blank",
        # "profile": profile,
        # "val": val,
        # "percent": percent,
        "q": Question.objects.count(),
        "a": Answer.objects.count(),
        "u": Profile.objects.count(),
        # "top": top,
    }
    messages.info(request, "test")
    return render(request, "quora\index.html", context)


def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            
            # Temporarily make an object to be add some
            # logic into the data if there is such a need
            # before writing to the database  
            question = form.save(commit = False)
 
            question.user = Profile.request.user.id
            # Finally write the changes into database
            question.save()           
            messages.success(request, f'Question saved!')    
            return redirect('quora/home')
        else:
            print("")
    else:
        form = QuestionForm()

    context = {'form': form}
    return render(request, 'quora/create_question.html', context)