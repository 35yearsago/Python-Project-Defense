from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model, update_session_auth_hash
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from .models import Profile, AddGames, GiftCards, AddExpert, AddKeys
from .forms import ProfileModelForm, AddGamesModelForm, GiftCardsModelForm, AddExpertModelForm, AddKeysModelForm, \
    ProfileEditForm, ProfileAndPasswordForm, UserDeleteForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
import logging
from django.views import generic as views, View
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views

UserModel = get_user_model()


# Create your views here.

# class RegisterUserView(views.CreateView):
#     template_name = 'web/register.html'
#     form_class = auth_forms.UserCreationForm
#
#
# class LogUserView(views.View):
#     pass
#
#
# class LogoutUserView(views.View):
#     pass


def home_page(request):
    return render(request, "web/home.html")


def index_page(request):
    return render(request, "web/index.html")


logger = logging.getLogger(__name__)


# class MyLoginView(LoginView):
#     template_name = 'login.html'
#     success_url = reverse_lazy('profile')

def login_page(request):
    if request.method == 'POST':
        print(request.POST)  # Print the POST data for debugging
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print("User:", user)
        print("Is authenticated:", user.is_authenticated if user else None)
        print(username, password)
        if user is not None:
            login(request, user)
            print("User logged in:", user)
            logger.info(f"User logged in: {user}")
            return redirect('index page')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 'web/login.html')


def about_page(request):
    return render(request, "web/about.html")


def about_nop_page(request):
    return render(request, "web/about_nop.html")


def profile_create_page(request):
    if request.method == 'POST':
        form = ProfileModelForm(request.POST)
        if form.is_valid():
            new_user = User(username=form.cleaned_data['username'],
                            email=form.cleaned_data['email'])
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

            # Authenticate and log in the user
            user = authenticate(request, username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('index page')

    else:
        form = ProfileModelForm()

    context = {
        "form": form
    }

    return render(request, 'web/register.html', context=context)


# @login_required
# def profile_edit_and_change_password(request):
#     if request.method == 'POST':
#         form = ProfileAndPasswordForm(request.POST, instance=request.user)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important to update the session
#             messages.success(request, 'Your profile and password were successfully updated!')
#             return redirect('profile_edit_and_change_password')  # Redirect to the combined page
#     else:
#         form = ProfileAndPasswordForm(instance=request.user)
#
#     context = {
#         'form': form
#     }
#     return render(request, 'web/profile_edit.html', context)


@login_required
def profile_edit_page(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile edit page')
    else:
        form = ProfileEditForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'web/profile_edit.html', context)


# ensures that only authenticated users can access the view
@method_decorator(login_required, name='dispatch')
class ChangePasswordView(View):
    template_name = 'web/password_change.html'

    def get(self, request):
        form = PasswordChangeForm(user=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

        return render(request, self.template_name, {'form': form})


#
# @login_required
# def change_password(request):
#     if request.method == 'POST':
#         form = ChangePasswordForm(request.user, request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('profile_edit')  # Redirect to the edit profile page
#     else:
#         form = ChangePasswordForm(request.user)
#
#     context = {
#         'form': form
#     }
#     return render(request, 'web/profile_edit.html', context)


def profile_delete_page(request):
    return render(request, 'web/delete_user.html')


def profile_saved_games_page(request):
    return None


def games(request):
    return render(request, "web/games.html")


def game_info(request):
    return render(request, "web/game_info.html")


def recommended_games(request):
    return None


def trending_games(request):
    return None


def experts(request):
    return render(request, "web/experts.html")


def more_games(request):
    return render(request, "web/more_games.html")


def cart_page(request):
    return render(request, "web/cart.html")


def logout_page(request):
    logout(request)

    return redirect('logout page')


def user_welcome(request):
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email


@login_required
def delete_user(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        return redirect('home page')

    return render(request, "web/delete_user.html")


# ensures that only authenticated users can access the view
@method_decorator(login_required, name='dispatch')
class UserDeleteView(View):
    template_name = 'web/profile_edit.html'

    def get(self, request):
        form = UserDeleteForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm_delete']:
            user = request.user
            user.delete()
            return redirect('home page')

        return render(request, self.template_name, {'form': form})


def real_time_strategy(request):
    return render(request, "web/real-time-strategy.html")


def shooter(request):
    return render(request, "web/shooter.html")


# ensures that only authenticated users can access the view
@method_decorator(login_required, name='dispatch')
class ShooterView(View):
    template_name = "web/shooter.html"

    def get(self, request):
        return render(request, self.template_name)


def multiplayer_online_battle_arena(request):
    return render(request, "web/multiplayer_arena.html")


def role_playing_games(request):
    return render(request, "web/role_playing.html")


def simulation_sports(request):
    return render(request, "web/simulators.html")


def sandbox_games(request):
    return render(request, "web/sandbox.html")


class My404View(View):
    def get(self, request):
        return HttpResponseNotFound(render(request, 'web/404.html'))

    def post(self, request):
        return HttpResponseNotFound(render(request, 'web/404.html'))
