from .models import HitCount


def hit_count_middleware(get_response):
    """
    Counts hit on all pages per user, except admin pages
    """

    def middleware(request):

        if not request.path.startswith('/admin'):
            user = request.user if not request.user.is_anonymous else None
            hc, created = HitCount.objects.get_or_create(path=request.path, user=user)
            if not created:
                hc.hits += 1
            hc.save()

        response = get_response(request)
        return response

    return middleware
