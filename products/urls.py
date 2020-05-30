from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^api/v1/products/$',
        views.get_post_products,
        name='get_post_products'
    ),
    url(
        r'^api/v1/products/(?P<pk>[0-9]+)$',
        views.get_delete_update_product,
        name='get_delete_update_product'
    ),
    url(
        r'^api/v1/categories/$',
        views.get_categories,
        name='get_categories'
    ),
    url(
        r'^api/v1/categories/(?P<category_id>[0-9]+)$',
        views.get_products_categories,
        name='get_categories_id'
    )

]
