
from whitenoise import WhiteNoise

from my_project import MyWSGIApp

application = get_wsgi_application()
application = WhiteNoise(application, root="/static/")
application.add_files("/media/cocktails", prefix="Cocktails/")
