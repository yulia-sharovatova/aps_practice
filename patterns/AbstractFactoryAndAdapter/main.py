import FakeDBModule
from pathlib import Path

#MAIN    	
if __name__ == '__main__':
    
    print('В данном примере реализован паттерн абстрактная фабрика обьекты создаются через интерфейсы с дополнительной проверкой')
    print('Так же в данном примере реализован паттерн адаптер - адаптирующий меру весов для банажа,если вылет происходит из странны с мерой весов отличной от кг')
    print('основная реализация паттернов содержится в модуле FakeDBModule.py')
    print('')
    
    print('> Создаем фабрику для создания намоканных фэйк БД для демонстрации')
    dbFactory = FakeDBModule.FakeDBFactory()
    
    print('> Через фабрику создаем базу на "порту" 5432 на 20 билетов')
    absolute_path_of_json = Path('./patterns/countries.json').resolve()
    newDB = dbFactory.create_db(5432,absolute_path_of_json,20)
    
    newDB.printTickets()
    
    print('> Через фабрику пробуем создать еще одну базу на том же порту')
    
    #использование паттерна абстрактная фабрика позволило создавать обьекты через сторонний класс, проверяя условия для создания обьекта
    newDB2 = dbFactory.create_db(5432,'',5)
    
    print('> Поскольку создание деллигировано в отдельный класс с проверкой - база не создалась')
    print(newDB2)
    
    fakeDriver = FakeDBModule.FakeDBDriver()
    fakeDriver.connectToDB(5432)
    
    ticketList = fakeDriver.readDataFromDB()
    
    print('------------ выводим разобранные обьекты ----------------')
    for ticket in ticketList:
        ticket.print()
    print('---------------------------------------------------------')
    print('Разбором данных из намоканной БД занимается отдельно написанный драйвер. В случае если страна отправления использует веса не в кг он использует адаптер из фунтов и переводит вес.')
    print('------------ С помощью адаптера были адаптированы веса багажа в билетах ----------------')
    for adaptedTicket in ticketList:
        for notAdaptedTicket in newDB.getTicketList():
            if adaptedTicket.get_ticketNumber() == notAdaptedTicket['ticketNumber']:
                if adaptedTicket.get_bagage_weight() != notAdaptedTicket['bagage']:
                    adaptedTicket.print()
                    print('Вес билета был адаптирован в кг через адаптер')
                    print(notAdaptedTicket['bagage'],' --> ', adaptedTicket.get_bagage_weight())
                    print('---------------')
    print('---------------------------------------------------------') 
    