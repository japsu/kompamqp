import asyncio
import asynqp

from . import config


async def main():
    connection = await asynqp.connect(
        config.AMQP_HOSTNAME,
        config.AMQP_PORT,
        username=config.AMQP_USERNAME,
        password=config.AMQP_PASSWORD
    )

    channel = await connection.open_channel()

    exchange = await channel.declare_exchange('kompassi.access.smtppassword', 'fanout')
    queue = await channel.declare_queue(exclusive=True)

    await queue.bind(exchange, '')

    while True:
        received_message = await queue.get()
        print(received_message.json())
        received_message.ack()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
