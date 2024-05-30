import TicketModule
import string
import json
import datetime
from datetime import timedelta
from datetime import datetime
import random

class IFakeDB:
    def __mockUpBase(self):
        pass
    
    def printTickets(self):
        pass
    
    def getTicketList(self)-> list:
        pass
    
    def deleteTicket(self, ticketNumber : int):
        pass
    
    def getPathToCountryJson(self)-> string:
        pass
    
    def addRandomTicketsToBase(self, countOfTickets : int):
        pass
    
    def addTicketDirectly(self, ticket : dict):
        pass
    
class AbstractDBFactory():
    busyPorts : dict = {}
    def create_db(self) -> IFakeDB:
        pass
    

class FakeDBFactory(AbstractDBFactory):
    
    def create_db(self, portNumber : int, pathToListCountries:string, countOfTickets : int ) -> IFakeDB:
        if portNumber in AbstractDBFactory.busyPorts.keys():
            print('Port already busy by another DB')
            return None
        else:
            newFakeDB = FakeDB(portNumber,pathToListCountries,countOfTickets)
            AbstractDBFactory.busyPorts[portNumber] = newFakeDB
            return newFakeDB
        
        

class FakeDB(IFakeDB):
    def __init__(self,portNumber : int, pathToListCountries:string, countOfTickets : int ): 
        self.__ListOfTickets : list =[]
        self.__portNumber : int = portNumber
        self.__pathToListCountries : string = pathToListCountries
        self.__mockUpBase(countOfTickets)
    
    def getPathToCountryJson(self)-> string:
        return self.__pathToListCountries
        
    def getTicketList(self) -> list:
        return self.__ListOfTickets
    
    def __mockUpBase(self, countOfTickets : int):        
        for currentTicketNumber in range(0, countOfTickets):
            randomTicket = self.__generateRandomTicket()
            self.__ListOfTickets.append(randomTicket)
    
    def __generateRandomTicket(self) -> dict:
        
        randomTcketNumber : int = random.randint(0, 1000)
        randomFlightNumber : int = random.randint(0, 1000)

        randomTicketPrice: int = random.randint(3000, 100000)
        
        #читаем какие страны и города есть
        readedJson=[]
        with open(self.__pathToListCountries, encoding='utf-8') as f:
            readedJson = json.load(f)

        #получаем случайный город и страну отправления
        randomDepartureCountry = self.__getRandomCountry(readedJson)
        randomDepartureCity = self.__getRandomCity(readedJson,randomDepartureCountry)
        
        #получаем случайный город и страну отправления
        randomArriveCountry = self.__getRandomCountry(readedJson)
        randomArriveCity = self.__getRandomCity(readedJson,randomArriveCountry)
        
        #получаем случайную дату отправления и прибытия
        now = datetime.now()
        anyFutureTime = datetime.strptime('21.12.2025 00:00', '%d.%m.%Y %H:%M')

        randomDepartureDate=self.__random_date(now,anyFutureTime)
        randomArriveDate=self.__random_date(randomDepartureDate,anyFutureTime)
        
        #случайный максимально допустимый вес багажа
        randomBagage = random.randint(0, 100)    
        
        randomTicket = { "ticketNumber" : randomTcketNumber, "flightNumber" : randomFlightNumber, "ticketPrice" : randomTicketPrice, "departureTime" : randomDepartureDate.strftime('%d.%m.%Y %H:%M'), "arriveTime" : randomArriveDate.strftime('%d.%m.%Y %H:%M'), "bagage" : randomBagage, "arrivedCountry" : randomArriveCountry, "departureCountry" : randomDepartureCountry, "arrivedCity" : randomArriveCity, "departureCity" : randomDepartureCity }
        
        return randomTicket

    def __getRandomCountry(self, readedJson:list ) -> string:
        #получаем случайную страну
        countryList=[]
        for country in readedJson:
            countryList.append(country['country'])
        
        randomCountryNumber = random.randint(0, len(countryList)-1)
        
        randomCountry = countryList[randomCountryNumber]
        
        return randomCountry    
                
    def __getRandomCity(self, readedJson:list, targetCountry : string ) -> string:
        countryCities=[]
        for country in readedJson:
            if country['country'] == targetCountry:
                for oneCity in country['cities']:
                    countryCities.append(oneCity['name'])
        
        randomCityNumber = random.randint(0, len(countryCities)-1)
        randomCity = countryCities[randomCityNumber]
        
        return randomCity 
    
    def __random_date(self, start, end) -> datetime:
        num_days   = (end - start).days
        if num_days <= 1: 
            num_days=2
            
        rand_days   = random.randint(1, num_days)
        random_date = start + timedelta(days=rand_days)
        return random_date

    def printTickets(self):          
        for ticket in self.__ListOfTickets:
            print(ticket)
    
    def deleteTicket(self, ticketNumber : int):          
        for ticket in self.__ListOfTickets:
            if ticket['ticketNumber'] == ticketNumber:
                self.__ListOfTickets.remove(ticket)     
    
    def addRandomTicketsToBase(self, countOfTickets : int):
        self.__mockUpBase(countOfTickets)
    
    def addTicketDirectly(self, ticket : dict):
        self.__ListOfTickets.append(ticket)
        
 #используем синглтон, он в зачет не идет, но по логике как будто направшивается - драйвер на приложение на один тип должен быть один
class FakeDBDriver:
    __instance = None
    def __new__(cls,*args,**knwargs):
        if cls.__instance == None:
            return super().__new__(cls)
        else:
            return cls.__instance 
        
    def __init__(self):
        self.__currentConnectedPort : int =0
        self.__currentConnectedInstance : IFakeDB =None
    
    def connectToDB(self, port : int):
        if port in AbstractDBFactory.busyPorts:
            self.__currentConnectedPort = port
            self.__currentConnectedInstance = AbstractDBFactory.busyPorts[port]
            
            print('Подключился к базе по порту', self.__currentConnectedPort)       
        else:
            print('Подключение не удалось')
    
    def deleteTicketFromDB(self, ticket : TicketModule.Ticket):
        self.__currentConnectedInstance.deleteTicket(ticket.get_ticketNumber())
    
        
    #функция читает данные из БД и возвращает список внутренних обьектов типа ticket        
    def readDataFromDB(self) -> list:
        fakeDataTicketList = self.__currentConnectedInstance.getTicketList()
        
        nonKgCountryList=[]
        readedJson=[]
        
        returnTicketList=[]
        
        with open(self.__currentConnectedInstance.getPathToCountryJson(), encoding='utf-8') as f:
            readedJson = json.load(f)
        
        for jsoncountry in readedJson:
            if jsoncountry['weight'] != 'kg':
                nonKgCountryList.append(jsoncountry['country'])
        
        
        for ticket in fakeDataTicketList:
            
            ticketNumber=ticket['ticketNumber']
            flightNumber=ticket['flightNumber']
            
            ticketPrice=ticket['ticketPrice']
            
            
            departureTime= datetime.strptime(ticket['departureTime'], '%d.%m.%Y %H:%M')
            arriveTime= datetime.strptime(ticket['arriveTime'], '%d.%m.%Y %H:%M')
            
            arrivedCountryString=ticket['arrivedCountry']
            departureCountryString=ticket['departureCountry']
            
            arrivedCity=ticket['arrivedCity']
            departureCity=ticket['departureCity']
            
            arrivedCountry=TicketModule.Country(TicketModule.weightType.kg,arrivedCountryString)
            if arrivedCountryString in nonKgCountryList:
                arrivedCountry=TicketModule.Country(TicketModule.weightType.foot,arrivedCountryString)
            
            departureCountry=TicketModule.Country(TicketModule.weightType.kg,departureCountryString)
            if departureCountryString in nonKgCountryList:
                departureCountry=TicketModule.Country(TicketModule.weightType.foot,departureCountryString)
            
            #используем адаптер
            #если вылет из страны у которой используется не кг мера - адаптируем через адаптер до кг и записываем в билет
            ticketBagage = TicketModule.KgBagage(ticket['bagage'])
            
            if departureCountry.getCountryWeight != TicketModule.weightType.kg:
                nonkgBagage = TicketModule.NonKgBagage(ticket['bagage'])
                new_weight = TicketModule.AdapterNonKgBagage(nonkgBagage.get_weight()).get_weight()
                ticketBagage = TicketModule.NonKgBagage(new_weight)
            
            newTicket=TicketModule.Ticket(ticketNumber,flightNumber,ticketPrice, departureTime,arriveTime,ticketBagage,arrivedCountry,departureCountry,departureCity,arrivedCity)
            
            returnTicketList.append(newTicket)
        return returnTicketList