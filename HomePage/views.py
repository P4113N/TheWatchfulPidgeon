from django.template import Context, loader
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def index(request):
	t = loader.get_template('index.html')
	c = Context({'current_time': datetime.now(),})
	return HttpResponse(t.render(c))