import os
import sys
import site

sys.stdout = sys.stderr

# Remember original sys.path.
prev_sys_path = list(sys.path)
site.addsitedir(os.path.abspath(os.path.join(os.path.dirname(__file__))))
site.addsitedir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
site.addsitedir(os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '..',
    'env',
    'lib',
    'python2.7',
    'site-packages'
)))

# Reorder sys.path so new directories at the front.
new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path[:0] = new_sys_path

os.environ['PYTHON_EGG_CACHE'] = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'eggcache'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
