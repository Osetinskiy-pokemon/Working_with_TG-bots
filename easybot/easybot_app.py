from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "6187761181:AAGiFD7kYqwEed7wuPhyE_uR2MhvwxW-Vro"
# в боте у нас создается поток (loop) в котором будет работать dispatcher
bot = Bot(token=TOKEN)
# Dispatcher принимает все апдейты и обрабатывает их - диспетчер
dispatcher = Dispatcher(bot)


# также нам необходим хендлер - класс, который используется для работы с очередью сообщений, связанной с потоком.
# Хэндлер позволяет отправлять сообщения в другие потоки с задержкой или без, а также обрабатывать полученные
# сообщения.

# в этот хендлер будут лететь текстовые сообщения
@dispatcher.message_handler()  # декоратор, который принимает текстовые сообщения
async def get_message(message: types.Message):
    # для ответа на сообщение нам нужен метод sendMessage
    chat_id = message.chat.id

    # отправим текстовое сообщение в качестве ответа
    text = "Привет! Это простой бот."
    sent_message_1 = await bot.send_message(chat_id=chat_id, text=text)
    print(sent_message_1.to_python())

    # отправим фотографию в качестве ответа
    sent_message_2 = await bot.send_photo(chat_id=chat_id, photo='https://i.pinimg.com/originals/f4/d2/96'
                                                                 '/f4d2961b652880be432fb9580891ed62.png', caption="Ух, "
                                                                                                                  "ты только "
                                                                                                                  "посмотри на "
                                                                                                                  "него!")
    # достаем уникальный идентификатор картинки, служит для сравнения фотографий
    print(sent_message_2.photo[-1].file_unique_id)

    # смена названия супергруппы
    # sent_message_3 = await bot.set_chat_title(chat_id=-1001359487461, title="Моя мини-супер группа")
    # print(sent_message_3) # вернет True в случае успеха

    # достать invite-ссылку для чата
    # invite_link = await bot.export_chat_invite_link(chat_id=-1001359487461)
    # print(invite_link)

    # получить username бота
    # sent_message_5 = await bot.get_me()
    # print(sent_message_5.username)


executor.start_polling(dispatcher)
