from django.shortcuts import render

from .forms import UserProfileChangeForm


def profile_page(request):
    if request.method == 'POST':
        form = UserProfileChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileChangeForm(instance=request.user)
    return render(request, 'profiles/profile.html', {'form': form})
