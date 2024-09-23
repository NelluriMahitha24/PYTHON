class Account:
    min_ba=500
    def open_account(self):
        print("account opened succuessfully")
    @classmethod
    def m2(cls):
        pass
    @staticmethod
    def m3():
        pass
a1=Account()
a2=Account()
#what class contains: variables and Methods

print(a1.__dict__)
print(a2.__dict__)
print(Account.__dict__)

# {}
# {}
# {'__module__': '__main__', 'min_ba': 500, 'open_account': <function Account.open_account at 0x0000018C42A8D1C0>, 'm2': <classmethod(<function Account.m2 at 0x0000018C42A8DEE0>)>, 'm3': <staticmethod(<function Account.m3 at 0x0000018C42A8EDE0>)>, '__dict__': <attribute '__dict__' of 'Account' objects>, '__weakref__': <attribute '__weakref__' of 'Account' objects>, '__doc__': None}