# 1) create account class with 2 attributes - balance and account no.
# 2) create methods for debit, credit and printing the balance.



class Account:
 balance = 0
 account_no = 0

 def __init__(self,balance,account_no):
  self.balance = balance
  self.account_no = account_no

 def debit(self,amount):
  self.balance -= amount

 def credit(self,amount):
  self.balance += amount

 def print_balance(self):
  return self.balance 

acc1 = Account(10000,1234)
print("balance =",acc1.print_balance())
acc1.debit(500)
print("balance =",acc1.print_balance())
acc1.credit(1000)
print("balance =",acc1.print_balance())  
   






















