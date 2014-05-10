from django.template import Context, loader
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def hello(request):
	t = loader.get_template('hello.html')
	c = Context({'current_time': datetime.now(),})
	return HttpResponse(t.render(c))