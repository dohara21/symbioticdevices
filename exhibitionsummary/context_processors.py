from .models import Summary

def sidebar(request):
    sidebar = Summary.objects.all()

    return {
        'sidebar': sidebar,
    }