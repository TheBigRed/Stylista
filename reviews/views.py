from django.shortcuts import render
from .models import Review

def reviews(request):
    '''
    :param request: reviews
    :return: page with reviews for Stylist
    '''

    reviews_list = Review.objects.filter(stylist_id=10)
    for r in reviews_list:
        print("Review Name: {}".format(r.title))

    return render(request, 'reviews/reviews.html', {'reviews_list': reviews_list})
