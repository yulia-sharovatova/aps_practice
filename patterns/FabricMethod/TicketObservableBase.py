from enum import Enum
import string
import FakeDBModule
import TicketModule

class ITicketObserver():
	def recieveTicket(self, ticket : TicketModule.Ticket):
		pass

class ITicketObservable():
	def subscribeOnTicket(self, observer: ITicketObserver, departure_city : string, arrive_city : string):
		pass

	def unsubscribe(self, observer: ITicketObserver):
		pass

	def __notify(self, observer: ITicketObserver, ticket : TicketModule.Ticket):
		pass

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

    def deleteTicket(self, ticket : TicketModule.Ticket):
        self.__fakeDriver.deleteTicketFromDB(ticket)
        
    def print(self):
        print('--- все билеты ----')
        for ticket in self.__ticketList:
            ticket.print()
            
    def getTicket(self, ticketNumber : int) -> TicketModule.Ticket:
        for ticket in self.__ticketList:
            if ticket.get_ticketNumber() == ticketNumber:
                return ticket
        return None
 