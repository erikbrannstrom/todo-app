from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core import serializers
from django.template import RequestContext
from todo.models import List, Item
from django.contrib.auth.decorators import login_required
import json

# Display all lists
@login_required
def index(request):
    lists = List.objects.all()
    output = ', '.join([l.name for l in lists ])
    return render_to_response('todo/tmpl/index.html', {'lists': lists})

# Display all todo items in list
@login_required
def detail(request, id):
    list = get_object_or_404(List, pk=id)
    items = list.item_set.order_by('order', 'created_on')
    return render_to_response(
        'todo/tmpl/details.html', 
        {'list': list, 'items': items}, 
        context_instance=RequestContext(request)
    )

# Add a new item to list
@login_required
def add(request, id):
    list = get_object_or_404(List, pk=id)
    item = Item(description=request.POST['item'])
    item.list = list
    item.save()
    # Redirect to the list
    return HttpResponseRedirect(reverse('todo.views.detail', args=(list.id,)))

# Move an item in list
@login_required
def move(request, id):
    list = get_object_or_404(List, pk=id)
    item = get_object_or_404(Item, pk=request.POST['item_id'])
    item.move(request.POST['position'])
    # Send JSON response
    return HttpResponse(json.dumps({'result': 'success'}, ensure_ascii=False), 'application/javascript')