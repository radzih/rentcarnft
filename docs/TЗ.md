# 1. Ціль проекта

Ціль проекта - розробити бот для перегляду доступних до покупки NFT, і для
перегляду статистики по купленим NFT.
Користувач має змогу добавляти куплені NFT (максимум 3 штуки), переглядати доступні
NFT для покупки, переглядати статистику по купленим NFT, замовляти виплату коштів

Під терміном NFT мається на увазі NFT певної коллекції

# 2. Опис бота

Бот складається із наступних функціональних блоків:

1. Функціонал прив'язування NFT до користувача
2. Функціонал перегляду доступних до покупки NFT
3. Функціонал перегляду придбаних NFT
4. Функціонал на отримання коштів
5. Функціонал додавання нових NFT
6. Функціонал зміни мови

## 2.1 Типи користувачів

Бот передбачає три типи користувача бота:

- власник NFT (далі Власник)
- оператор який відсилає кошти (далі Оператор) на перший час, потім потрібно
  автоматизувати
- адмін який буде змогу додавати нові NFT (далі Адмін)

## 2.2 Функціонал користувачів:

Власник:

- Функціонал прив'язування NFT до користувача
- Функціонал перегляду доступних до покупки NFT
- Функціонал перегляду придбаних NFT
- Функціонал на отримання коштів
- Функціонал зміни мови

Оператор:

- Функціонал прив'язування NFT до користувача
- Функціонал перегляду доступних до покупки NFT
- Функціонал перегляду придбаних NFT
- Функціонал на отримання коштів
- Функціонал зміни мови
- також має можливість отримувати сповіщення від бота кому потрібно зробити виплати

Адмін:

- Функціонал прив'язування NFT до користувача
- Функціонал перегляду доступних до покупки NFT
- Функціонал перегляду придбаних NFT
- Функціонал на отримання коштів
- Функціонал зміни мови
- Функціонал додавання нових NFT

## 2.3 Функціонал прив'язування NFT до користувача

При придбанні NFT на [OpenSea](https://opensea.io/), у власника буде можливість
переглянути "Unlockable Content" який:

> Включає вміст, який можна розблокувати, відкритий лише для власника NFT.

В цьому вмісті буде посилання з секретним кодом, при натисканні на нього
власника переадресує на діалог з ботом (приклад посилання https://t.me/botnamebot?start=bdb7556d-fac3-409f-a711-4e311b50bb2f).
Далі в боті власник натискає 'Start' і бот готовий до використання. Щоб NFT почала
приносити прибуток мають бути куплені всі NFT даного типу машини, після того як вони
були куплені всім власникам NFT даного типу приходить повідомлення що машина куплена і
через деякий час почне приносити прибуток. Максимум куплених NFT які можна додати до
бота має бути не більше 3 штук. Якщо користувач додає 4 NFT то бот відповідає що ліміт
по NFT уже досягнений. Якщо NFT була перепродана то бот відповідає що вона була продана
і відв'язує NFT від даного акаунту. Дялі чекає хто переде по посиланню з секретним кодом.

## 2.4 Функціонал перегляду доступних до покупки NFT

В боті при натисканні на команду /cars власник переглядає доступні NFT для покупки.
Перегляд буде представлений у вигляді карток. На картках буде відображена така
інформація:

1. Назва NFT
2. Коллекція
3. Процент від автомобіля
4. Ціна NFT
5. Посилання на покупку на сайті [OpenSea](https://opensea.io/)

## 2.5 Функціонал перегляду придбаних NFT

При натисканні на команду /my власник переглядає придбані NFT.
Перегляд буде представлений у вигляді карток. На картках буде відображена така
інформація:

1. Назва NFT
2. Коллекція
3. Процент від автомобіля
4. Ціна NFT

На картці буде кнопка при натискані на яку можна буде подивитись статистику по данній NFT

## 2.6 Функціонал на отримання коштів

При натисканні на команду /request власник може запросити кошти які були зароблені NFT.
Команду можна використовувати раз в тиждень. Кошти будуть відправленні протягом 24 годин

оператором на адресу гаманця власника(ця адреса береться з [OpenSea](https://opensea.io/)
). Якщо власник не натиснув на команду /request то кошти будуть автоматично відправлені
раз в місяць оператором. При запиті коштів оператор отримає сповіщення від бота що
потрібно відправити кошти, в майбутньому відправка коштів буде автоматичною.

## 2.7 Функціонал додавання нових NFT

При комманді /add бот просить дати посилання на покупку NFT (посилання генерується на
[OpenSea](https://opensea.io/) при створенні NFT) далі бот генерує посилання з секретним
кодом (далі Секретне посилання)і скидає його користувачу. Потім користувач має вставити
це посилання в поле "Unlockable Content" щоб власник мав змогу прив'язати його до свого
акаунту в боті.

Після того як користувач додав посилання він має натиснути на кнопку і підтвердити що
він додав секретне посилання до NFT.

## 2.8 Функціонал зміни мови

При команді /language бот надсилає повідомлення з трьома кнопками для вибору мови.
Доступні мови:

- Російська
- Англійська
- Італійська

При натисканні на кнопку бот змінює мову на вибрану.

# 3. Стек технологій

Для реалізації бота пропонується наступний стек:

- Мова Python
- БД PostgreSQL
- SQLAlchemy ORM
- aiogram
- Redis NoSQL
