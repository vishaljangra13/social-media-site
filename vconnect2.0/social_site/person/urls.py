from django.urls import path,re_path
from . import views

app_name='person'
urlpatterns=[
    path('new/',views.CreatePerson.as_view(),name='create'),
    #path('check/',views.CheckPage.as_view(),name='check'),
    path('all/',views.ListPerson.as_view(),name='all'),
    re_path(r'^useraccounts/$',views.UserPerson.as_view(),name='userperson'),
    re_path(r'^/(?P<slug>[-\w]+)/$',views.SinglePerson.as_view(),name='single'),
    re_path(r'^addfriend/(?P<slug>[-\w]+)/$',views.AddFriend.as_view(),name='addfriend'),
    re_path(r'^unfriend/(?P<slug>[-\w]+)/$',views.Unfriend.as_view(),name='unfriend'),
        re_path(r'^addfriend2/(?P<slug>[-\w]+)/$',views.AddFriend2.as_view(),name='addfriend2'),
        re_path(r'^unfriend2/(?P<slug>[-\w]+)/$',views.Unfriend2.as_view(),name='unfriend2'),

]
