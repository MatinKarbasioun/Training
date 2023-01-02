import pykka
import threading


class BrokerActor(pykka.ThreadingActor):

    def on_receive(self, message):
        print(threading.get_ident())
        while True:
            print('hi')
