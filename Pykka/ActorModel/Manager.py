import pykka
import threading
from .Broker import BrokerActor


class ManagerActor(pykka.ThreadingActor):

    def on_receive(self, message):
        print(threading.get_ident())
        c = BrokerActor.start()
        c.tell('hello')
        print(c)

        if type(message) is str:
            return 'Hi there!'
