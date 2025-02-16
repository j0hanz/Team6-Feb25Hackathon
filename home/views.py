from django.shortcuts import get_object_or_404, render

from profiles.models import UserProfile


def hello_world(request):
    return render(request, 'home/home.html')


def match_profiles(request):
    gender = request.GET.get('gender')
    sexual_orientation = request.GET.get('sexual_orientation')
    age_range = request.GET.get('age_range')
    interests = request.GET.get('interests')
    profiles = UserProfile.objects.none()

    if gender or sexual_orientation or age_range or interests:
        profiles = UserProfile.objects.all()
        if gender:
            profiles = profiles.filter(gender=gender)
        if sexual_orientation:
            profiles = profiles.filter(sexual_orientation=sexual_orientation)
        if age_range:
            min_age, max_age = map(int, age_range.split('-'))
            profiles = profiles.filter(age__gte=min_age, age__lte=max_age)
        if interests:
            profiles = profiles.filter(interests=interests)

    return render(request, 'home/match.html', {'profiles': profiles})


def auto_match_profiles(request):
    user = request.user
    profiles = UserProfile.objects.none()

    if user.is_authenticated:
        profiles = UserProfile.objects.exclude(id=user.id)
        if user.interests:
            profiles = profiles.filter(gender=user.interests)
        if user.age:
            min_age = user.age - 5
            max_age = user.age + 5
            profiles = profiles.filter(age__gte=min_age, age__lte=max_age)

    return render(request, 'home/auto_match.html', {'profiles': profiles})


def user_profile(request, user_id):
    profile = get_object_or_404(UserProfile, id=user_id)
    return render(request, 'home/user-profile.html', {'profile': profile})
