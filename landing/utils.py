from django.contrib.sessions.backends.db import SessionStore


def create_session(request, user_pk):
    '''CREATE SESSION IN DB'''
    s = SessionStore()
    s['user_pk'] = user_pk
    s.create()
    request.session['session_login'] = s.session_key
    print('Created db session key: {0} \n USER_PK: {1}'.format(s.session_key, s['user_pk']))
    print('Created cookie session key: {0}'.format(request.session.session_key))


def get_dbsession(cookie_session):
    s = SessionStore(session_key=cookie_session)
    return s

'''CREATE CUSTOM COOKIE'''
# cresponse = HttpResponse(template.render(context, request))
# cresponse.set_cookie('logged_in_status', 'never_use_this_ever')
# return cresponse