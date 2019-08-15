# Emodis бот
 _______ .___  ___.   ______    _______   __       _______.
|   ____||   \/   |  /  __  \  |       \ |  |     /       |
|  |__   |  \  /  | |  |  |  | |  .--.  ||  |    |   (----`
|   __|  |  |\/|  | |  |  |  | |  |  |  ||  |     \   \    
|  |____ |  |  |  | |  `--'  | |  '--'  ||  | .----)   |   
|_______||__|  |__|  \______/  |_______/ |__| |_______/    


Как мы знаем, чаты в телеграме - основа общения мессенджера. Существует множество способов работы с ними.
Однако так нельзя сказать о ВК.

Чаты в Вконтакте особенно популярны у россиян.
Соотвественно была принята идея чат-бота в телеграме под названием Combot.
Какие есть возможности комбота?
- статистика.
- список бесед по тематикам в порядке популярности.
- антиспам система.

Единственный ми-нус бесед Вконтакте
- ограничение в 500 человек.
- нельзя администраторам удалять чужие сообщения.
- нет read only режима на определенное время.

Для работы с беседой и статистикой необходим сайт. Доступ к настройкам беседы только администраторам.

Как работает статистика?
Каждый час записываются итоги общения каждого участника человека.
Соотвественно каждый раз будет записываться строчка такого типа:
- Номер ID.
- Номер пользователя из таблицы пользователей. (для того чтобы можно было посмотреть насколько он активный в других беседах).
- Номер беседы из таблицы бесед.
- Дата с указанием часа за которое время идет запись данных.
- Количество всех сообщений пользователя.
- Из них - кол-во голосовых сообщений пользователя.
- Из них - кол-во стикеров пользователя.
- Само сообщение (мб почему и не хранить?)


Таблица еще 1 связывающая: Человек и беседа
- ID
- Номер пользователя из таблицы пользователей. (для того чтобы можно было посмотреть насколько он активный в других беседах).
- Номер беседы из таблицы бесед.
- Дата с момента прихода в беседу
- Дата последнего сообщения


дополнительные параметры, которые можно высчитывать: Flood%, Lvl, Активность - только хз как 