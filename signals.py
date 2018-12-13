""" other links

https://pypi.org/project/blinker/
https://www.mattlayman.com/blog/2015/blinker/
"""
# This example: https://pythonadventures.wordpress.com/tag/blinker/

from blinker import signal
class One:
    def __init__(self):
        self.two = Two()
        self.two.some_signal.connect(self.callback)

    def callback(self, data):  # notice the data parameter
        print('Called')
        print(data)


class Two:
    some_signal = signal('some_signal')

    def process(self):
        # Do something
        self.some_signal.send('blah!-blah!')

one = One()
one.two.process()
