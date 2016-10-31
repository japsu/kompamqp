import asyncio
from pprint import pprint

import asynqp

from . import config


def process_message(received_message):
    pprint(received_message.json())


async def setup_tool(process_message=process_message):
    connection = await asynqp.connect(
        config.AMQP_HOSTNAME,
        config.AMQP_PORT,
        virtual_host=config.AMQP_VHOST,
        username=config.AMQP_USERNAME,
        password=config.AMQP_PASSWORD
    )

    channel = await connection.open_channel()

    exchange = await channel.declare_exchange('kompassi.access.smtppassword', 'fanout')
    queue = await channel.declare_queue(exclusive=True)

    await queue.bind(exchange, '')
    await queue.consume(process_message)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(setup_tool())
    loop.run_forever()
