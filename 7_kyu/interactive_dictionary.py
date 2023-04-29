class Dictionary:
    def __init__(self):
        self.my_dict = {}

    def newentry(self, word, definition):
        self.word = word
        self.definition = definition
        self.my_dict[self.word] = self.definition

    def look(self, key):
        self.key = key
        if self.key in self.my_dict:
            return self.my_dict[self.key]
        else:
            return f"Can't find entry for {self.key}"

d = Dictionary()
d.newentry('Apple', 'A fruit that grows on trees')
print(d.look('Apple'))
print(d.look('Banana'))