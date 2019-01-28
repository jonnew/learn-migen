from migen import *

class Blinky(Module):
    def __init__(self):
        self.led = led = Signal()
        self.counter = counter = Signal(3)

        # LED reports MSB of counter
        self.comb += led.eq(counter[2])

        # Counter driven by implicit clock
        self.sync += counter.eq(counter + 1)

def blinky_test(dut):
    for i in range(20):
        print("{} {}".format((yield dut.counter), (yield dut.led)))
        yield

dut = Blinky()
run_simulation(dut, blinky_test(dut), vcd_name="blinky.vcd")
