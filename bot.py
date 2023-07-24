from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import aiogram.utils.markdown as md
import re
from SQL import SQLighter
# подключаем API токен для телеграмма
from config import TOKEN
import time
# your account id
Test_id_message_send = 123456789

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class Take_info_from_new_user(StatesGroup):
    Select_Game = State()
    Get_Name = State()
    Get_number = State()
    Get_first_inf_about_user = State()
    Get_comfortable_time = State()
    Get_discord_nickname = State()
    Get_information_about_advertising = State()
    Redirect_to_manager = State()






@dp.message_handler(commands=['start'])
async def start_command(message : types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton(text="CS:GO", callback_data="random_value_1"))
    keyboard.add(types.InlineKeyboardButton(text="Dota 2", callback_data="random_value_2"))
    keyboard.add(types.InlineKeyboardButton(text="Valorant", callback_data="random_value_3"))
    keyboard.add(types.InlineKeyboardButton(text="Fortnite", callback_data="random_value_5"))
    keyboard.add(types.InlineKeyboardButton(text="Я уже проходил тренировку", callback_data="random_value_4"))
    await bot.send_message(message.from_user.id, "Привет!" + "\n" 
                           + "На связи тренировочная игровая платформа skilly-training.com " + '\n' +
                           "\n" + 'Какая игра тебя интересует?)' , reply_markup=keyboard)
    
    await bot.send_message(message.from_user.id, "Если ты ошибся с выбором, напиши:" + "\n" 
                           + "/start" + '\n' )
    
    await bot.send_message(Test_id_message_send , "@" + str(message.from_user.username) + ' - Запустил бота')    
    

    print(message.from_user.id)


@dp.callback_query_handler(text="random_value_4")
async def CS_GO_text(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(call.from_user.id, "Если ты уже оплачивал тренировку переходи к нам в чат:" + "\n" +  "\n" +
                                            md.bold('@SkillyTraining')
                                                , parse_mode='markdown')
        
            
@dp.callback_query_handler(text="random_value_1")
async def CS_GO_text(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(call.from_user.id, "Расскажешь, пожалуйста, про себя" + "\n" +
                                                "- сколько тебе лет?" + "\n" +
                                                "- какое текущее звание/эло в CS:GO?" + "\n" +
                                                "- какие цели и ожидания от тренировок на перспективу?"+ "\n"
                                                + "\n" +
                                                "Это нужно для того, чтоб подобрать тебе тренера"
                                                )

    await Take_info_from_new_user.Get_first_inf_about_user.set()
    async with state.proxy() as data:
        data['Game'] = 'CS:GO'
    
@dp.callback_query_handler(text="random_value_2")
async def CS_GO_text(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(call.from_user.id, "Расскажешь, пожалуйста, про себя" + "\n" +
                                                "- сколько тебе лет?" + "\n" +
                                                "- какой текущий mmr в Dota 2?" + "\n" +
                                                "- какие цели и ожидания от тренировок на перспективу?"+ "\n"
                                                + "\n" +
                                                "Это нужно для того, чтоб подобрать тебе тренера"
                                                )
    await Take_info_from_new_user.Get_first_inf_about_user.set()
    async with state.proxy() as data:
        data['Game'] = 'Dota 2'
@dp.callback_query_handler(text="random_value_3")
async def CS_GO_text(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(call.from_user.id, "Расскажешь, пожалуйста, про себя" + "\n" +
                                                "- сколько тебе лет?" + "\n" +
                                                "- какое текущее звание в Valorant?" + "\n" +
                                                "- какие цели и ожидания от тренировок на перспективу?"+ "\n"
                                                + "\n" +
                                                "Это нужно для того, чтоб подобрать тебе тренера"
                                                )
    await Take_info_from_new_user.Get_first_inf_about_user.set()
    async with state.proxy() as data:
        data['Game'] = 'Valorant'
        
@dp.callback_query_handler(text="random_value_5")
async def CS_GO_text(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(call.from_user.id, "Расскажешь, пожалуйста, про себя" + "\n" +
                                                "- Сколько тебе лет?" + "\n" +
                                                "- Какой у тебя ранг (максимальный/актуальный)?" + "\n" +
                                                "- С каких девайсов играешь (ПК/Консоль)?" + "\n" +
                                                "- Какие цели и ожидания от тренировок на перспективу?"+ "\n"
                                                + "\n" +
                                                "Это нужно для того, чтоб подобрать тебе тренера"
                                                )

    await Take_info_from_new_user.Get_first_inf_about_user.set()
    async with state.proxy() as data:
        data['Game'] = 'Fortnite'

@dp.message_handler(state = Take_info_from_new_user.Get_first_inf_about_user)
async def start_command(msg,  state: FSMContext):
    if msg.text != '/start':
        await bot.send_message(msg.from_user.id,
                                "Как тебя зовут ?)")
        print(msg.from_user.id)
        async with state.proxy() as data:
            data['first_info'] = msg.text
            data['nickname'] = msg.from_user.username

        await Take_info_from_new_user.Get_Name.set()
    else:
        await state.finish()
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(types.InlineKeyboardButton(text="CS:GO", callback_data="random_value_1"))
        keyboard.add(types.InlineKeyboardButton(text="Dota 2", callback_data="random_value_2"))
        keyboard.add(types.InlineKeyboardButton(text="Valorant", callback_data="random_value_3"))
        keyboard.add(types.InlineKeyboardButton(text="Я уже проходил тренировку", callback_data="random_value_4"))
        await bot.send_message(msg.from_user.id, "Привет!" + "\n" 
                            + "На связи тренировочная игровая платформа skilly-training.com " + '\n' +
                            "\n" + 'Какая игра тебя интересует?)' , reply_markup=keyboard)

@dp.message_handler(state = Take_info_from_new_user.Get_Name)
async def start_command(msg,  state: FSMContext):
    if msg.text != '/start':
        await bot.send_message(msg.from_user.id,
                                "Напиши, пожалуйста, номер телефона, чтобы мы проверили оплату) ")
        print(msg.from_user.id)
        
        async with state.proxy() as data:
            data['name'] = msg.text

        await Take_info_from_new_user.Get_number.set()
    else:
        await state.finish()
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(types.InlineKeyboardButton(text="CS:GO", callback_data="random_value_1"))
        keyboard.add(types.InlineKeyboardButton(text="Dota 2", callback_data="random_value_2"))
        keyboard.add(types.InlineKeyboardButton(text="Valorant", callback_data="random_value_3"))
        keyboard.add(types.InlineKeyboardButton(text="Я уже проходил тренировку", callback_data="random_value_4"))
        await bot.send_message(msg.from_user.id, "Привет!" + "\n" 
                            + "На связи тренировочная игровая платформа skilly-training.com " + '\n' +
                            "\n" + 'Какая игра тебя интересует?)' , reply_markup=keyboard)  
          
@dp.message_handler(state = Take_info_from_new_user.Get_number)
async def start_command(msg,  state: FSMContext):
    if msg.text != '/start':
        async with state.proxy() as data:
            data['number'] = msg.text
            await bot.send_message(msg.from_user.id,
                                    "Круто, спасибо! Давай теперь расскажем про процесс дальше:" + "\n" +
                                    "- сейчас мы тебе подберем тренера"+ "\n" +
                                    "- выберем время и дату для первой тренировки"+ "\n" +
                                    "- все тренировки y нас походят на нашем сервере в Discord на сервере Skilly - я тебя обязательно добавлю."+ "\n" +
                                    "Там будет создана персональная комната для тебя и тренера."+ "\n" +
                                    "Вы будете общаться и тренироваться внутри нее"+ "\n" +
                                    "\n" +
                                    "Скажи, пожалуйста, когда тебе было бы удобно сделать первую трену?" + "\n"
                                    + "\n" +"\n" +'B формате:' +"\n" + 'Сегодня удобно c 17:00 до 21:00'
                                    +"\n" + 'Завтра c 20:00 до 23:00')
            print(msg.from_user.id)
        await Take_info_from_new_user.Get_comfortable_time.set()
    else:
        await state.finish()
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(types.InlineKeyboardButton(text="CS:GO", callback_data="random_value_1"))
        keyboard.add(types.InlineKeyboardButton(text="Dota 2", callback_data="random_value_2"))
        keyboard.add(types.InlineKeyboardButton(text="Valorant", callback_data="random_value_3"))
        keyboard.add(types.InlineKeyboardButton(text="Я уже проходил тренировку", callback_data="random_value_4"))
        await bot.send_message(msg.from_user.id, "Привет!" + "\n" 
                            + "На связи тренировочная игровая платформа skilly-training.com " + '\n' +
                            "\n" + 'Какая игра тебя интересует?)' , reply_markup=keyboard)
        
@dp.message_handler(state = Take_info_from_new_user.Get_comfortable_time )
async def start_command(msg,  state: FSMContext):
    if msg.text != '/start':
        async with state.proxy() as data:
            data['Comfortable_time'] = msg.text
            await bot.send_message(msg.from_user.id,
                                    "Класс, спасибо. Про удобное время - принято!"+ "\n" + "\n" +

                                    "Заходи пока на наш сервер в Discord:" + "\n" +
                                    "https://discord.gg/skillytraining" + "\n" +"\n" +
                                    
                                    md.bold("Напиши здесь свой ник в дискорде")
                                    , disable_web_page_preview=True, parse_mode="Markdown")
            print(msg.from_user.id)

        await Take_info_from_new_user.Get_information_about_advertising.set()
    else:
        await state.finish()
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(types.InlineKeyboardButton(text="CS:GO", callback_data="random_value_1"))
        keyboard.add(types.InlineKeyboardButton(text="Dota 2", callback_data="random_value_2"))
        keyboard.add(types.InlineKeyboardButton(text="Valorant", callback_data="random_value_3"))
        keyboard.add(types.InlineKeyboardButton(text="Я уже проходил тренировку", callback_data="random_value_4"))
        await bot.send_message(msg.from_user.id, "Привет!" + "\n" 
                            + "На связи тренировочная игровая платформа skilly-training.com " + '\n' +
                            "\n" + 'Какая игра тебя интересует?)' , reply_markup=keyboard)

@dp.message_handler(state = Take_info_from_new_user.Get_information_about_advertising)
async def start_command(msg,  state: FSMContext):
    if msg.text != '/start':
        async with state.proxy() as data:
            data['discrod'] = msg.text
            await bot.send_message(msg.from_user.id,
                                    "Откуда про нас узнал(a)?")
            print(msg.from_user.id)

        await Take_info_from_new_user.Get_discord_nickname.set()
    else:
        await state.finish()
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(types.InlineKeyboardButton(text="CS:GO", callback_data="random_value_1"))
        keyboard.add(types.InlineKeyboardButton(text="Dota 2", callback_data="random_value_2"))
        keyboard.add(types.InlineKeyboardButton(text="Valorant", callback_data="random_value_3"))
        keyboard.add(types.InlineKeyboardButton(text="Я уже проходил тренировку", callback_data="random_value_4"))
        await bot.send_message(msg.from_user.id, "Привет!" + "\n" 
                            + "На связи тренировочная игровая платформа skilly-training.com " + '\n' +
                            "\n" + 'Какая игра тебя интересует?)' , reply_markup=keyboard)


@dp.message_handler(state = Take_info_from_new_user.Get_discord_nickname)
async def start_command(msg,  state: FSMContext):
    if msg.text != '/start':
        async with state.proxy() as data:
            data['Get_information_about_advertising'] = msg.text
            await bot.send_message(msg.from_user.id,
                                    "Спасибо!"+ "\n" +
                                    "В ближайшее время (15-30 минут) тебе в телеграме напишет наш менеджер, расскажет про тренера и подтвердит время!"
                                    + "\n" + "\n" +
                                    "Если у тебя остались дополнительные вопросы - пиши нам в ТГ напрямую @Skillytraining"
                                    + "\n" + "\n" +
                                    "На связи!"+ "\n"

                                    )
            print(msg.from_user.id)

        async with state.proxy() as data:
            chat_id = msg.from_user.id
            button_url = f'tg://openmessage?user_id={chat_id}'
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text='Перейти в чат', url=button_url))
            await bot.send_message(Test_id_message_send,
                                    str(data['Game'])
                                    + "\n" +
                                    str(data['name'])
                                    + "\n" +
                                    "+" + str(data['number']).replace(" ", '').replace("-", '').replace("+", '').replace("(", '').replace(")", '')
                                    + "\n" +
                                    'Информация:'+ "\n" +
                                    str(data['first_info'])
                                    + "\n" +
                                    "Telegram" + "\n" +
                                    "@" + str(data['nickname'])
                                    + "\n" +
                                    'Удобное время:'+ "\n" +
                                    str(data['Comfortable_time'])
                                    + "\n" +
                                    'Ник в дискорде:'
                                    + "\n" +
                                    str(data['discrod']) + '\n' + 
                                    'Откуда про нас узнал(a)?' +'\n' +
                                    str(data['Get_information_about_advertising']) 
                                    , reply_markup=markup)
            
            await state.finish()
            print(data['number'])
            try: 
                SQLighter().add_subscriber(data['number'], msg.from_user.id ,data['nickname'] ,data['name'], data['Game'],data['first_info'],data['Comfortable_time'], data['discrod'],0,0,0)
            except:
                print('Error')

# @dp.message_handler(state = Take_info_start.Get_number)
# async def Select_Game(msg,  state: FSMContext):
#         async with state.proxy() as data:
#             print('123')
#             print(data['name'])
#         print(2)
#         print(msg.text)
#         print(3)
#         print(msg.from_user.username)
#         keyboard = types.InlineKeyboardMarkup(row_width=1)
#         keyboard.add(types.InlineKeyboardButton(text="CS:GO", callback_data="random_value_1"))
#         keyboard.add(types.InlineKeyboardButton(text="Dota 2", callback_data="random_value_2"))
#         keyboard.add(types.InlineKeyboardButton(text="Valorant", callback_data="random_value_3"))
#         await bot.send_message(msg.from_user.id,
#                                'Какая игра тебя интересует?)',
#                              reply_markup=keyboard)
#         await state.finish()   
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)