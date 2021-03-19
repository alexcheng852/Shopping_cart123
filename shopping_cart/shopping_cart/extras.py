from django.conf import settings
import random
import string
from datetime import date
import datetime
import braintree
from shopping_cart.models import OrderItem

def generate_order_id():
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return date_str + rand_str

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="55mrzc3ph5vfvgkd",
        public_key="286xsgxxrb6rdsk9",
        private_key="4d0976b370cce3ef8abef87a5806ccfb"
    )
)

def generate_client_token():
    print(gateway)
    return gateway.client_token.generate()

def transact(options):
    return gateway.transaction.sale(options)

def find_transaction(id):
    return gateway.transaction.find(id)
