import stripe
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, TemplateView
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from .models import *


class ProductListView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "products/products.html"


class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "products/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        # context["product"] = Product.objects.get(id=self.kwargs('pk'))
        # context["prices"] = Price.objects.filter(product=self.get_object())
        return context


stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateStripeCheckoutSessionView(View):
    """
    Create a checkout session and redirect the user to Stripe's checkout page
    """

    def post(self, request, *args, **kwargs):

        product = Product.objects.get(id=self.kwargs['pk'])

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": int(product.price) * 100,
                        "product_data": {
                            "name": product.name,
                            "description": product.desc,
                            # 'amount': int(product.price),
                            "images": [
                                f"{settings.BACKEND_DOMAIN}/{product.thumbnail}"
                            ],
                        },
                    },
                    "quantity":  1,
                }
            ],
            metadata={"product_id": product.id},
            mode="payment",
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
        )
        img = f"{settings.BACKEND_DOMAIN}/{product.thumbnail.url}"
        print(f'img >>> {img}')
        print(f'thumbnail URL >>> {product.thumbnail.url}')
        return redirect(checkout_session.url)


#
# @csrf_exempt
# def create_checkout_session(request):
#     print(f'CreateChekoutSession')
#
#     if request.method == 'POST': #'GET':
#         domain_url = 'http://localhost:8000/'
#         stripe.api_key = settings.STRIPE_SECRET_KEY
#         print('IF')
#         try:
#             # Create new Checkout Session for the order
#             # Other optional params include:
#             # [billing_address_collection] - to display billing address details on the page
#             # [customer] - if you have an existing Stripe Customer ID
#             # [payment_intent_data] - capture the payment later
#             # [customer_email] - prefill the email input in the form
#             # For full details see https://stripe.com/docs/api/checkout/sessions/create
#
#             # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
#             checkout_session = stripe.checkout.Session.create(
#                 success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
#                 cancel_url=domain_url + 'cancel/',
#                 payment_method_types=['card'],
#                 mode='payment',
#                 line_items=[
#                     {
#                         'name': 'T-shirt',
#                         'quantity': 1,
#                         'currency': 'usd',
#                         'amount': '2000',
#                     }
#                 ]
#             )
#             print(f'TRY :  ChekoutSession  >>> {checkout_session}')
#
#             return JsonResponse({'sessionId': checkout_session['id']})
#         except Exception as e:
#             print(f'EXCEPT')
#             return JsonResponse({'error': str(e)})


class SuccessView(TemplateView):
    template_name = 'products/success.html'


class CancelView(TemplateView):
    template_name = 'products/cancel.html'