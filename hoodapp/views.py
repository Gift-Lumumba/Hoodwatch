from django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import SignupForm,AddHoodForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .models import Neighbourhood,Business,Profile,JoinHood,Posts,Comments
import datetime as dt
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
  '''
  view function that renders the homepage
  '''
  if request.user.is_authenticated:
    if JoinHood.objects.filter(user_id=request.user).exists():
      neighbourhood = Neighbourhood.get_neighbourhoods().order_by('-posted_on')
      neighbourhood = Neighbourhood.objects.get(pk=request.user.join.hood_id)
      posts = Post.objects.filter(hood=request.user.join.hood_id)
      businesses = Business.objects.filter(hood=request.user.join.hood_id)
      return render(request,'home.html',locals())

    else:
      neighbourhoods = Neighbourhood.objects.all()
      return render(request,'index.html',locals())
  else:
    neighbourhoods = Neighbourhood.objects.all()
    return render(request,'index.html',locals())

def search_business(request):
  
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',locals())

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',locals())
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Hoodwatch account.'
            message = render_to_string('registration/activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.''<a href="/accounts/login/"> click here </a>')
    else:
        return HttpResponse('Activation link is invalid!')

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
			return redirect('index')

	else:
		form = AddHoodForm()
		return render(request,'add_hood.html',locals())

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