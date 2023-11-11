import random
class Application:
    
    def showMainMenu():
        
        while True:
            
            selected = int(input(f"What Would You Like To Do?\nSelect Account: 1\nOpen Account: 2\nExit: 3\n"))
            
            if selected == 1:
                accNum = str(input("Enter Account Number: "))
                accFound = bank.searchAccount(accNum)
                if accFound == False:
                    print(f"No account found related to {accNum}")       
                else:
                    print("Account Found\nPlease Wait")
                    Application.showAccountMenu(bank,accFound)
            
            elif selected == 2:
                # call account class
                bank.openAccount()
            elif selected == 3:
                # leave main menu
                break
                
            elif selected != 1 or selected != 2 or selected != 3:
                print("Invaild Option Try Again")    
                
    def showAccountMenu(Bank, accIdx):
        
        while True:
            

            selected = int(input(f"What Would You Like To Do?\nCheck Balance: 1\nDeposit: 2\nWithdraw: 3\nExit: 4\n"))
            
            if selected == 1:
                # check account balance

                print("Checking Balance...")
                balanceIdx = Bank.allAccounts[accIdx - 1].rfind(",")
                print(f"${Bank.allAccounts[accIdx - 1][balanceIdx + 1:]}")

            
            elif selected == 2:
                # deposit money
                depositNum = input("Enter The Amount Of Money That You Would Like To Deposit:")
                Account.deposit(depositNum)
            
            elif selected == 3:
            # withdraw money
                withdrawNum = input("Enter How Much Money You Would Like To Take Out:")
            elif selected == 4:
                # leave main menu
                break
                
            elif selected != 1 or selected != 2 or selected != 3 or selected != 4:
                print("Invaild Option Try Again")
            
    def run():
        Application.showMainMenu()
        

class Bank:
    
    def __init__(self, name):
        self._bankName = name
        self.allAccounts = []
        
    def accounts(self):
        acc1 = Account(1000, "Aljen", 0.1, 75000)
        acc2 = Account(1010, "Raj", 0.1, 65000)
        acc3 = Account(1100, "Connor", 0.1, 70000)
        self.allAccounts.append(acc1.toStr())
        self.allAccounts.append(acc2.toStr())
        self.allAccounts.append(acc3.toStr())
        
    def openAccount(self):
        # open a new account
        accId = random.randint(1111,99999)
        name = input("Please Provide A Name For The Account")
        balance = int(input("How Much Do You want To Depsoit Into The Account?  \nPlease Enter A Numeric Value No characters or symbols"))
        newAcc = Account(accId, name, 0.1, balance)
        print(newAcc.toStr())
        self.allAccounts.append(newAcc.toStr())
        
    def searchAccount(self, accNum):
        # search for an account in the bank
        idx = 0
        for a in self.allAccounts:
            acc = a
            commaIdx = acc.find(",")
            if accNum == acc[:commaIdx]:
                return idx + 1
            else:
                idx += 1
                
      
        return False
        
        
        
        
class Account:
    
    def __init__(self,accNum,holderName, intrest, balance):
        
        self._accountNumber = accNum
        self._accountHolderName = holderName
        self._intrestRate = intrest
        self._accountBalance = balance
        
    def getAccountNum(self):
        return self._accountNumber
    
    def getAccountHolderName(self):
        return self._accountHolderName
    
    def setAccountHolderName(self,newName):
        self._accountHolderName = newName
    
    def getIntrestRate(self):
        return self._intrestRate
    
    def setInterstRate(self,newIntrest):
        self._intrestRate = newIntrest
        
    def deposit(self, depositNum):
        return self.accountBalance + depositNum
    
    def withdraw(self,withdrawNum):
        return self.accountBalance - withdrawNum
    
    def getCurrentBalance(self):
        return self.accountBalance
    
    def toStr(self):
        return f"{self._accountNumber},{self._accountHolderName},{self._intrestRate},{self._accountBalance}"
    
class savingAccount:
    
    def __init__(self,minBalance):
        self._minimumBalance = minBalance
        
    def withdraw(self, withdrawNum):
        if Account.getCurrentBalance() - withdrawNum < self._minimumBalance:
            print("Sorry! You cannot withdraw that amount")
            
        else:
            Account.withdraw(withdrawNum)
            print("transication complete")
    
class chequingAccount:
    
    def __init__(self,overDraft):
        self._overDraftLimit = overDraft 
        
    def withdraw(self, withdrawNum):
        if (Account.getCurrentBalance() + self._overDraftLimit) - withdrawNum < 0:
            print("Sorry! You do not have enough money in your account to cover this transaction.")
        
        else:
            Account.withdraw(withdrawNum)
            print("Transaction Complete")
            

bank = Bank("RAJ'S BANK")
bank.accounts()
Application.run()