# AbstractFactoryAndAdapter

<div align="center">
  <img src="https://img.freepik.com/premium-photo/giant-factory-sky_549702-1971.jpg" width="300" height="300">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Adapter_2011-02-27.jpg/220px-Adapter_2011-02-27.jpg" width="300" height="300">
</div>

Этот проект демонстрирует реализацию двух паттернов: 
* Абстрактная фабрика (Порождающий тип)
* Адаптер (Структурный)

основная реализация паттернов содержится в модуле **FakeDBModule.py**

## Реализованные модули:

### FakeDBModule
классы, реализованные в модуле
* IFakeDB - интерфейс для псевдо физической БД
* AbstractDBFactory - абстрактная фабрика создания БД
* FakeDBFactory - реализация фабрики
* FakeDB - реализация БД
* FakeDBDriver - драйвер для работы с фейковой бд
### TicketModule 
* weightType - перечисление типов весов
* IBagage - интерфейс для работы с багажом (используется для адаптации)
* KgBagage - багаж с типом веса кг
* NonKgBagage - багаж с типом веса фут
* AdapterNonKgBagage - адаптер из одного веса в другой
* Country - класс обозначающий страну
* Ticket - класс для билета
