from .models import Category


def menu_links(request):
    if 'admin' in request.path:
        return {}
    links = Category.objects.all()
    return dict(links=links)
