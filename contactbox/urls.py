from django.contrib import admin
from django.urls import path, re_path
# from django.conf import settings
# from django.conf.urls.static import static
from box.views import Index, NewPerson, ModifyPerson, DeletePerson, ShowPerson, People

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', People.as_view(), name='people'),
    path('index/', Index.as_view(), name='index'),
    path('new/', NewPerson.as_view(), name='new-person'),
    re_path(r'^modify/(?P<id>\d+)/$', ModifyPerson.as_view(), name='modify-person'),
    re_path(r'^delete/(?P<id>\d+)/$', DeletePerson.as_view(), name='delete-person'),
    re_path(r'^show/(?P<id>\d+)/$', ShowPerson.as_view(), name='show-person')
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)