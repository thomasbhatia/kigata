def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods',
                         'POST, GET, PUT, PATCH, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type, X-Requested-With, Authorization, X-HTTP-Method-Override')
    response.headers.add('Access-Control-Max-Age', '1728000')
    """
    Add headers to both force latest IE rendering engine or Chrome Frame
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
    response.headers['server'] = 'KIGATA'
    return response


def before_request(request):
    return request
