import re


class MobileDetectionMiddleware(object):
    """
    Useful middleware to detect if the user is
    on a mobile device.
    http://djangosnippets.org/snippets/2001/
    """

    def process_request(self, request):

        if request.GET.get('cordova', None):
            if request.GET.get('cordova') == 'true':
                request.session['cordova'] = True
            else:
                request.session['cordova'] = False

        if request.session.get('cordova', False):
            request.is_cordova = True
            #print "is_cordova = True"
        else:
            request.is_cordova = False
            #print "is_cordova = False"

        is_mobile = False

        if request.META.has_key('HTTP_USER_AGENT'):
            user_agent = request.META['HTTP_USER_AGENT']

            pattern = "(ipad|iphone)"
            prog = re.compile(pattern, re.IGNORECASE)
            match = prog.search(user_agent)
            if match:
                request.is_ios = True
                #print "is_ios = True"
            else:
                request.is_ios = False
                #print "is_ios = False"

            pattern = "(android)"
            prog = re.compile(pattern, re.IGNORECASE)
            match = prog.search(user_agent)
            if match:
                request.is_android = True
                #print "is_android = True"
            else:
                request.is_android = False
                #print "is_android = False"


            # Test common mobile values.
            pattern = "(up.browser|up.link|mmp|ipad|android|symbian|smartphone|midp|wap|phone|windows ce|pda|mobile|mini|palm|netfront)"
            prog = re.compile(pattern, re.IGNORECASE)
            match = prog.search(user_agent)

            if match:
                is_mobile = True
            else:
                # Nokia like test for WAP browsers.
                # http://www.developershome.com/wap/xhtmlmp/xhtml_mp_tutorial.asp?page=mimeTypesFileExtension

                if request.META.has_key('HTTP_ACCEPT'):
                    http_accept = request.META['HTTP_ACCEPT']

                    pattern = "application/vnd\.wap\.xhtml\+xml"
                    prog = re.compile(pattern, re.IGNORECASE)

                    match = prog.search(http_accept)

                    if match:
                        is_mobile = True

            if not is_mobile:
                # Now we test the user_agent from a big list.
                user_agents_test = ("w3c ", "acs-", "alav", "alca", "amoi", "audi",
                                    "avan", "benq", "bird", "blac", "blaz", "brew",
                                    "cell", "cldc", "cmd-", "dang", "doco", "eric",
                                    "hipt", "inno", "ipaq", "java", "jigs", "kddi",
                                    "keji", "leno", "lg-c", "lg-d", "lg-g", "lge-",
                                    "maui", "maxo", "midp", "mits", "mmef", "mobi",
                                    "mot-", "moto", "mwbp", "nec-", "newt", "noki",
                                    "xda",  "palm", "pana", "pant", "phil", "play",
                                    "port", "prox", "qwap", "sage", "sams", "sany",
                                    "sch-", "sec-", "send", "seri", "sgh-", "shar",
                                    "sie-", "siem", "smal", "smar", "sony", "sph-",
                                    "symb", "t-mo", "teli", "tim-", "tosh", "tsm-",
                                    "upg1", "upsi", "vk-v", "voda", "wap-", "wapa",
                                    "wapi", "wapp", "wapr", "webc", "winw", "winw",
                                    "xda-",)

                test = user_agent[0:4].lower()
                if test in user_agents_test:
                    is_mobile = True

        request.is_mobile = is_mobile
