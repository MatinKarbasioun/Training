import pykka
import threading
import time


class EngineActor(pykka.ThreadingActor):

    def on_receive(self, message):
        print(threading.get_ident())

        if type(message) is str:
            self.actor_ref.tell('hi')

        elif type(message) is list:
            self.stop()

        elif type(message) is int:
            print('int')
            time.sleep(10)
            self.hello()

        elif type(message) is float:
            print('float')
            time.sleep(10)
            self.hi()

    def hi(self):
        self.actor_ref.tell(12)

    def hello(self):
        self.actor_ref.tell(12.3)


