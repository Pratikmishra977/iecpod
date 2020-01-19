from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm, EducationUpdateForm

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        e_form = EducationUpdateForm(request.POST, instance=request.user.student_education )
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.student_detail)
        if u_form.is_valid() and p_form.is_valid() and e_form.is_valid():
            u_form.save()
            p_form.save()
            e_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('user:user_profile:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.student_detail)
        e_form = EducationUpdateForm(instance=request.user.student_education)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'e_form': e_form
    }

    return render(request, 'profile.html', context)

