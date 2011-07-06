from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.core import serializers
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from todo.models import List, Item
from django.contrib.auth.decorators import login_required
import json

# Display all lists
@csrf_protect
@login_required
def index(request):
    lists = List.objects.filter(user__id=request.user.id)
    c = {'lists': lists}
    return render_to_response('todo/tmpl/index.html', c, context_instance=RequestContext(request))

# Display all todo items in list
@login_required
def detail(request, id):
    list = get_object_or_404(List, pk=id)
    if list.user != request.user:
        return HttpResponseForbidden("Not authorized!")
    items = list.item_set.order_by('order', 'created_on')
    return render_to_response(
        'todo/tmpl/details.html', 
        {'list': list, 'items': items}, 
        context_instance=RequestContext(request)
    )

# Create a new list
@csrf_protect
@login_required
def create(request):
    if request.method == 'POST':
        list = List()
        list.user = request.user
        list.name = request.POST['name']
        list.save()
        # Redirect to the list
        return HttpResponseRedirect(reverse('todo.views.detail', args=(list.id,)))

# Add a new item to list
@login_required
def add(request, id):
    list = get_object_or_404(List, pk=id)
    if list.user != request.user:
            return HttpResponseForbidden("Not authorized!")
    item = Item(description=request.POST['item'])
    item.list = list
    item.save()
    # Redirect to the list
    return HttpResponseRedirect(reverse('todo.views.detail', args=(list.id,)))

# Move an item in list
@login_required
def move(request, id):
    list = get_object_or_404(List, pk=id)
    if list.user != request.user:
        return HttpResponseForbidden("Not authorized!")
    item = get_object_or_404(Item, pk=request.POST['item_id'])
    item.move(request.POST['position'])
    # Send JSON response
    return HttpResponse(json.dumps({'result': 'success'}, ensure_ascii=False), 'application/javascript')