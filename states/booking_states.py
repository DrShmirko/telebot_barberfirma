from aiogram.dispatcher.filters.state import StatesGroup, State


class BookingStates(StatesGroup):
    ServiceSelect = State()
    BarberSelect = State()
    DaySelect = State()
    TimeSelect = State()
