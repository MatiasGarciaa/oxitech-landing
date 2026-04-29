from django.shortcuts import render


def landing(request):
    """Landing page principal de Óxitech."""
    return render(request, "oxitech/landing.html")
