from copy import copy
from enum import IntEnum

class Mode(IntEnum):
    POS = 0
    IMM = 1


class Op(IntEnum):
    ADD = 1
    MULT = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_T = 5
    JUMP_F = 6
    LT = 7
    EQ = 8
    HALT = 99


class Intcode:
    def __init__(self, reg, inputs=[]):
        self.reg = copy(reg)
        self.ip = 0
        self.done = False

        self.inputs = inputs

        self.mode = Mode.POS
        self.value = None

    def run(self, until_output=False, display=False):
        while True:
            ins = self.reg[self.ip]
            mp1, mp2, mp3 = (int(ins / v) % 10 for v in (100, 1000, 10000))
            op = ins % 100

            if op == Op.HALT:
                self.done = True
                break
            r1 = self.ip+1 if mp1 == Mode.IMM else self.reg[self.ip+1]
            r2 = self.ip+2 if mp2 == Mode.IMM else self.reg[self.ip+2]
            try:
                r3 = self.ip+3 if mp3 == Mode.IMM else self.reg[self.ip+3]
            except IndexError:
                pass # if this happens, you don't need it
            if op == Op.ADD:
                self.reg[r3] = self.reg[r1] + self.reg[r2]
                self.ip += 4
            elif op == Op.MULT:
                self.reg[r3] = self.reg[r1] * self.reg[r2]
                self.ip += 4
            elif op == Op.INPUT:
                self.reg[r1] = self.inputs.pop(0)
                self.ip += 2
            elif op == Op.OUTPUT:
                self.value = self.reg[r1]
                self.ip += 2
                if display:
                    if self.reg[self.ip] % 100 == Op.HALT:
                        line = f'Diagnostic code: {self.value}'
                    else:
                        line = f'Test: {self.value}{" - FAILED " if self.value != 0 else ""}'
                    print(line)
                if until_output:
                    break
            elif op == Op.JUMP_T:
                if self.reg[r1]:
                    self.ip = self.reg[r2]
                else:
                    self.ip += 3
            elif op == Op.JUMP_F:
                if self.reg[r1] == 0:
                    self.ip = self.reg[r2]
                else:
                    self.ip += 3
            elif op == Op.LT:
                self.reg[r3] = 1 if self.reg[r1] < self.reg[r2] else 0
                self.ip += 4
            elif op == Op.EQ:
                self.reg[r3] = 1 if self.reg[r1] == self.reg[r2] else 0
                self.ip += 4
            else:
                print(f'Bad opcode: {op} - EXITING')
                break
        return self.value

    def run_until_output(self):
        return self.run(until_output=True)

    def run_with_output(self):
        return self.run(display=True)

    def run_with_nv(self, noun, verb):
        self.reg[1] = noun
        self.reg[2] = verb
        self.run()
        return self.reg[0]
