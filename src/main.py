from sys import *
from lexer_mod.lexer import Lexer
from parser_mod.parser import Parser

def open_file(file_name):
    gotten_file = open(file_name, "r")
    file_data = gotten_file.read()
    return file_data

def main():
    first_cmd_argument = argv[1]
    file_data = open_file(first_cmd_argument)
    program_lexer = Lexer(file_data)
    tokens = program_lexer.lex()
    program_parser = Parser(tokens)
    program_parser.parse()

if __name__ == '__main__':
    main()
