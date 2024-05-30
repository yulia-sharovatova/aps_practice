from enum import Enum
import string
import datetime


#основная мысль и допущения решающееся с помощью адаптера:
#Наше "приложение" было изначально разработано для рейсов внутри россии и в страны где используется система измернения кг/см, затем были включены
#рейсы из стран где система измерения весов фунт/фут, но переписывать классы не стали чтобы не ломать завязанную на нее логику и написали адаптер
#приводящий веса и размеры к нужному виду

#таким образом используется паттерн адаптер для:
#в билетах на рейсы которые вылетают из стран, где используется не та система измерения, которая нужна через апдаптер поля приводятся к нужному виду, для представления внутри приложения

#--------------- перечисления для удобства -------------
class weightType(Enum):
    kg = 1
    foot = 2

#----------------- вспомогательные классы между бизнес логикой и приложением -----------------
#вес
class IBagage:
	def get_weight(self) -> float:
		pass


class KgBagage(IBagage):
	def __init__(self):
		self.__current_weight : float = 0.0
		
	def __init__(self, cw: float):
		self.__current_weight = cw

	def get_weight(self) -> float:
		return self.__current_weight

class NonKgBagage:
	def __init__(self, cw: float):
		self.__current_weight = cw

	def get_weight(self) -> float:
		return self.__current_weight

#Adapter class
class AdapterNonKgBagage(NonKgBagage, IBagage):
	def __init__(self, cw: float):
		super().__init__(cw)
    
	def get_weight(self) -> float:
		return super().get_weight() * 0.45359237

class Country:
    def __init__(self):
        self.__countryWeight : weightType = weightType.kg
        self.__name='None'
    def __init__(self, countryWeight : weightType, name : string ):
        self.__countryWeight : weightType = countryWeight
        self.__name : string =name
        
    def print(self):
        print("Страна:", self.__name)
        if self.__countryWeight == weightType.kg: print('Мера веса: кг')
        else: print('Мера веса: фут')
    
    def getCountryWeight(self):
        return self.__countryWeight


class Ticket: 
    def __init__(self):
        self.__ticketNumber : int = 0
        self.__flightNumber : int = 0
        self.__departureTime : datetime=datetime.strptime('00.00.0000 00:00', '%d.%m.%Y %H:%M')
        self.__arriveTime : datetime=datetime.strptime('00.00.0000 00:00', '%d.%m.%Y %H:%M')
        self.__arrivedCountry : Country=Country()
        self.__bagage : KgBagage = KgBagage()
        self.__departureCountry : Country=Country()
        self.__arrivedCity : string = ""
        self.__departureCity : string= ""

    def __init__(self,ticketNumber : int, flightNumber : int, departureTime : datetime, arriveTime : datetime, ticketBagage : KgBagage,arrivedCountry : Country, departureCountry : Country, departureCity : string, arrrivedCity : string): 
        self.__ticketNumber : int = ticketNumber
        self.__flightNumber : int = flightNumber
        self.__departureTime : datetime=departureTime
        self.__arriveTime : datetime=arriveTime
        self.__bagage : KgBagage=ticketBagage 
        self.__arrivedCountry : Country=arrivedCountry
        self.__departureCountry : Country=departureCountry
        self.__arrivedCity : string = arrrivedCity
        self.__departureCity : string= departureCity
    
    def print(self):
        print('---------- ', self.__departureCity,' --> ', self.__arrivedCity,'-------------')
        print('Номер билета:', self.__ticketNumber) 
        print('Номер рейса:', self.__flightNumber)
        print('Время отправления:',self.__departureTime) 
        print('Время прибытия:',self.__arriveTime )
        print('Багаж (вес адаптирован в кг):',self.__bagage.get_weight())  
        print('Страна отправления:')
        self.__departureCountry.print() 
        print('Город отправления:',self.__departureCity)
        print('Страна прибытия:')
        self.__arrivedCountry.print()
        print('Город прибытия:',self.__arrivedCity )
        print('----------------------------------------------')
    
    def get_bagage_weight(self):
        return self.__bagage.get_weight()
    
    def get_ticketNumber(self):
        return self.__ticketNumber