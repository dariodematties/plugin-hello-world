from waggle import plugin
from time import sleep

plugin.init()

counter = 0

while True:
    sleep(1)
    print("publishing value", counter)
    plugin.publish("hello.world.counter", counter)
    counter += 1

