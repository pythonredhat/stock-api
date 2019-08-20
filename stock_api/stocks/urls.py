from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^api/v1/stocks/(?P<pk>[0-9+)$',
        views.get_delete_update_stock,
        name='get_delete_update_stock'
    ),
    url(
        r'^api/v1/stocks/$',
        views.get_post_stocks,
        name='get_post_stocks'
    )
]