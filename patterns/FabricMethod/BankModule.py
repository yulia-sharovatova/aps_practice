import string
import TicketModule
import TicketObservableBase
import random
import datetime

class IBankClient():
    def addBonus(self, bonus : int):
        pass
    
    def saveOperation(self, operationText : string):
        pass
    
    def buyTicket(self, ticket : TicketModule.Ticket):
        pass

class IBank():
	def makeOperation(self, countOfMoney : int) -> dict: 
		pass

class ITicketSeller():
    def buyTicket(self, client : IBankClient, ticket : TicketModule.Ticket):
        pass


#------------- реализации ---------------
class Sberbank(IBank):
    def __init__(self):
        self.__bonusPerRubl = 1
        self.__bankName = "Сбербанк"
    
    def getName(self) -> dict: 
        return self.__bankName
    
    def makeOperation(self, countOfMoney : int) -> dict:
        bonuses = countOfMoney * self.__bonusPerRubl
        print('Спасибо за то что воспользовались банком', self.__bankName, 'за операцию на сумму', countOfMoney, 'вам будет начисленно', bonuses, 'бонусов') 
        return { "transactionNumber" : random.randint(0, 10000000000000), "bonuses" : bonuses }

class Tinkoff(IBank):
    def __init__(self):
        self.__bonusPerRubl = 3
        self.__bankName = "Тинькофф"
    
    def getName(self) -> dict: 
        return self.__bankName
    
    def makeOperation(self, countOfMoney : int) -> dict:
        bonuses = countOfMoney * self.__bonusPerRubl
        print('Спасибо за то что воспользовались банком', self.__bankName, 'за операцию на сумму', countOfMoney, 'вам будет начисленно', bonuses, 'бонусов') 
        return { "transactionNumber" : random.randint(0, 10000000000000), "bonuses" : bonuses }

class VTB(IBank):
    def __init__(self):
        self.__bonusPerRubl = 2
        self.__bankName = "ВТБ"
    
    def getName(self) -> dict: 
        return self.__bankName
    
    def makeOperation(self, countOfMoney : int) -> dict:
        bonuses = countOfMoney * self.__bonusPerRubl
        print('Спасибо за то что воспользовались банком', self.__bankName, 'за операцию на сумму', countOfMoney, 'вам будет начисленно', bonuses, 'бонусов') 
        return { "transactionNumber" : random.randint(0, 10000000000000), "bonuses" : bonuses }

class BankOfAmericaCorporation (IBank):
    def __init__(self):
        self.__bonusPerRubl = 0
        self.__bankName = "ReallyFatBank"
    
    def getName(self) -> dict: 
        return self.__bankName
    
    def makeOperation(self, countOfMoney : int) -> dict:
        bonuses = countOfMoney * self.__bonusPerRubl
        print('Thank you for using our bank', self.__bankName, ' you spend ', countOfMoney, ' you recieve', bonuses, 'bonuses') 
        return { "transactionNumber" : random.randint(0, 10000000000000), "bonuses" : bonuses }

class BankOfFranch (IBank):
    def __init__(self):
        self.__bonusPerRubl = 1
        self.__bankName = "BanqueSePainFrançais"
    
    def getName(self) -> dict: 
        return self.__bankName
    
    def makeOperation(self, countOfMoney : int) -> dict:
        bonuses = countOfMoney * self.__bonusPerRubl
        print("Merci d'utiliser notre banque", self.__bankName, ' tu as depensé ', countOfMoney, ' tu auras ', bonuses, 'bonus') 
        return { "transactionNumber" : random.randint(0, 10000000000000), "bonuses" : bonuses }

class BankOfGermany (IBank):
    def __init__(self):
        self.__bonusPerRubl = 1
        self.__bankName = "SehrWütendeBankMitSchnurrbart"
    
    def getName(self) -> dict: 
        return self.__bankName
    
    def makeOperation(self, countOfMoney : int) -> dict:
        bonuses = countOfMoney * self.__bonusPerRubl
        print("Danke für die Nutzung", self.__bankName, ' du hast ausgegeben ', countOfMoney, ' du wirst kriegen ', bonuses, 'boni') 
        return { "transactionNumber" : random.randint(0, 10000000000000), "bonuses" : bonuses }


class Client(IBankClient):
    def __init__(self):
        self.__bonuses = 0
        self.__operationHistory : list = []
        self.__seller : ITicketSeller = None
    
    def setTicketSeller(self, seller : ITicketSeller):
        self.__seller = seller
    
    def addBonus(self, bonus : int):
        self.__bonuses += bonus
    
    def saveOperation(self, operationText : string):
        self.__operationHistory.append(operationText)
    
    def buyTicket(self, ticket : TicketModule.Ticket):
        self.__seller.buyTicket(self,ticket)
    
    def getBonus(self) -> int:
        return self.__bonuses
    
    def getOperationHistory(self) -> int:
        return self.__operationHistory
    
class AviaTicketSeller(ITicketSeller):
    def __init__(self, ticketBase : TicketObservableBase.ObservableTicketBase):
        self.__bankList : list = [Sberbank()]
        self.__ticketBase : TicketObservableBase.ObservableTicketBase = ticketBase
        
    def buyTicket(self, client : IBankClient, ticket : TicketModule.Ticket):
        
        print('Банки доступные для оплаты билета:')
        
        choosenBank = 0
        while True:
            for bankNumber,bank in enumerate(self.__bankList,start=1):
                print('[',bankNumber,']',bank.getName())
                
            textChoosenBank=input('Введите номер банка:')
            choosenBank=int(textChoosenBank)-1
            
            if choosenBank >= 0 and choosenBank < len(self.__bankList):
                break
            else:
                print('Введите банк из выведенного списка. Попробуйте еще раз.')

        transactionInfo = self.__makeBankTransaction(self.__bankList[choosenBank],ticket)
        returnBonus =  transactionInfo['bonuses']
        transactionNumber =  transactionInfo['transactionNumber']
            
        infoString = str(datetime.datetime.now()) + '| Был куплен билет ' + str(ticket.get_DepartureCity()) + '-->' + str(ticket.get_ArrivalCity()) + ' на сумму ' + str(ticket.get_ticketPrice()) + '(' + str(self.__bankList[choosenBank].getName()) + ' | ' + str(transactionNumber) + ')'
        
        client.addBonus(returnBonus)
        client.saveOperation(infoString)
        
        print('Билет', ticket.get_ticketNumber(), ' был куплен!')
        self.__ticketBase.deleteTicket(ticket)    
    
    def __makeBankTransaction(self, bank : IBank, ticket : TicketModule.Ticket) -> dict:
        return bank.makeOperation(ticket.get_ticketPrice())    