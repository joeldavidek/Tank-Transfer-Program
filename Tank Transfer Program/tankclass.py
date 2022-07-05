credbg = '\33[41m'
cend = '\33[0m'
cgreenbg = '\33[42m'
cyellowbg = '\33[43m'
cgreen = '\33[32m'


class Tank:
    def __init__(self, tknum, tkheight, tkmax, tkgpf, maxgal, crtlev):  # how to create a class
        self.tknum = tknum
        self.tkheight = tkheight
        self.tkmax = tkmax
        self.tkgpf = tkgpf
        self.maxgal = maxgal
        self.crtlev = crtlev

    def info(self):
        return ("{}{}\n{}{}\n{}{}\n{}{}\n{}{}" .format(cyellowbg + "Tank Number:" + cend + " ", self.tknum, cyellowbg + "Height:" + cend + " ", self.tkheight, cyellowbg + "Max Fill:" + cend + " ", self.tkmax, cyellowbg + "GPF:" + cend + " ", self.tkgpf, cyellowbg + "Max Capacity:" + cend + " ", self.maxgal))
