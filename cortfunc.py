from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = ''

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


kb = ReplyKeyboardMarkup()
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')

kb.add(button1)
kb.add(button2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать')],
        [
            KeyboardButton(text='Информация')
        ]
    ], resize_keyboard=True
)


@dp.message_handler(text=['Привет!'])
async def start_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет я Бот с Информацией о себе', reply_markup=start_menu)


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
        await state.update_data(age=message.text)
        await message.answer(f"Введите свой рост:")
        await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_growth(message, state):
    await state.update_data(growth=message.text)
    await message.answer(f"Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    dta = await state.get_data()
    m = 10*int(dta['weight'])
    f = 6.25*int(dta['growth'])
    r = 5*int(dta['age'])
    mfr = (m + f - r) + 5
    await message.answer(f'Ваша норма колорий {mfr}')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
