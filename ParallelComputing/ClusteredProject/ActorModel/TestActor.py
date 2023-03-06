import pykka
import ray
from ray.actor import ActorHandle


@ray.remote
class TestActor(pykka.ThreadingActor):
    def __int__(self, arg1, arg2):
        print(arg1)
        print(arg2)


if __name__ == "__main__":
    ray.init(address="127.0.0.1:8000", namespace="colors")
    MyActorClass = ray.actor.ActorClass(TestActor)
    ray.experimental.add_actor(MyActorClass, "my_actor_id")

    # Create an instance of your actor
    actor = ray.get_actor("my_actor_id").remote('test 1', 'test 2')
    print(actor)
