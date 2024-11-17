from datetime import date

class Account:
    def __init__(self, account_id:int, account_number:str, account_type_id:int, date_opened:date):
        self.account_id = account_id
        self.account_number = account_number
        self.account_type = account_type_id
        self.date_opened = date_opened