from django.shortcuts import render , redirect
from django.conf import settings
import stripe
from django.urls import reverse
from django.http import JsonResponse
from .models import Payment

# Create your views here.
stripe.api_key = settings.STRPIE_PRIVATE_KEY
def index(request):
	if request.method == "POST":
		checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1Lwq39Ekal4BbptgHwmiphnD',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('success')),
            cancel_url=request.build_absolute_uri(reverse('cancel')),
        )
		Payment.objects.create(user=checkout_session.id)

		return redirect(checkout_session.url)
	return render(request , 'index.html' , {})

def cancel(request):
	return render(request , 'cancel.html' , )

def success(request):
	return render(request , 'success.html' , )

# def json_test(request):
# 	from . import test_json as J
# 	context = {'id' : J.id}
# 	return render(request , 'json.html' , context)