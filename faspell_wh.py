from faspell import SpellChecker


class Faspell(object):
    def __init__(self):
        self.spellchecker = SpellChecker()

    def __call__(self, sentence):
        result = self.spellchecker.make_corrections([sentence])
        return result[0]


if __name__ == '__main__':
    f = Faspell()
    print(f('我非常需要你的陪办'))
    print(f('包括材质的一些碰栓啊'))
    print(f('填写工师'))
    print(f('永户所有的种端设备及终端特权必须妥善保管'))
