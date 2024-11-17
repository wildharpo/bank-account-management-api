from data_access.repo_base import RepoBase

class CustomerRepo(RepoBase):
    def get_all_customers(self):
        customers = self.select_data('SELECT * FROM customer')
        return customers
    
    def get_customer_by_id(self, customer_id:int):
        arguments = (customer_id,)
        customers = self.select_data_by_id('SELECT * FROM customer WHERE customer_id = %s', arguments)
        return customers