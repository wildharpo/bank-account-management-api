import json
import os, sys

from flask import Blueprint
sys.path.append(os.path.join(sys.path[0], '../'))
sys.path.append(os.path.join(sys.path[0], '../data_access'))
from data_access.customer_repo import CustomerRepo

customer_bp = Blueprint('customer', __name__)

# http://localhost:5000/customer/ - this will be the GET method for fetching all customers
@customer_bp.route('/customer/', methods=['GET'])
def get_all_customers():
    customer_repo = CustomerRepo()
    customers = customer_repo.get_all_customers()
    customers_json = json.dumps(customers, default=str)
    return customers_json

@customer_bp.route('/customer/<int:id>', methods=['GET'])
def get_customer_by_id(id:int):
    customer_repo = CustomerRepo()
    customer = customer_repo.get_customer_by_id(id)
    customer_json = json.dumps(customer, default=str)
    return customer_json

# if __name__ == '__main__':
#     app.run()
