from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from todo.models import List, Item

# Display all lists
def index(request):
    lists = List.objects.all()
    output = ', '.join([l.name for l in lists ])
    return render_to_response('todo/tmpl/index.html', {'lists': lists})

# Display all todo items in list
def detail(request, id):
    list = get_object_or_404(List, pk=id)
    return render_to_response(
        'todo/tmpl/details.html', 
        {'list': list}, 
        context_instance=RequestContext(request)
    )

# Add a new item to list
def add(request, id):
    list = get_object_or_404(List, pk=id)
    item = Item(description=request.POST['item'])
    item.list = list
    item.save()
    # Redirect to the list
    return HttpResponseRedirect(reverse('todo.views.detail', args=(list.id,)))