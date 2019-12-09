from copy import copy
from enum import IntEnum

class Mode(IntEnum):
    POS = 0
    IMM = 1
    REL = 2


class Op(IntEnum):
    ADD = 1
    MULT = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_T = 5
    JUMP_F = 6
    LT = 7
    EQ = 8
    BASE = 9
    HALT = 99


class Intcode:
    def __init__(self, reg, inputs=[]):
        self.reg = copy(reg)
        self.reg.extend([0] * 2000)
        self.ip = 0
        self.base = 0
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

            if mp1 == Mode.IMM:
                r1 = self.ip+1
            elif mp1 == Mode.POS:
                r1 = self.reg[self.ip+1]
            else:
                r1 = self.reg[self.ip+1] + self.base

            if mp2 == Mode.IMM:
                r2 = self.ip+2
            elif mp2 == Mode.POS:
                r2 = self.reg[self.ip+2]
            else:
                r2 = self.reg[self.ip+2] + self.base

            try:
                if mp3 == Mode.IMM:
                    r3 = self.ip+3
                elif mp3 == Mode.POS:
                    r3 = self.reg[self.ip+3]
                else:
                    r3 = self.reg[self.ip+3] + self.base
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
            elif op == Op.BASE:
                self.base += self.reg[r1]
                self.ip += 2
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
