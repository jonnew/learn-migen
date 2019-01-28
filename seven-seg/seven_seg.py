from migen import *
# val is 7 bit number
def display_seven(val):
    line0 = ["   ", " _ "]

    # NB: "  |" is LSB (b, c)
    # NB: " _ " (g, d) 
    # NB: "|  " is MSB (e, f)
    line1 = ["   ", "  |", " _ ", " _|", "|  ", "| |", "|_ ","|_|"]

    # Get LSB for top row
    a = val & 1
    
    # Shift to the letter of the bit on the display for second line
    fgb = ((val >> 1) & 1) | ((val >> 5) & 2) | ((val >> 3) & 4)

    # last line
    edc = ((val >> 2) & 1) | ((val >> 2) & 2) | ((val >> 2) & 4)

    print(line0[a])
    print(line1[fgb])
    print(line1[edc])
   
def test_display():
    val = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f, 0x77,
           0x7c, 0x39, 0x5e, 0x79, 0x71]
    for v in val:
        display_seven(v)
    #for i in range(128):
    #    print(i)
    #    print("---------")
    #    display_seven(i)

class SevenSeg(Module):
    def __init__(self):

        # Output control
        self.abcdefg = abcdefg = Signal(7)

        # Input hex
        self.hexa = hexa = Signal(4)

        # Lookup
        table = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f,
               0x77, 0x7c, 0x39, 0x5e, 0x79, 0x71]

        # Case table for each hex value
        cases = {}
        for i in range(16):
            cases[i] = abcdefg.eq(table[i])

        # Use hexa on the cases case table
        self.comb += Case(hexa, cases)

def tb_SevenSeg(dut):
    for i in range(16):
        yield dut.hexa.eq(i)
        yield display_seven((yield dut.abcdefg))


dut = SevenSeg()
run_simulation(dut, tb_SevenSeg(dut))
