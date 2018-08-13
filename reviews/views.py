from django.shortcuts import render


def reviews(request):
    '''
    :param request: get request which has user on db session stored in session cookie
    :return: main page with correct user after authenticate session
    '''
    return render(request, 'reviews/reviews.html')
