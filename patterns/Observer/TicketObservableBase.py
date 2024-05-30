from enum import Enum
import string
import datetime
import FakeDBModule
import TicketModule

#интерфейс наблюдателя за появлением билетов - все должны быть готовы получить его
class ITicketObserver():
	def recieveTicket(self, ticket : TicketModule.Ticket):
		pass

#интерфейс обьекта реализующего наблюдение (или наблюдаемого)
class ITicketObservable():
	def subscribeOnTicket(self, observer: ITicketObserver, departure_city : string, arrive_city : string):
		pass

	def unsubscribe(self, observer: ITicketObserver):
		pass

	def __notify(self, observer: ITicketObserver, ticket : TicketModule.Ticket):
		pass

#реализация базы билетов внутри приложения с функцией рассылки необходимых билетов
class ObservableTicketBase(ITicketObservable):
    def __init__(self, portToConnect : int):
        self.__ticketList : list = []
        self.__observersAndCities : list = []
        self.__fakeDriver = FakeDBModule.FakeDBDriver()
        
        self.__fakeDriver.connectToDB(portToConnect)
        self.__ticketList = self.__fakeDriver.readDataFromDB()
        
    def updateTickets(self):
        self.__ticketList = []
        tickets = self.__fakeDriver.readDataFromDB()
        for ticket in tickets:
            self.__addTicket(ticket)
        
    def __addTicket(self, ticket : TicketModule.Ticket): 
        self.__ticketList.append(ticket)
        
        for observerDict in self.__observersAndCities:
            if ticket.get_ArrivalCity() == observerDict['arrivalCity'] and ticket.get_DepartureCity() == observerDict['departureCity']:
                self.__notify(observerDict['client'], ticket)
                

    def subscribeOnTicket(self, observer: ITicketObserver,departure_city : string, arrive_city : string):
        self.__observersAndCities.append({ 'client' : observer, 'arrivalCity' : arrive_city, 'departureCity' : departure_city })
        
    def unsubscribe(self, observer: ITicketObserver):
        for observerDict in self.__observersAndCities:
            if observerDict['client'] == observer:
                self.__observersAndCities.remove(observerDict)
                print('Клиент отписался от получения информации о билетах')
    
    def __notify(self, observer: ITicketObserver, ticket : TicketModule.Ticket):
        observer.recieveTicket(ticket) 

    def buyTicket(self, ticket : TicketModule.Ticket):
        self.__fakeDriver.deleteTicketFromDB(ticket)
        
    def print(self):
        print('--- все билеты ----')
        for ticket in self.__ticketList:
            ticket.print()

#реализация наблюдателя
class Client(ITicketObserver):
    def __init__(self, name : string, isRegistred : bool, livedIn : string):
        self.__name : string = name
        self.__subscribedBase : ITicketObservable = None
        self.__isRegistred : bool = isRegistred
        self.__livedIn : bool = livedIn
        

    def wantToFlyTo(self, waitForTicketInBase : ObservableTicketBase, arrive_city : string):
        self.__subscribedBase = waitForTicketInBase
        self.__subscribedBase.subscribeOnTicket(self, self.__livedIn, arrive_city)
    
    def recieveTicket(self,  ticket : TicketModule.Ticket):
        if self.__isRegistred == False:
            print(self.__name,': Искомый билет ', ticket.get_DepartureCity(), '-->', ticket.get_ArrivalCity(), ' появился, но я его не куплю - я не зарегистрировался(' )
            self.__subscribedBase.unsubscribe(self)
            self.__subscribedBase = None
            return
        
        print(self.__name, ': Ура! Я лечу в ', ticket.get_ArrivalCity(), '!', 'Подписка на билет мне больше не нужна!')
        self.__subscribedBase.unsubscribe(self)
        self.__subscribedBase = None

    def isWaitingForTicket(self) -> bool:
        return self.__subscribedBase != None