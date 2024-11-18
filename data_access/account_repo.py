from data_access.repo_base import RepoBase

class AccountRepo(RepoBase):
    def get_all_accounts(self):
        accounts = self.select_data('SELECT * FROM account')
        return accounts
    
    def get_account_by_id(self, account_id:int):
        arguments = (account_id,)
        accounts = self.select_data_by_id('SELECT * FROM account WHERE account_id = %s', arguments)
        return accounts