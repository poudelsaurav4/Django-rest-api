from django.urls import path, include
from snippets.views import *
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter


# snippet_list = SnippetViewSet.as_view({
#     'get':'list',
#     'post':'create'
# })

# snippet_details = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'pathch': 'partial_update',
#     'delete': 'destroy'
# })

# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes = [renderers.StaticHTMLRenderer])


# user_list = UserViewSet.as_view({
#     'get': 'list'
# })

# user_details = UserViewSet.as_view({
#     'get': 'retrieve'
# })


router = DefaultRouter()
router.register(r'snippets', SnippetViewSet, basename='snippet')
router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
    # path('snippets/', snippet_list, name ='snippets-list'),
    # path('snippets/<int:pk>/', snippet_details, name ='snippet-detail'),
    # path('users/', user_list,name ='user-list'),
    # path('users/<int:pk>/', user_details, name ='user-detail'),
    
    # path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight')

]

# urlpatterns = format_suffix_patterns(urlpatterns)
