# VisitorAndBridge

<div align="center">
  <img src="https://math4everyone.info/media/blog_images/%D0%9F%D0%BE%D1%81%D0%B5%D1%82%D0%B8%D1%82%D0%B5%D0%BB%D1%8C.jpg" width="300" height="300">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Yugra_Bridge_2.jpg/266px-Yugra_Bridge_2.jpg" width="300" height="300">
</div>

Этот проект демонстрирует реализацию двух паттернов: 
* Посетитель(Поведенческий тип)
* Мост(Структурный тип)

основная реализация паттерна содержится в модуле **AviaSellerModule.py**

## Реализованные модули:

### BankModule 
* IBankClient
* IBank
* ITicketSeller 
* Sberbank
* Tinkoff
* VTB

подробно описаны в проекте AbstaractFactoryAndAdapter, но

* Client - изменил поведение так, чтобы реализовывать паттерн посетитель
* AviaTicketSeller - изменил поведение так, чтобы реализовывать паттерн посетитель

* InCountryTicketSeller - наследники AviaTicketSeller(который наследник от ITIcketSeller) через мост взаимозаменяймы
* OutCountryTicketSeller

### FakeDBModule
(подробно описан в проекте AbstaractFactoryAndAdapter) 
* IFakeDB 
* AbstractDBFactory
* FakeDBFactory
* FakeDB
* FakeDBDriver

### TicketModule 
(подробно описан в проекте AbstaractFactoryAndAdapter)
* weightType
* IBagage
* KgBagage
* NonKgBagage
* AdapterNonKgBagage
* Country
* Ticket

### TicketObservableBase
(подробно описан в Observer)
* ITicketObserver
* ITicketObservable
* ObservableTicketBase