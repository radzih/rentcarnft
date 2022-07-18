from aiogram.dispatcher.filters.state import State, StatesGroup

class AddNewrent(StatesGroup):
    get_rent_days = State()
    get_earnings = State()