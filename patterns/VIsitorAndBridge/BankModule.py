import string
import TicketModule
import TicketObservableBase
import random
import datetime

#интерфейс банковского клиента - он должен быть готов сохранить вернувшуюся транзакцию, должен уметь покупать билет и получить бонусы за покупку
class IBankClient():
    def addBonus(self, bonus : int):
        pass
    
    def saveOperation(self, operationText : string):
        pass
    
    def buyTicket(self, ticket : TicketModule.Ticket):
        pass

#все банки должны уметь проводить операции
class IBank():
	def makeOperation(self, countOfMoney : int) -> dict: 
		pass

#все продавцы должны продавать билеты
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

#реализация клиента содержит части сразу двух паттернов - посетитель, т.к. он посещает банки для оплаты (через посредника)
#и мост - т.к. использует для покупки билета передаваемого ему абстрактного продавца, не заботясь о реализации метода
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

#класс через который клиент посещает для оплаты различные банки и накапливает бонусы и историю операций    
class AviaTicketSeller(ITicketSeller):
    def __init__(self, ticketBase : TicketObservableBase.ObservableTicketBase):
        self.__bankList : list = [Sberbank(), Tinkoff(), VTB()]
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
    
#наследуются от продажника - в данных двух классах реализация паттерна мост
#оба они взаимозаменяймы по поведению, но реализация каждого отличается
#каждый из них в зависимости от внешних обстоятельств передается клиенту для соверщения операций
class InCountryTicketSeller(AviaTicketSeller):
    def __init__(self, ticketBase : TicketObservableBase.ObservableTicketBase):
        super().__init__(ticketBase)
        
    def buyTicket(self, client : IBankClient, ticket : TicketModule.Ticket):
        print('Вы купили билет на внутренний перелет! 30% стоимости субсидировано государством!')
        
        oldPrice = ticket.get_ticketPrice()
        decrease = ticket.get_ticketPrice() * 0.3
        ticket.subsidizeTheTicket(decrease)
        
        print('Цена уменьшена:', ticket.get_ticketPrice(), '<-', oldPrice )
        super().buyTicket(client, ticket)

class OutCountryTicketSeller(AviaTicketSeller):
    def __init__(self, ticketBase : TicketObservableBase.ObservableTicketBase):
        super().__init__(ticketBase)
        
    def buyTicket(self, client : IBankClient, ticket : TicketModule.Ticket):
        print('Вы купили билет на перелет задействующий другую страну! В связи с внешнеполитической обстановкой цена билета увеличена на 0.3!')
        
        oldPrice = ticket.get_ticketPrice()
        decrease = (ticket.get_ticketPrice() * 0.3) * -1
        ticket.subsidizeTheTicket(decrease)
        
        print('Цена увеличена:',oldPrice, '->', ticket.get_ticketPrice() )
        super().buyTicket(client, ticket)