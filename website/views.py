from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages

# Create your views here.

def home(request):
 all_members = Member.objects.all()
 return render(request, 'home.html', {'all': all_members}) # here we assign the all_member with the reference name 'all' to be used in the jinger html code snippet


def join(request):
 # check if the request is a post request
 if request.method == "POST":
  # the memberform class will take in the request (or "None" if no request is given) in it's parenthesis. and then we will store the request in a variable 'form'
  form = MemberForm(request.POST or None)
  # here we will check if the request is valid and if it is, we will save it to the database
  if form.is_valid():
   form.save()
  else:
   messages.success(request, ('There was an error submitting your requset. Please try again latter'))
  # here we set the form fields as the value of each variable we want to be pesisted in the form value
   fname = request.POST['fname']
   lname = request.POST['lname']
   age = request.POST['age']
   email = request.POST['email']
   password = request.POST['password']

   context = {
    'fname': fname,
    'lname': lname,
    'age': age,
    'email': email,
    'password': password,
   }

   # to simply redirect the user to a page we can import redirect from django.shortcuts and use it here
   # return redirect('join')
   # or we can redirect the user back to the join view url and also persist the previous user input in the form using render
   return render(request, 'join.html', context)  # now we can go on to reference the context in the frontend join.html page by including each value in the form field values.
  
   # using the django inbuilt messging class we can display a message in the front end
  messages.success(request, ("Request submitted successfully!"))
  # now we need to go to the base.html page to decide where we want the message displayed in the frontend
  # here we can redirect the user back to the home page
  return redirect('home')
 else:
  return render(request, 'join.html', {})
