import logging
import os
from aiogram import Bot, Dispatcher, executor, types
import asyncio

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import filters
from aiogram.types import BotCommand, BotCommandScopeDefault

from handlers.cmd_handler import CmdHandler
from handlers.payment_handler import PaymentHandler


class TelBot:
    def __init__(self):
        logging.basicConfig(level=logging.INFO,
                            format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
        self.bot = Bot(os.getenv('BOT_TOKEN'))
        self.storage = MemoryStorage()
        self.dp = Dispatcher(self.bot, storage=self.storage)
        self.cmd_handler = CmdHandler(self.dp)
        self.payment_handler = PaymentHandler(self.dp)


    async def set_bot_commands(self):
        commands = [
            BotCommand(command='bookatime', description='Записаться в барбершоп'),
            BotCommand(command='cancel', description='Отмена')
        ]
        await self.bot.set_my_commands(commands, scope=BotCommandScopeDefault())

    def handle(self):
        #### Register handlers
        self.cmd_handler.handle()
        self.payment_handler.handle()

        @self.dp.message_handler(commands=['Wow'])
        async def process_wow(message: types.Message):
            print(message.text)
            await message.answer("Wow, Wow")

        @self.dp.message_handler(regexp='(^cat[s]?$|puss)')
        async def cats(message: types.Message):
            await message.reply("Cats, Cats are here 😺.")

        @self.dp.message_handler()
        async def process_messages(message: types.Message):
            print(message.text)
            await message.reply(f"You have requested an item with id <code></code>")

    async def start(self):
        await self.dp.start_polling()


async def main():
    bot = TelBot()
    await bot.set_bot_commands()

    bot.handle()


    try:
        await bot.start()
    finally:

        pass

if __name__ == '__main__':

    asyncio.run(main())
    pass
