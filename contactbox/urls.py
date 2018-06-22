from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from box.views import Index, NewPerson, ModifyPerson, DeletePerson, ShowPerson, People, AddAddress, AddPhone, AddEmail
from box.views import NewGroup, DeleteGroup, AddToGroup, DeleteFromGroup, Groups, GroupSearch

urlpatterns = [
    path('admin/', admin.site.urls),
    path('people', People.as_view(), name='people'),
    path('', Index.as_view(), name='index'),
    path('new/', NewPerson.as_view(), name='new-person'),
    re_path(r'^modify/(?P<id>\d+)/$', ModifyPerson.as_view(), name='modify-person'),
    re_path(r'^delete/(?P<id>\d+)/$', DeletePerson.as_view(), name='delete-person'),
    re_path(r'^show/(?P<id>\d+)/$', ShowPerson.as_view(), name='show-person'),
    re_path(r'^address/(?P<id>\d+)/$', AddAddress.as_view(), name='add-address'),
    re_path(r'^phone/(?P<id>\d+)/$', AddPhone.as_view(), name='add-phone'),
    re_path(r'^email/(?P<id>\d+)/$', AddEmail.as_view(), name='add-email'),
    path('new_group/', NewGroup.as_view(), name='new-group'),
    re_path(r'^delete_group/(?P<id>\d+)/$', DeleteGroup.as_view(), name='delete-group'),
    re_path(r'^add_to_group/(?P<id>\d+)/$', AddToGroup.as_view(), name='add-to-group'),
    re_path(r'^delete_from_group/(?P<id>\d+)/$', DeleteFromGroup.as_view(), name='delete-from-group'),
    path('groups/', Groups.as_view(), name='groups'),
    re_path(r'group-search/(?P<id>\d+)/$', GroupSearch.as_view(), name='group-search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

