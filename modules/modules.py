from migen import *

class module(Module):
    def __init__(self):
        led1 = Signal()
        led2 = Signal()
        button = Signal()

        # Comb table (driven by button whenever)
        self.comb += led1.eq(button)

        # Sync table (driven by implicit clock)
        self.sync += led2.eq(~led2)

