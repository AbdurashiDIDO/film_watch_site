from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect

from apps.shared.utils.send_to_email import send_email
from apps.users.forms.reset_password import ResetPasswordEmail
from apps.users.forms.reset_password import ChangeProfilePassword


def forgot_pass_send_email(request):
    context = {}
    domain = get_current_site(request).domain
    if request.method == 'POST':
        forms = ResetPasswordEmail(request.POST)
        if forms.is_valid():
            send_email.delay(domain, forms.data.get('email'), type_='forgot_password')
            return redirect('login')
        else:
            context['errors'] = forms.errors
    return render(request, 'films/auth/forgot_password_email.html', context)


def change_profile_password(request):
    context = {}
    if request.method == 'POST':
        forms = ChangeProfilePassword(request.POST, instance=request.user)
        if forms.is_valid():
            forms.save()
        else:
            context['errors'] = forms.errors
    return render(request, 'films/user/user-profile.html', context)


