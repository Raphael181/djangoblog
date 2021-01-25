from django.shortcuts import render , redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm , UserUpdateForm , ProfileUpdateForm
from django.contrib.auth.decorators import login_required



def register(request):
  #classes that turn into a form
  if request.method == "POST":
    form = UserRegisterForm(request.POST)
    #validating the form to get the right information
    if form.is_valid():
      #saving the user
      form.save()
      username = form.cleaned_data.get("username")
      messages.success(request, f"Your account has been created! You are now logged in")
      #redirect user back to home
      return redirect("blog-home")
  else:
    form   = UserRegisterForm()
  return render(request, 'users/register.html', {"form": form})

#the users profile
@login_required
def userprofile(request):
  if request.method == "POST":
    u_form = UserUpdateForm(request.POST , instance = request.user)
    p_form = ProfileUpdateForm(request.POST, request.FILES , instance = request.user.profile)

    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()

      messages.success(request, f"Your account has been updated!")
      return redirect('profile')


  else:
    u_form = UserUpdateForm(instance = request.user)
    p_form = ProfileUpdateForm(instance = request.user.profile)


  context = {
      'u_form': u_form,
      'p_form': p_form
  }

  return render(request, 'users/profile.html', context)

