from django.shortcuts import render

from profiles.models import UserProfile


def hello_world(request):
    return render(request, 'home/home.html')


def match_profiles(request):
    gender = request.GET.get('gender')
    sexual_orientation = request.GET.get('sexual_orientation')
    profiles = UserProfile.objects.none()

    if gender or sexual_orientation:
        profiles = UserProfile.objects.all()
        if gender:
            profiles = profiles.filter(gender=gender)
        if sexual_orientation:
            profiles = profiles.filter(sexual_orientation=sexual_orientation)

    return render(request, 'home/match.html', {'profiles': profiles})
