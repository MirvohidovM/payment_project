from django.urls import path

from .views import *


urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list' ),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    # path('create-checkout-session/', create_checkout_session, name='create-checkout-session'),
    path('create-checkout-session/<int:pk>', CreateStripeCheckoutSessionView.as_view(), name='create-checkout-session'),

    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
]