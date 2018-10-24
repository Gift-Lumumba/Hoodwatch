from django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignupForm,AddHoodForm,AddBusinessForm,UpdateProfileForm,PostForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .models import Neighbourhood,Business,Profile,Join,Posts,Comments
import datetime as dt
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
  '''
  View function that renders the homepage
  '''
  neighbourhoods = Neighbourhood.objects.all()
  return render(request,'index.html',locals())
  # if request.user.is_authenticated:
  #   if Join.objects.filter(user_id = request.user).exists():
  #     neighbourhoods = Neighbourhood.objects.get(pk = request.user.join.hood_id.id)
  #     posts = Posts.objects.filter(hood = request.user.join.hood_id.id)
  #     businesses = Business.objects.filter(neighbourhood=request.user.join.hood_id.id)
  #     return render(request,'index.html',locals())

  #   else:
  #     neighbourhoods = Neighbourhood.objects.all()
  #     return render(request,'index.html',locals())
  # else:
  #   neighbourhoods = Neighbourhood.objects.all()
  #   return render(request,'index.html',locals())

@login_required(login_url='/accounts/login/')
def search_business(request):
  
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        businesses = Business.objects.filter(name__icontains = search_term,hood = request.user.join.hood_id.id)
        searched_businesses = Business.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',locals())

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',locals())
# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             mail_subject = 'Activate your Hoodwatch account.'
#             message = render_to_string('registration/activate_account.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid':urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token':account_activation_token.make_token(user),
#             })
#             to_email = form.cleaned_data.get('email')
#             email = EmailMessage(
#                         mail_subject, message, to=[to_email]
#             )
#             email.send()
#             return HttpResponse('Please confirm your email address to complete the registration')
#     else:
#         form = SignupForm()
#     return render(request, 'registration/signup.html', {'form': form})


# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         return HttpResponse('Thank you for your email confirmation. Now you can login your account.''<a href="/accounts/login/"> click here </a>')
#     else:
#         return HttpResponse('Activation link is invalid!')

@login_required(login_url='/accounts/login/')
def add_hood(request):
	'''
	View function that enables users to add hoods
	'''
	if request.method == 'POST':
		form = AddHoodForm(request.POST)
		if form.is_valid():
			neighbourhood = form.save(commit = False)
			neighbourhood.user = request.user
			neighbourhood.save()
			messages.success(request, 'You Have succesfully created a hood.You may now join your neighbourhood')
			return redirect('home')

	else:
		form = AddHoodForm()
		return render(request,'add_hood.html',locals())

@login_required(login_url='/accounts/login/')
def join_hood(request,hood_id):
	'''
	View function that enables users join a hood
	'''
	neighbourhood = Neighbourhood.objects.get(pk = hood_id)
	if Join.objects.filter(user_id = request.user).exists():
		
		Join.objects.filter(user_id = request.user).update(hood_id = neighbourhood)
	else:
		
		Join(user_id=request.user,hood_id = neighbourhood).save()

	messages.success(request, 'Success! You have succesfully joined this Neighbourhood ')
	return redirect('index')

def home(request):
  '''
  View function that renders users neighbourhood
  '''
  neighbourhoods = Neighbourhood.objects.filter(user=request.user)
  return render(request,'home.html',locals())

@login_required(login_url='/accounts/login/')
def edit_hood(request,hood_id):
	'''
	View function that enables a user to edit his/her neighbourhood details
	'''
	neighbourhood = Neighbourhood.objects.get(pk = hood_id)
	if request.method == 'POST':
		form = AddHoodForm(request.POST,instance = neighbourhood)
		if form.is_valid():
			form.save()
			messages.success(request, 'Neighbourhood edited successfully')
			
			return redirect('index')
	else:
		form = AddHoodForm(instance = neighbourhood)
		return render(request,'edit_hood.html',locals())

@login_required(login_url='/accounts/login/')
def leave_hood(request,id):
  '''
  Views that enables users leave a neighbourhood
  '''
  Join.objects.get(id = request.user.id).delete()
  return redirect('index')

@login_required(login_url='/accounts/login/')
def add_business(request):
	'''
	View function that enables users to add businesses
	'''
	if request.method == 'POST':
		form = AddBusinessForm(request.POST)
		if form.is_valid():
			business = form.save(commit = False)
			business.user = request.user
			business.save()
			messages.success(request, 'You Have succesfully created a hood.You may now join your neighbourhood')
			return redirect('added_businesses')

	else:
		form = AddBusinessForm()
		return render(request,'add_business.html',locals())

@login_required(login_url='/accounts/login/')
def added_businesses(request):
	'''
	View function that returns all added user businesses
	'''
	businesses= Business.objects.filter(user = request.user)
	return render(request,'businesses.html',locals())

@login_required(login_url='/accounts/login/')
def edit_business(request,business_id):
	'''
	View function that enables a user to edit his/her added businesses
	'''
	business = Business.objects.get(pk = business_id)
	if request.method == 'POST':
		form = AddBusinessForm(request.POST,instance = business)
		if form.is_valid():
			form.save()
			return redirect('added_businesses')
	else:
		form = AddBusinessForm(instance = business)
	return render(request,'edit_business.html',locals())

@login_required(login_url='/accounts/login/')
def profile(request):
	'''
	View profile that renders a user's profile page
	'''
	profile = Profile.objects.get(user = request.user)
  
	return render(request,'profile/profile.html',locals())

@login_required(login_url='/accounts/login/')
def update_profile(request):
	'''
	View function that enables a user to update their profile
	'''
	profile = Profile.objects.get(user = request.user)
	if request.method == 'POST':
		form = UpdateProfileForm(request.POST,instance = profile )
		if form.is_valid():
			form.save()
			messages.success(request, 'Successful profile edit!')
			return redirect('profile')
	else:
		form = UpdateProfileForm(instance = profile )
		return render(request,'profile/update_profile.html',locals())

@login_required(login_url='/accounts/login/')
def add_post(request):
  '''
  View function that enables a user to create a post in a neighbourhood
  '''
  if Join.objects.filter(user_id=request.user).exists():
    if request.method == 'POST':
      form = PostForm(request.POST)
      if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.hood = request.user.join.hood_id
        post.save()
        return redirect('index')

    else:
      form = PostForm()
      return render(request,'add_post.html',locals())
  else:
    messages.error(request,'Error!!Post can only be added after joining a neighbourhood!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def posts(request):
  '''
  View function that renders the posts page
  '''
  posts = Posts.objects.filter(user = request.user)
  return render(request,'posts.html',locals())

@login_required(login_url='/accounts/login')
def edit_post(request,post_id):
  '''
  View function that enables users edit their posts
  '''
  if Join.objects.filter(user_id=request.user).exists():
    post = Posts.objects.get(id=post_id)
    if request.method == 'POST':
      form = PostForm(request.POST,instance = post)
      if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.hood = request.user.join.hood_id
        post.save()
        return redirect('posts')
    else:
      form = PostForm(instance = post)
      return render(request,'edit_post.html',locals())

  else:
    messages.error(request,'You cannot edit this post...Join a neighbourhood first')
    return HttpResponseRedirect(request.META.get('HTTP REFERER'))  

@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'neighbourhood' in request.GET and request.GET["neighbourhood"]:
        search_term = request.GET.get("neighbourhood")
        searched_neighbourhoods = Neighbourhood.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"neighbourhood": searched_neighbourhoods})

    else:
        message = "You haven't searched for any neighbourhood"
        return render(request, 'search.html',{"message":message})

def delete_hood(request,hood_id):
  '''
  View function that enables deletion of hoods
  '''
  Neighbourhood.objects.filter(pk=hood_id).delete()
  messages.error(request,'Neighbourhood has been deleted successfully')
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_post(request,post_id):
  '''
  View function that enables a post to be deleted
  '''
  Posts.objects.filter(pk=post_id).delete()
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_business(request,business_id):
  '''
  View function that enables a business to be deleted
  '''
  Business.objects.filter(pk=business_id).delete()
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))