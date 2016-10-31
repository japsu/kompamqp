from envparse import env

env.read_envfile()

AMQP_HOSTNAME = env('KOMPAQ_AMQP_HOSTNAME', default='localhost')
AMQP_VHOST = env('KOMPAQ_AMQP_VHOST', default='/')
AMQP_PORT = env.int('KOMPAQ_AMQP_PORT', default=5672)
AMQP_USERNAME = env('KOMPAQ_AMQP_USERNAME', default='guest')
AMQP_PASSWORD = env('KOMPAQ_AMQP_PASSWORD', default='guest')
