from django.urls import path, include
from django.http import HttpResponse
from . import views
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

def health_check(request):
    return HttpResponse("OK", status=200)

urlpatterns = [
    path('index', views.index, name='index'),
    path('base', views.base, name='base'),
    path('crud', views.index, name='crud'),       # The same as index
    path('api/', views.items_list, name='items_list'), 
    # path('', views.items_list),  # You can map the home page to this view too # Because i want to make the index to be Root(First page to appear)
    
    path('health/', health_check, name='health_check'),
    path('api/', include(router.urls)),  # API endpoints at /api/items/
    path('', views.index, name='index'),  # Root URL renders the HTML page
    path('base/', views.base, name='base'),
    path('crud/', views.index, name='crud'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    # path('api/items-list/', views.items_list, name='items_list'),  # Optional: keep items_list at a specific path
]

# --------------------------------------------------------------------# 

# from django.urls import path
# from django.http import HttpResponse
# from . import views

# def health_check(request):
#     return HttpResponse("OK", status=200)

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('index/', views.index, name='index-alt'),
#     path('base/', views.base, name='base'),
#     path('crud/', views.index, name='crud'),
#     path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
#     path('health/', health_check, name='health_check'),
#     path('api/items-list/', views.items_list, name='items_list'),
#     path('api/items-list/<int:id>/', views.item_detail, name='item_detail'),
# ]