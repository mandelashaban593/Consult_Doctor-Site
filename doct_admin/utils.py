
from django.contrib.contenttypes.models import ContentType

from django.conf import settings

from manDoct.settings import LOCALHOST,BASE_DIR






def debug(e, txt=False, log='debug'):
    if LOCALHOST:
        if not txt:
            txt = ''
        print >> sys.stderr, 'Debuging____________________ %s' % txt
        print >> sys.stderr, e
    else:
        try:
            old_stdout = sys.stdout
            log_file = open("%slogs/%s.log" % (BASE_DIR, log), "a")
            sys.stdout = log_file
            print '%s: Debuging____________________ %s' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                           txt)
            print e
            sys.stdout = old_stdout
            log_file.close()
        except Exception, e:
            pass
