class bank :

    def transaction(self):
        print("total transaction value ")

    def account_opening(self):
        print("this will show you your account open status")

    def deposit(self):
        print("this will show your deposited amount")

    def test(self):
        print("this is a test method from bank class")

class hdfc_bank:

    def hdfc_to_icici(self):
        print("this will show all the transactions between HDFC and ICICI bank. ")

    def test(self):
        print("this is test method from hdfc bank")

class sunil_bank:

    def account_status_icici(self):
        print("Account status of ICICI for Sunil.")

class icici(hdfc_bank, bank, sunil_bank): #multiple inheritance: inheriting two or more independent classes.
    pass

i = icici()
i.transaction()
i.deposit()
i.hdfc_to_icici()
i.account_opening()
i.test() #even though test method was present in both bank and hdfc_bank class, it is only calling test method from hdfc_bank class only
        #hence, if there is conflict (method/variable is same), then by default it will call the very first class arguemnt called during inheritance
i.account_status_icici()