
class Parser(object):
    def __init__(self, tokens):
        self.tokens = tokens

    def parse(self):
        index = 0
        while index < len(self.tokens):
            if self.tokens[index] == "print".upper() and self.tokens[index + 1][:6] == "string".upper():
                string = self.tokens[index + 1][9:len(self.tokens[index + 1]) - 1]
                print(string)
                index += 2
            else:
                print("ERROR: Could not find valid line of TeraBASIC code.")
                exit(0)
            