import string
import random
import BankModule
import TicketModule
import TicketObservableBase


#интерфейс, который должны реализовывать все продавцы
class ICountryTicketSeller:
	def sellTicket(self, client : BankModule.IBankClient, ticket : TicketModule.Ticket):
		pass

#реализация продавцов - у каждого свой метод
class MainRussianTicketSeller(ICountryTicketSeller, BankModule.AviaTicketSeller):
    def __init__(self, ticketBase : TicketObservableBase.ObservableTicketBase):
        super().__init__(ticketBase)
        self._AviaTicketSeller__bankList : list = [ BankModule.Sberbank(), BankModule.VTB(), BankModule.Tinkoff() ]

    def sellTicket(self, client : BankModule.IBankClient, ticket : TicketModule.Ticket):
        self.buyTicket(client,ticket)


class MainAmericanTicketSeller(ICountryTicketSeller, BankModule.AviaTicketSeller):
    def __init__(self, ticketBase : TicketObservableBase.ObservableTicketBase):
        super().__init__(ticketBase)
        self._AviaTicketSeller__bankList : list = [ BankModule.BankOfAmericaCorporation() ]
        
    def sellTicket(self, client : BankModule.IBankClient, ticket : TicketModule.Ticket):
        if random.randint(1,5) == 1:
            print('Вам повезло! Американский продавец билетов согласился работать!')
            self.buyTicket(client,ticket)
        else:
            print('Неудача! Продажа билетов остановлена из за внезапных санкций!')

class MainGermanTicketSeller(ICountryTicketSeller, BankModule.AviaTicketSeller):
    def __init__(self, ticketBase : TicketObservableBase.ObservableTicketBase):
        super().__init__(ticketBase)
        self._AviaTicketSeller__bankList : list = [ BankModule.BankOfGermany() ]
        
    def sellTicket(self, client : BankModule.IBankClient, ticket : TicketModule.Ticket):
        if random.randint(1,3) == 1:
            print('Вам повезло! Немецкий продавец билетов согласился работать!')
            self.buyTicket(client,ticket)
        else:
            print('Неудача! Продажа билетов остановлена из за внезапных санкций!')


class MainFranchTicketSeller(ICountryTicketSeller, BankModule.AviaTicketSeller):
    def __init__(self, ticketBase : TicketObservableBase.ObservableTicketBase):
        super().__init__(ticketBase)
        self._AviaTicketSeller__bankList : list = [ BankModule.BankOfFranch() ]
        
    def sellTicket(self, client : BankModule.IBankClient, ticket : TicketModule.Ticket):
        if random.randint(1,2) == 1:
            print('Вам повезло! Французский продавец билетов согласился работать!')
            self.buyTicket(client,ticket)
        else:
            print('Неудача! Продажа билетов остановлена из за внезапных санкций!')


class AnyOtherTicketSeller(ICountryTicketSeller, BankModule.AviaTicketSeller):
    def __init__(self, ticketBase : TicketObservableBase.ObservableTicketBase):
        super().__init__(ticketBase)
        
    def sellTicket(self, client : BankModule.IBankClient, ticket : TicketModule.Ticket):
        print('Нет продажи билетов в этой стране!')

#интерфейс фабрики продавцов
class ITicketSellerFactory:
	def createSeller(self, ticketBase : TicketObservableBase.ObservableTicketBase):
		pass

#каждая фабрика создает обьект своего типа
class RussianSellerFactory(ITicketSellerFactory):
	def createSeller(self, ticketBase : TicketObservableBase.ObservableTicketBase):
		return MainRussianTicketSeller(ticketBase)

class AmericanSellerFactory(ITicketSellerFactory):
	def createSeller(self, ticketBase : TicketObservableBase.ObservableTicketBase):
		return MainAmericanTicketSeller(ticketBase)

class GermanSellerFactory(ITicketSellerFactory):
	def createSeller(self, ticketBase : TicketObservableBase.ObservableTicketBase):
		return MainGermanTicketSeller(ticketBase)

class FrenchSellerFactory(ITicketSellerFactory):
	def createSeller(self, ticketBase : TicketObservableBase.ObservableTicketBase):
		return MainFranchTicketSeller(ticketBase)

class OtherSellerFactory(ITicketSellerFactory):
	def createSeller(self, ticketBase : TicketObservableBase.ObservableTicketBase):
		return AnyOtherTicketSeller(ticketBase)

class CountryClient(BankModule.IBankClient):
    def __init__(self):
        self.__bonuses = 0
        self.__operationHistory : list = []
        
    def addBonus(self, bonus : int):
        self.__bonuses += bonus
    
    def saveOperation(self, operationText : string):
        self.__operationHistory.append(operationText)
    
    def getBonus(self) -> int:
        return self.__bonuses
    
    def getOperationHistory(self) -> int:
        return self.__operationHistory