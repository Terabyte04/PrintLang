
class Lexer(object):
    def __init__(self, data):
        self.data = data
        self.tokens = []

    def lex(self):
        self.data = list(self.data)
        acc = ""
        state = 0
        string = ""
        for char in self.data:
            acc += char
            if acc == "\n":
                acc = ""
            elif acc == " ":
                if state == 0:
                    acc = ""
                else:
                    acc = " "
            elif acc == "print".upper():
                self.tokens.append("PRINT")
                acc = ""
            elif acc == "\"":
                if state == 0:
                    state = 1
                elif state == 1:
                    self.tokens.append("STRING: " + string + "\"")
                    state = 0
                    acc = ""
                    string = ""
            elif state == 1:
                string += acc
                acc = ""
        return self.tokens