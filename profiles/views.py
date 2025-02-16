from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProfileImageForm, UserProfileChangeForm
from .models import ProfileImage


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


def gallery_page(request):
    if request.method == 'POST':
        if 'delete_image' in request.POST:
            image_id = request.POST.get('image_id')
            image = get_object_or_404(
                ProfileImage, id=image_id, user=request.user
            )
            image.delete()
            messages.success(request, 'Image deleted successfully.')
            return redirect('gallery')
        else:
            form = ProfileImageForm(request.POST, request.FILES)
            if form.is_valid():
                profile_image = form.save(commit=False)
                profile_image.user = request.user
                profile_image.save()
                messages.success(request, 'Image uploaded successfully.')
                return redirect('gallery')
            else:
                messages.error(request, 'Please correct the error below.')
    else:
        form = ProfileImageForm()
    images = request.user.gallery_images.all()
    return render(
        request, 'profiles/gallery.html', {'form': form, 'images': images}
    )


def profile_page_view(request):
    return render(request, 'profiles/profile-page.html')
