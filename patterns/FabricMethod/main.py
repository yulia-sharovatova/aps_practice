import FakeDBModule
import TicketObservableBase
import random
import AviaSellerModule
from pathlib import Path

#MAIN    	
if __name__ == '__main__':
    
    dbFactory = FakeDBModule.FakeDBFactory()
    
    absolute_path_of_json = Path('./patterns/countries.json').resolve()
    newDB = dbFactory.create_db(5432,absolute_path_of_json,5)
    
    appBase = TicketObservableBase.ObservableTicketBase(5432)
    
    client = AviaSellerModule.CountryClient()
    
    seller : AviaSellerModule.ICountryTicketSeller = None
    sellerFactory : AviaSellerModule.ITicketSellerFactory = None
    
    print('В данном примере реализован паттерн фабричный метод. Обьекты осуществляющие операции продажи штампуются на соответсвующих фабриках. При этом для обьектов в классе интерфейсов родителей установлен фабричный метод.')
    print('основная реализация паттерна содержится в модуле AviaSellerModule.py')
    print('')
    
    choosenMenu = 0
    while choosenMenu != 5:
        print('')    
        print('Доступные операции:')
        print('1. Посмотреть билеты')
        print('2. Купить билет ')
        print('3. Посмотреть количетство бонусов ')
        print('4. Посмотреть историю операций ')
        print('5. Улететь (выйти из программы) ')    
        choosenMenuText=input('Выберите:')
        choosenMenu=int(choosenMenuText)
        
        print('')
        match choosenMenu:
            case 1:
                appBase.updateTickets()
                appBase.print()
                newDB.addRandomTicketsToBase(random.randint(1,3))
            case 2:
                ticketNumber = input('Введите номер билета который купим:')
                wantedTicket = appBase.getTicket(int(ticketNumber))
                
                if wantedTicket == None:
                    print ('Не могу найти билет с таким номером')
                else:
                    departureCountryName = wantedTicket.get_DepartureCountry().getCountryName()
                    match departureCountryName:
                        case 'Россия':
                            sellerFactory = AviaSellerModule.RussianSellerFactory()
                        case 'Германия':
                            sellerFactory = AviaSellerModule.GermanSellerFactory()
                        case 'Франция':
                            sellerFactory = AviaSellerModule.FrenchSellerFactory()
                        case 'США':
                            sellerFactory = AviaSellerModule.AmericanSellerFactory()
                        case _:
                            sellerFactory = AviaSellerModule.OtherSellerFactory()
                        
                    
                    seller = sellerFactory.createSeller(appBase)
                    seller.sellTicket(client,wantedTicket)
            case 3:
                print('Количество бонусов на данный момент:', client.getBonus())
            case 4:
                for operation in client.getOperationHistory():
                    print(operation)
            case 5:
                print('До свидания')
            case _:
                print('Неизвестная операция меню')    
        
    #newDB.printTickets()    
    
