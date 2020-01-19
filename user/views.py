from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
#from django.contrib.auth.password_validation import validate_password, password_validators_help_texts
from django.views.generic import View
from django.core.exceptions import ValidationError
from django.views.generic.edit import CreateView
from .forms import SignupForm, LoginForm
from django.core.mail import EmailMessage
from django.contrib.auth.models import User

class SignupFormView(View):
    form_class = SignupForm
    template_name = 'form.html'
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'join': 'active'})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            repassword = form.cleaned_data['repassword']
            if password == repassword:
                if User.objects.filter(email=email).exists():
                    return render(request, self.template_name,{'form': form, 'error_message': 'Email allready used', 'join': 'active'})
                user.set_password(password)
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                return HttpResponse('Please confirm your email address to complete the registration')
            else:
                print("////////////////////////////////////")
                return render(request, self.template_name, {'form':form, 'error_message': 'Password and Re-Password does not match', 'join': 'active'})
        else:
            return render(request, self.template_name, {'form': form, 'error_message': 'Username taken', 'join': 'active'})

        # user = authenticate(username=username, password=password)
        # if user is not None:
        #     if user.is_active:
        #         login(request, user)
        #         return redirect('index')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        return redirect('user:login')
    else:
        return HttpResponse('Activation link is invalid!')


class LoginFormView(View):
    form_class = LoginForm
    template_name = 'form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'signin':'active'})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        print()
        if User.objects.filter(username = username).exists():
            user = authenticate(username = username , password = password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('index')
            else:
                return render(request, self.template_name, {'form': self.form_class(None), 'error_message': 'Wrong Password', 'signin': 'active'})
        else:
            return render(request, self.template_name, {'form': self.form_class(None), 'error_message': 'Username not found', 'signin': 'active'})


def logout_view(request):
    logout(request)
    return redirect('index')