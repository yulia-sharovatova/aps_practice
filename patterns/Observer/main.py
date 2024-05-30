import FakeDBModule
import TicketObservableBase
import time
from pathlib import Path

#MAIN    	
if __name__ == '__main__':
    
    dbFactory = FakeDBModule.FakeDBFactory()
    
    absolute_path_of_json = Path('./patterns/countries.json').resolve()
    newDB = dbFactory.create_db(5432,absolute_path_of_json,10)
    
    print('В данном примере реализован паттерн наблюдатель - через него клиенты подписываются на получение билетов и покупают их когда они появляются в БД.')
    
    print('Создаем товарищей: Васю из Новосибирска, Вову из Чикаго, Тоху из Москвы и Джорджа из Сургута')
    clientVasya = TicketObservableBase.Client('Вася',False,'Новосибирск')
    clientVova = TicketObservableBase.Client('Вова',True,'Чикаго')
    clientToha = TicketObservableBase.Client('Анатолий',True,'Москва')
    clientJorge = TicketObservableBase.Client('Джордж Иванович',True,'Сургут')
    
    appBase = TicketObservableBase.ObservableTicketBase(5432)
    
    print('------------ Исходная база: ----------------')
    appBase.print()
    print('--------------------------------------------')
    print('С помощью паттерна наблюдатель реализована система подписок на билеты по городу отбытия и городу прилета')
    print('Каждый из клиентов указывает город в который он хотел бы полететь и когда такой билет появляется - его покупают и отписываются от ожидания билета')
    print('Основная реализация паттерна содержится в TicketObservableBase.py')
    print('')
    
    print('Вася хочет в Ливерпуль')
    clientVasya.wantToFlyTo(appBase,'Ливерпуль')
    
    print('Вова хочет в Тулуза')
    clientVova.wantToFlyTo(appBase,'Тулуза')
    
    print('Тоха хочет в Дрезден')
    clientToha.wantToFlyTo(appBase,'Дрезден')
    
    print('Джордж хочет в Нью-Йорк')
    clientJorge.wantToFlyTo(appBase,'Нью-Йорк')
    
    print('Билет для Васи добавляем руками во фэйковую внешнюю базу')
    vasyaTicket = { "ticketNumber" : 999, "flightNumber" : 1221, "departureTime" : '21.01.1991 21:11', "arriveTime" : '21.01.1991 21:12', "bagage" : 12, "arrivedCountry" : 'Великобритания', "departureCountry" : 'Россия', "arrivedCity" : 'Ливерпуль', "departureCity" : 'Новосибирск' }
    newDB.addTicketDirectly(vasyaTicket)    
    
    print('')
    print('Обновляем информацию в базе приложения (как будто читаем из внешенй БД)')
    print('')
    appBase.updateTickets()
    
    
    while (clientJorge.isWaitingForTicket() or clientVova.isWaitingForTicket() or clientToha.isWaitingForTicket() or clientVasya.isWaitingForTicket()):
        print('')
        print('Добавляем случайных 300 билетов во внешнюю базу')
        newDB.addRandomTicketsToBase(300)
    #    
        print('Ждем 5 сек и обновляем базу нашего приложения')
        time.sleep(5)
        print('')
        appBase.updateTickets()
    
    print('Все клиенты получили по билету!')
    
    
    #newDB.printTickets()    
    