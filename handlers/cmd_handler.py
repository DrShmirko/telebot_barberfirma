import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from handlers.base_handler import BaseHandler
from states.booking_states import BookingStates


class CmdHandler(BaseHandler):

    def handle(self):

        @self.dp.message_handler(commands=['bookatime'])
        async def process_start_message(message: types.Message):
            await BookingStates.ServiceSelect.set()
            await message.reply("Ok, let's start!")

        @self.dp.message_handler(state='*', commands='cancel')
        @self.dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
        async def cancel_operation(message: types.message, state: FSMContext):
            current_state = await state.get_state()
            if current_state is None:
                await message.reply('Нечего отменять')
                return

            logging.info('Cancelling state %r', current_state)
            await state.finish()
            await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())
