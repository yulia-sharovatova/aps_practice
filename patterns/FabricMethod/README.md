# FabricMethod

<div align="center">
  <img src="https://cs11.pikabu.ru/post_img/2020/01/27/10/158014754519045936.jpg" width="500" height="250">
</div>

Этот проект демонстрирует реализацию одного паттерна: 
* Фабричный метод (Порождающий тип)

основная реализация паттерна содержится в модуле **AviaSellerModule.py**

## Реализованные модули:

### AviaSellerModule
классы, реализованные в модуле:
* ICountryTicketSeller - интерфейс продажника билета для выбранной страны
* ITicketSellerFactory - интерфейс фабрики для создания продавцов (используется в фабричном методе)

* MainRussianTicketSeller - реализация основные продажники по странам
* MainAmericanTicketSeller
* MainGermanTicketSeller
* MainFrenchTicketSeller
* AnyOtherTicketSeller

* RussianSellerFactory - реализация фабрики по созданию основных продажников
* AmericanSellerFactory
* GermanSellerFactory
* FrenchSellerFactory
* OtherSellerFactory

* CountryClient
### BankModule 
* IBankClient - интерфейс клиента инициирующего банковскую операцию
* IBank - интерфейс для банка
* ITicketSeller - интерфейс для продавца билетов 

* Sberbank - конкретный зеленый банк 
* Tinkoff - конкретный желтый банк
* VTB - конкретный синий банки

* BankOfAmericaCorporation - тоже банки
* BankOfFrench
* BankOfGerman

* Client - клиент производящий операцию покупки
* AviaTicketSeller - класс с реализацией продажника
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