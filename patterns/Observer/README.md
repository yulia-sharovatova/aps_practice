# Observer

<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/ru/thumb/0/0a/The_Watcher.jpg/201px-The_Watcher.jpg" width="500" height="300">
</div>

Этот проект демонстрирует реализацию одного паттерна: 
* Наблюдатель (Поведенческий тип)

Основная реализация паттерна содержится в **TicketObservableBase.py**

## Реализованные модули:


### FakeDBModule 
(подробно описан в AbstractFactoryAndAdapter)
* IFakeDB 
* AbstractDBFactory
* FakeDBFactory
* FakeDB
* FakeDBDriver
### TicketModule 
(подробно описан в AbstractFactoryAndAdapter)
* weightType
* IBagage
* KgBagage
* NonKgBagage
* AdapterNonKgBagage
* Country
* Ticket
### TicketObservableBase
* ITicketObserver - интерфейс наблюдателя за билетом
* ITicketObservable - интерфейс класса за которым следят 
* ObservableTicketBase - реализация внутренней базы приложения с возможностью подписки на появившийся билет
* Client - реализация наблюдателя - клиент который хотел бы купить определенный билет