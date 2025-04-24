from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

def base(request) :
    return render(request, 'base.html')

def index(request):
    return render(request, 'crud/index.html')


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

def item_list_view(request):
    items = Item.objects.all().order_by('id')
    return render(request, 'item_list.html', {'items': items})

def delete_item(request, item_id):
    # Delete the item
    item_to_delete = get_object_or_404(Item, id=item_id)
    item_to_delete.delete()

    # Renumber the remaining items
    all_items = Item.objects.all().order_by('id')
    for i, item in enumerate(all_items):
        item.id = i + 1
        item.save()

    return redirect('todo_list')  # Adjust the redirect as needed for your app

@api_view(['GET', 'POST'])
@csrf_exempt  # This line disables CSRF protection (if needed for the API view)
def items_list(request):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = request.data
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ToDoItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Ensure proper permissions

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

# ------------------------------------------------------------------

# # from django.shortcuts import render, get_object_or_404, redirect # Imports rendering and redirect utilities
# from django.http import JsonResponse # Imports JsonResponse for API responses
# from django.views.decorators.csrf import csrf_exempt # Imports CSRF exemption decorator for API views
# from .models import Item # Imports the Item model (affects database operations)
# import json # Imports JSON for parsing request bodies

# def base(request): # Defines the base view
#     return render(request, 'base.html') # Renders base.html template (affects base.html, accessed via /base/)

# def index(request): # Defines the index view
#     return render(request, 'crud/index.html') # Renders index.html template (affects index.html, accessed via /, /index/, /crud/)

# def delete_item(request, item_id): # Defines the delete view for HTML requests
#     item_to_delete = get_object_or_404(Item, id=item_id) # Gets the item or returns 404 (affects database)
#     item_to_delete.delete() # Deletes the item (affects database)
#     return redirect('index') # Redirects to the index page (affects urls.py, reloads index.html)

# @csrf_exempt # Exempts this view from CSRF protection (needed for POST requests from JavaScript)
# def items_list(request): # Defines the API view for listing/creating items
#     if request.method == 'GET': # Handles GET requests to list items
#         items = Item.objects.all() # Queries all items from the database (affects database)
#         data = [{'id': item.id, 'name': item.name, 'description': item.description, 
#                  'status': item.status, 'priority': item.priority, 'due_date': str(item.due_date), 
#                  'created_at': str(item.created_at)} for item in items] # Converts items to JSON-compatible format
#         return JsonResponse(data, safe=False) # Returns the items as JSON (affects main.js fetchItems)

#     elif request.method == 'POST': # Handles POST requests to create items
#         data = json.loads(request.body) # Parses the JSON request body (from main.js)
#         item = Item.objects.create( # Creates a new item in the database (affects database)
#             name=data['name'], # Sets the name
#             description=data['description'], # Sets the description
#             status=data['status'], # Sets the status
#             priority=data['priority'], # Sets the priority
#             due_date=data['due_date'] # Sets the due date
#         )
#         return JsonResponse({'id': item.id}, status=201) # Returns the new item’s ID with status 201 (affects main.js)

#     return JsonResponse({'error': 'Method not allowed'}, status=405) # Returns an error for unsupported methods (affects main.js)

# @csrf_exempt # Exempts this view from CSRF protection (needed for PUT/DELETE requests from JavaScript)
# def item_detail(request, id): # Defines the API view for individual item operations
#     try: # Tries to get the item
#         item = Item.objects.get(id=id) # Gets the item by ID (affects database)
#     except Item.DoesNotExist: # If the item doesn’t exist
#         return JsonResponse({'error': 'Item not found'}, status=404) # Returns a 404 error (affects main.js)

#     if request.method == 'GET': # Handles GET requests to retrieve item details
#         data = { # Constructs the item data as JSON
#             'id': item.id, # Includes the ID
#             'name': item.name, # Includes the name
#             'description': item.description, # Includes the description
#             'status': item.status, # Includes the status
#             'priority': item.priority, # Includes the priority
#             'due_date': str(item.due_date), # Includes the due date
#             'created_at': str(item.created_at) # Includes the creation date
#         }
#         return JsonResponse(data) # Returns the item as JSON (affects main.js handleEdit)

#     elif request.method == 'PUT': # Handles PUT requests to update an item
#         data = json.loads(request.body) # Parses the JSON request body (from main.js)
#         item.name = data['name'] # Updates the name (affects database)
#         item.description = data['description'] # Updates the description (affects database)
#         item.status = data['status'] # Updates the status (affects database)
#         item.priority = data['priority'] # Updates the priority (affects database)
#         item.due_date = data['due_date'] # Updates the due date (affects database)
#         item.save() # Saves the updated item (affects database)
#         return JsonResponse({'id': item.id}) # Returns the item’s ID (affects main.js)

#     elif request.method == 'DELETE': # Handles DELETE requests to remove an item
#         item.delete() # Deletes the item (affects database)
#         return JsonResponse({}, status=204) # Returns a 204 status (affects main.js)

#     return JsonResponse({'error': 'Method not allowed'}, status=405) # Returns an error for unsupported methods (affects main.js)