from envparse import env

AMQP_HOSTNAME = env('AMQP_HOSTNAME', default='localhost')
AMQP_PORT = env.int('AMQP_PORT', default=5672)
AMQP_USERNAME = env('AMQP_USERNAME', default='guest')
AMQP_PASSWORD = env('AMQP_PASSWORD', default='secret')
