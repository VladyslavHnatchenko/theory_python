import requests

urls = open("websites.txt", "r")

for url in urls:
    url = url.strip()
    req = requests.get(url)
    print(url, 'report:')

    try:
        protection_xss = req.headers['X-XSS-Protection']
        if protection_xss != '1; mode = block':
            print('X-XSS-Protection not set properly, it may be possible:', protection_xss)
    except:
        print('X-XSS-Protection not set, it may be possible')

    try:
        options_content_type = req.headers['X-Content-Type-Options']
        if options_content_type != 'nosniff':
            print('X-Content-Type-Options not set properly:', options_content_type)
    except:
        print('X-Content-Type-Options not set')

    try:
        transport_security = req.headers['Strict-Transport-Security']
    except:
        print('HSTS header not set properly, Man in the middle attacks is possible')

    try:
        content_security = req.headers['Content-Security-Policy']
        print('Content-Security-Policy set:', content_security)
    except:
        print('Content-Security-Policy missing')
# ------------------------------------------------------------------- #
# request = requests.get("https://www.python.org/")
#
# header_list = [
#     'Server', 'Date', 'Via', 'X-Powered-By', 'X-Country-Code',
#     'Connection', 'Content-Length'
# ]
#
# for header in header_list:
#     try:
#         result = request.header_list[header]
#         print('%s: %s' % (header, result))
#     except Exception as err:
#         print('%s: No Details Found' % header)

# ------------------------------------------------------------------- #
# method_list = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'TRACE', 'TEST']
#
# for method in method_list:
#     req = requests.request(method, "http://net-informations.com/python/iq/is.htm")
#     print(method, req.status_code, req.reason)
#
#     if method == 'TRACE' and 'TRACE / HTTP/1.1' in req.text:
#         print("Cross Site Tracing(XST) is possible")


# https://www.python.org/
# http://net-informations.com/python/iq/is.htm
