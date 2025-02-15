from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import UserProfileChangeForm


def profile_page(request):
    if request.method == 'POST':
        form = UserProfileChangeForm(
            request.POST, request.FILES, instance=request.user
        )
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your profile has been updated successfully.'
            )
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserProfileChangeForm(instance=request.user)
    return render(request, 'profiles/profile.html', {'form': form})
