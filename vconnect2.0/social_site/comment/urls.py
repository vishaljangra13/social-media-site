from django.urls import path,re_path
from . import views

app_name='comment'
urlpatterns=[
    re_path(r'^post/(?P<pk>\d+)/addcomment/$',views.add_comment_to_post,name='add_comment_to_post'),
    re_path(r'^posts/comment/(?P<pk>\d+)/$',views.SinglePost.as_view(),name='single'),
    #re_path(r'^posts/commentandform/(?P<pk>\d+)/$',views.TwoPage.as_view(),name='twopage'),
]
