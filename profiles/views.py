from django.shortcuts import render


def profile(request):
    """ Display the profile for user """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
