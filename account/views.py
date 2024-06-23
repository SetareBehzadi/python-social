from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import views as auth_view
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse, reverse_lazy

from account.forms import UserRegistrationForm, UserLoginForm
from follow.models import Relation
from post.models import Post


class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'account/register.html'

    def __init__(self, **kwargs):
        super().__init__(kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, 'You have been already logged in.')
            return redirect('home:home')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        template_name = ''

        if form.is_valid():
            clean_data_form = form.cleaned_data
            User.objects.create_user(clean_data_form['username'], clean_data_form['email'],
                                     clean_data_form['password'], )
            messages.success(request, 'You registered successfully', 'success')
            return redirect('home:home')
        else:
            return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get('next')
        return super().setup(self, request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'successful')
                if self.next:
                    return redirect(self.next)
                return redirect('home:home')
            messages.error(request, 'something is wrong', 'warning')
            return render(request, self.template_name, {'form': form})


class UserLogoutView(LoginRequiredMixin, View):
    # login_url = "/account/login"
    def get(self, request):
        logout(request)
        messages.success(request, 'you logged out successfully', 'successful')
        return redirect('home:home')


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        is_follow= False
        relation = Relation.objects.filter(from_user=request.user, to_user= user)
        if relation.exists():
            is_follow = True

        return render(request, 'account/profile.html', {'user': user, 'is_follow':is_follow})


class UserPasswordResetView(auth_view.PasswordResetView):
    template_name = 'account/password_reset_form.html'
    success_url = reverse_lazy('account:password_reset_done')
    email_template_name = 'account/password_reset_email.html'

class UserPasswordResetDoneView(auth_view.PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'


class UserPasswordResetConfirmView(auth_view.PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy('account:password_reset_complete')


class UserPasswordResetCompleteView(auth_view.PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'
