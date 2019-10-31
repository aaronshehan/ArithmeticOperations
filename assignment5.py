# Aaron Shehan
# ats0109


class Expr:
    pass


class True_(Expr):
    def __init__(self):
        self.x = 1

    def ev(self):
        return self.x


class False_(Expr):
    def __init__(self):
        self.x = 0

    def ev(self):
        return self.x


class Not(Expr):
    def __init__(self, x):
        self.x = x

    def ev(self):
        return 1-self.x.ev()


class Or(Expr):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def ev(self):
        return max(self.x.ev(), self.y.ev())


class And(Expr):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def ev(self):
        return min(self.x.ev(), self.y.ev())

# any number
class Number(Expr):
    def __init__(self, x):
        self.x = x

    def ev(self):
        return self.x

# addition
class Plus(Expr):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def ev(self):
        return self.x.ev() + self.y.ev()

# subtraction
class Sub(Expr):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def ev(self):
        return self.x.ev() - self.y.ev()

# multiplication
class Mul(Expr):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def ev(self):
        return self.x.ev() * self.y.ev()

# exponent
class Exp(Expr):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def ev(self):
        return self.x.ev() ** self.y.ev()


def t1():
    return And(Or(False_(), True_()), True_()).ev()


def t2():
    return Or(True_(), Or(False_(), False_())).ev()


def t3():
    return And(Not(True_()), True_()).ev()


def t4():
    # (((4 + 3) - 1) * 5) ^ 2
    print("(((4 + 3) - 1) * 5) ** 2 =", end = ' ')
    print(Exp(Mul(Sub(Plus(Number(4), Number(3)), Number(1)), Number(5)), Number(2)).ev())

    # (4 * (6 + 9)) - ( 2 ^ 3)
    print("(4 * (6 + 9)) - ( 2 ** 3) =", end = ' ')
    print(Sub(Mul(Number(4), Plus(Number(6), Number(9))), Exp(Number(2), Number(3))).ev())

    # (7 * (10 - 2)) + (3 ** 5)
    print("(7 * (10 - 2)) + (3 ** 5) =", end = ' ')
    print(Plus(Mul(Number(7), Sub(Number(10), Number(2))), Exp(Number(3), Number(5))).ev())

    # (((8 - 1) + 4) ^ 2) * 11
    print("(((8 - 1) + 4) ** 2) * 11 =", end=' ')
    print(Mul(Exp(Plus(Sub(Number(8), Number(1)), Number(4)), Number(2)), Number(11)).ev())

    # (4 * (-3 + 23)) ** (14 - 12)
    print("(4 * (-3 + 23)) ** (14 - 12) =", end = ' ')
    print(Exp(Mul(Number(4), Plus(Number(-3), Number(23))), Sub(Number(14), Number(12))).ev())

    # (2 ** (4 * 6)) - (3 + 15)
    print("(2 ** (4 * 6)) - (3 + 15) =", end=' ')
    print(Sub(Exp(Number(2), Mul(Number(4), Number(6))), Plus(Number(3), Number(15))).ev())

    # (41 - ((45 * 17) ** 4) + 303
    print("(41 - ((45 * 17) ** 4) + 303 =", end = ' ')
    print(Plus(Sub(Number(41), Exp(Mul(Number(45), Number(17)), Number(4))), Number(303)).ev())

    # (-83 * ((-9 ** 3) + 33) - -11
    print("(-83 * ((-9 ** 3) + 33) - -11 =", end =' ')
    print(Sub(Mul(Number(-83), Plus(Exp(Number(-9), Number(3)), Number(33))), Number(-11)).ev())

    # (987 + (-10 ** (34 - 31))) * 54
    print("(987 + (-10 ** (34 - 31))) * 54 =", end = ' ')
    print(Mul(Plus(Number(987), Exp(Number(-10), Sub(Number(34), Number(31)))), Number(54)).ev())

    # (2 ** (98 - (23 * 4))) + 933
    print("(2 ** (98 - (23 * 4))) + 933 =", end=' ')
    print(Plus(Exp(Number(2), Sub(Number(98), Mul(Number(23), Number(4)))), Number(933)).ev())


t4()







