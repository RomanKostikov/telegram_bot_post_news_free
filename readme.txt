Ход Разработки:
1. Создал нового телеграмм бота:
Done! Congratulations on your new bot. You will find it at .
You can now add a description, about section and profile picture for your bot, see /help for a list of commands.
By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it.
Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
6688503172:YOUR TOKEN # нужно копировать весь код(вместе с этим 6688503172:!!!)
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api

2. После создания телеграмм бота и получения его токена, необходимо добавить его в свой канал и сделать админом.
3. Далее получить свой чат id (либо с помощью телеграмм бота:Get My ID, либо при помощи кода и вывода в консоль
(но нужно тогда хотя бы одно сообщение новое отправить на канале, после присоединения бота)
4. Все работает
- зачем запускать было джанго сервер, если команда и отдельно запускается??
Ответ: бот создан в составе джанго проекта т.к в дальнейшем можно расширить его функционал

5. Необходимо развернуть данного бота на сервере(для начала на dev)-развернул копированием файлов через FZ
и запуском docker-compose(для бота не нужно настравивать nginx, gunicorn и БД тоже пока не нужна-done.

6. Создаем отдельный проект на основе этого для запуска в продакшен.
