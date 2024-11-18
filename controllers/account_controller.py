import json
import os, sys

from flask import Blueprint
sys.path.append(os.path.join(sys.path[0], '../'))
sys.path.append(os.path.join(sys.path[0], '../data_access'))
from data_access.account_repo import AccountRepo

account_bp = Blueprint('account', __name__)

# http://localhost:5000/customer/ - this will be the GET method for fetching all customers
@account_bp.route('/account/', methods=['GET'])
def get_all_accounts():
    account_repo = AccountRepo()
    accounts = account_repo.get_all_accounts()
    accounts_json = json.dumps(accounts, default=str)
    return accounts_json

@account_bp.route('/account/<int:id>', methods=['GET'])
def get_account_by_id(id:int):
    account_repo = AccountRepo()
    account = account_repo.get_account_by_id(id)
    account_json = json.dumps(account, default=str)
    return account_json

# if __name__ == '__main__':
#     app.run()
