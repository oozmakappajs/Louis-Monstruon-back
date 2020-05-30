from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^api/v1/products/(?P<pk>[0-9]+)$',
        views.get_delete_update_product,
        name='get_delete_update_product'
    ),
    url(
        r'^api/v1/products/$',
        views.get_post_products,
        name='get_post_products'
    ),
    url(
        r'^api/v1/products/filter',
        views.get_filter,
        name='get_filter'
    ),
    url(
        r'^api/v1/products/categories',
        views.get_post_categories,
        name='get_post_categories'
    ),
    url(
        r'^api/v1/products/cart',
        views.get_post_cart,
        name='get_post_cart'
    ),
]