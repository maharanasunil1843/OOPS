class bank : #parent class #level1

    def transaction(self):
        print("total transaction value ")

    def account_opening(self):
        print("this will show you your account open status")

    def deposit(self):
        print("this will show your deposited amount")

class hdfc_bank(bank): #child class of bank #level2

    def hdfc_to_icici(self):
        print("this will show all the transactions between HDFC and ICICI bank. ")

class icici(hdfc_bank): #child class of hdfc_bank #level3
    pass
#this is called multi-level inheritance.
#decreased number of line of codes
i = icici()
i.hdfc_to_icici()
i.deposit()
i.account_opening()
i.transaction()
