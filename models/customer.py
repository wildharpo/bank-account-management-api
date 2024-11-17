from datetime import date

class Customer:
    def __init__(self, customer_id:int, first_name:str, middle_name:str, last_name:str, street_address:str, city:str, state_abbrev:str, zip_code:str, email:str, phone:str, date_of_birth:date, ssn:str):
        self.customer_id = customer_id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.street_address = street_address
        self.city = city
        self.state_abbrev = state_abbrev
        self.zip_code = zip_code
        self.email = email
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.ssn = ssn