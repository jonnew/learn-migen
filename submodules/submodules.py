from migen import *

class Adder(Module):
    def __init__(self, width):
        self.a = a = Signal(width)
        self.b = b = Signal(width)
        self.result = result = Signal(width + 1)

        self.comb += result.eq(a + b)

class Top(Module):
    def __init__(self):

        # 8-bit input
        self.inp = inp = Signal(8)

        # Adder instance
        adder = Adder(8)
        self.submodules += adder

        # Adder result here
        self.res = adder.result

        # update comb logic with adder
        self.comb += [
            adder.a.eq(inp),
            adder.b.eq(3)
        ]

def submod_test(dut):
    for i in range(20):
        yield dut.inp.eq(i)
        yield
        print("{} {}".format(i, (yield dut.res)))


dut = Top()
run_simulation(dut, submod_test(dut), vcd_name="adder.vcd")
