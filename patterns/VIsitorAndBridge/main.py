import FakeDBModule
import TicketObservableBase
import BankModule
import random
from pathlib import Path

#MAIN    	
if __name__ == '__main__':
    
    print('> Создаем фабрику для создания намоканных фэйк БД для демонстрации')
    dbFactory = FakeDBModule.FakeDBFactory()
    
    print('> Через фабрику создаем базу на "порту" 5432 на 5 билетов')
    absolute_path_of_json = Path('./patterns/countries.json').resolve()
    newDB = dbFactory.create_db(5432,absolute_path_of_json,5)
    
    appBase = TicketObservableBase.ObservableTicketBase(5432)
    
    client = BankModule.Client()
    
    print('В данном примере реализован паттерн посетитель - через него происходит накопление бонусов и сохранение истории транзакции')
    print('Так же рализован паттерн мост - он позволяет абстрагировать поведение от классов, так чтобы они были взаимозаменяемыми.')
    print('Реализации паттернов содежатся в модуле BankModule.py')
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
                    if wantedTicket.get_ArrivedCountry().getCountryName() != 'Россия' or wantedTicket.get_DepartureCountry().getCountryName() != 'Россия':
                        client.setTicketSeller(BankModule.OutCountryTicketSeller(appBase))
                    else:
                        client.setTicketSeller(BankModule.InCountryTicketSeller(appBase))
                    
                    client.buyTicket(wantedTicket)
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
    