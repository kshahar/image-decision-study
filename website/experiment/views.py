from time import time
from django.conf import settings
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.utils import simplejson
from models import Image, Result, Session

# IMAGES_PATH must be defined in settings.py
IMAGES_PATH = getattr(settings, 'IMAGES_PATH', '')

def index(request):
    try:
        all_images = Image.objects \
            .order_by('environment_id', 'id')
        print request.session.session_key

        # Transform to client format
        images = map( _format_image, all_images)

        data = { 'images' : images }
        js_data = simplejson.dumps(data)
        return render(request, 'experiment/templates/session.html',
            { 'data' : js_data, 'images' : images})

    except Exception as e:
        print e
        raise Http404

def save(request):
    results = simplejson.loads(request.POST['results'])

    session_key = request.session.session_key    #request.COOKIES[settings.SESSION_COOKIE_NAME]
    session = Session(key=session_key, global_time=time())
    session.save()

    # Convert user results to Result table row
    db_results = []
    for result in results:
        db_result = Result(
            session = session,
            time = result['time'],
            selection = result['selection'],
        )
        db_result.image_id = result['id']
        db_results.append(db_result)

    try:
        # This could be done better with a transaction
        for db_result in db_results:
            db_result.save()
    except Exception as e:
        print e
        pass

    return HttpResponseRedirect('/static/thankyou.html')

# Convert an Image table row to client format
def _format_image(db_image):
    url = IMAGES_PATH + '/' + db_image.filename
    entry = { 'id' : db_image.id, 'url' : url }
    return entry
