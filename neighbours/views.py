
from django.shortcuts import render, redirect, get_object_or_404

# from django.core.mail import EmailMessage
# from .tokens import account_activation_token
# from django.utils.encoding import force_bytes, force_text
# from django.http import HttpResponse
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.contrib.sites.shortcuts import get_current_site
# from django.contrib.auth import login, authenticate
# importing login as auth_login to prevent clashing with inbuilt view
from django.contrib.auth import login as auth_login

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from .models import Profile, Neighbourhood, Business, Post

# import forms
from .forms import SignUpForm, EditProfileForm, NeighbourhoodForm, CreatebizForm, PostForm

# Create your views here.


# Home view function
def Home(request):

    hoods = Neighbourhood.objects.all()
    return render(request, 'home.html', locals())


# SIGNUP VIEW FUNCTION
def signup(request):
    """
    signup form view function
    """
    # checking if request method is a post
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        # form validation
        if form.is_valid():
            # saving user credentials and creating uer instance  if form is valid
            user = form.save()


            # # mail confirmation
            # current_site = get_current_site(request)
            # mail_subject = 'Activate your JIRANI account'
            # message = render_to_string('acc_active_email.html',
            #                            {
            #                             'user':user,
            #                             'domain': current_site.domain,
            #                             'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #                             'token': account_activation_token.make_token(user),
            #
            #                            })
            # to_email = form.cleaned_data.get('email')
            # email = EmailMessage(mail_subject, message, to =[to_email])
            # email.send()
            # auth_login(request, user)
            # return HttpResponse('Please confirm your email address to complete registration')

            # user passed as argument to auth_login function
            auth_login(request, user)
            return redirect('edit_profile')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})


# activate function
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
#         # return redirect('home')
#         return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
#     else:
#         return HttpResponse('Activation link is invalid!')


# edit profile view function
@login_required(login_url='/registration/login/')
def profile_edit(request):
    """
    view function to render profile

    """
    form = EditProfileForm()
    current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=current_user.profile)
        if form.is_valid():
            form.save()

            return redirect('profile')

    return render(request, 'Profile/profile_edit.html', {'form': form})


# profile view function
@login_required(login_url='/registration/login/')
def profile(request):
    """
    view function to render profile

    """
    current_user = request.user
    profile = Profile.objects.get(user = current_user)
    return render(request, 'Profile/profile.html', {'profile': profile})


# search for business in neighbourhood
def search_biz(request):
    if 'neighbourhood' in request.GET and request.GET["neighbourhood"]:
        search_term =request.GET.get("neighbourhood")
        searched_biz = Neighbourhood.search_business_hood(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message, "Neighbourhood":searched_biz})

    else:
        message ="Enter Business to Search For"
        return render(request, "search.html", {"message":message})


@login_required(login_url='/registration/login/')
def create_hood(request):
    """
    view function to create hood
    :param request:
    :return:
    """
    if request.method == 'POST':
        nform = NeighbourhoodForm(request.POST, request.FILES)
        if nform.is_valid():
            n = nform.save(commit=False)
            n.admin = request.user.profile
            request.user.profile.save()
            n.save()
            return redirect('hood')
    else:
        nform = NeighbourhoodForm()
    return render(request, 'createhood.html', {'nform': nform})


@login_required()
def create_post(request):
    """
    view function to create posts
    :param request:
    :return:
    """
    if request.method == 'POST':
        pform = PostForm(request.POST)
        if pform.is_valid():
            p = pform.save(commit=False)
            p.user = request.user.profile
            p.neighbourhood = request.user.profile.neighbourhood
            p.save()
            return redirect('neighbourhood')
    else:
        pform = PostForm
    return render(request, 'post.html', locals())


@login_required()
def createbiz(request):
    """
    create business function
    :param request:
    :return:
    """
    if request.method == 'POST':
        bform = CreatebizForm(request.POST, request.FILES)
        if bform.is_valid():
            b = bform.save(commit=False)
            b.user = request.user.profile
            b.neighbourhood = request.user.profile.neighbourhood
            b.save()
            return redirect('neighbourhood')
    else:
        bform = CreatebizForm()
    return render(request, 'createbiz.html', locals())


def neighbourhood(request, neighbourhood_id):
    """
    view function to render neighbourhood

    """
    hood = Neighbourhood.find_neighbourhood(neighbourhood_id)
    bsns = Business.find_business(neighbourhood_id)
    post = Post.objects.filter(id=neighbourhood_id)
    return render(request, 'neighbourhood.html', {"hood":hood, "neighbourhood_id":neighbourhood_id, "bsns":bsns, "post":post})


@login_required(login_url='/registration/login/')
def enter_hood(request, neighbourhood_id):
    hood = get_object_or_404(Neighbourhood, pk=neighbourhood_id)
    request.user.profile.neighbourhood = hood
    request.user.profile.save()
    return redirect('neighbourhood')


@login_required(login_url='/registration/login/')
def exit_hood(request, neighbourhood_id):
    hood = get_object_or_404(Neighbourhood, pk=neighbourhood_id)
    if request.user.profile.neighbourhood == hood:
        request.user.profile.neighbourhood = None
        request.user.profile.save()
    return redirect('home')
