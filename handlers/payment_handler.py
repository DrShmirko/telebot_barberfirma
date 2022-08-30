from aiogram import types
from aiogram.types import ContentTypes

from handlers.base_handler import BaseHandler


class PaymentHandler(BaseHandler):

    def handle(self):

        @self.dp.message_handler(commands=['купить'])
        async def cmd_buy(message: types.Message):
            await message.bot.send_message(message.chat.id,
                                           "Real cards won't work with me, no money will be debited from your account."
                                           " Use this test card number to pay for your Time Machine: `4242 4242 4242 4242`"
                                           "\n\nThis is your demo invoice:", parse_mode='Markdown')
            await message.bot.send_invoice(message.chat.id,
                                           title='Working Time Machine',
                                           description='Want to visit your great-great-great-grandparents?'
                                                       ' Make a fortune at the races?'
                                                       'Shake hands with Hammurabi and take a stroll in the Hanging '
                                                       'Gardens? '
                                                       ' Order our Working Time Machine today!',
                                           provider_token='284685063:TEST:OWFiODQ3YzkzMjhj',
                                           currency='rub',
                                           photo_url=None,
                                           photo_size=None, photo_width=0, photo_height=0,
                                           is_flexible=False,
                                           prices=[types.LabeledPrice(label='Working time machine', amount=120000)],
                                           start_parameter='time-machine-example',
                                           payload='sdsd'
                                           )

        @self.dp.pre_checkout_query_handler(lambda q: True)
        async def checkout(pre_checkout_query: types.PreCheckoutQuery):
            await pre_checkout_query.bot.answer_pre_checkout_query(
                pre_checkout_query.id,
                ok=True,
                error_message="Aliens tried to steal your card's CVV,"
                              " but we successfully protected your credentials,"
                              " try to pay again in a few minutes, we need a small rest."
            )

        @self.dp.message_handler(content_types=ContentTypes.SUCCESSFUL_PAYMENT)
        async def got_payment(message: types.Message):
            await message.bot.send_message(message.chat.id,
                                           'Ура! Спасибо за оплату! Мы обработаем ваш заказ `{} {}`'
                                           ' в самое ближайшее время! Оставайтесь на связи.'.format(
                                               message.successful_payment.total_amount / 100,
                                               message.successful_payment.currency),
                                           parse_mode='Markdown')
