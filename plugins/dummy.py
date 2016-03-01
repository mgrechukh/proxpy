def proxy_mangle_request(req):
    print req
    return req

def proxy_mangle_response(res, req):
    print req, res
    return res
