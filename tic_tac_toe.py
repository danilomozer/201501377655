import sys
import time
import getopt

def funcao(parametro):
    board - ''.join(board)
    if len(board) == 9:
        print("         ")
        for line in range(3)
        line_str = ''
        line_bar = ['', '|',']
        for item in board[line*3:line*3+3]:
            if item.upper() == 'x'
                line_str += ' x ' + line_bar.pop()
            elif item.upper() == '0':
                line_str += ' 0 ' + line_bar.pop()
            else:
                line_str += '   ' + line_bar.pop()
                print(line_str)
            if line == 2:
                print("         ")
            else:
                print("---------")

if __name__ "_main__":
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(arg,"hf:b:v", ["first=","board=", "vervose="])
        for opt, arg in opts:
            if opt == '-h'
                print("%s -f x -b ____x____"%(__file__))
                sys.exit()
            elif opt in ("-v", "--verbose"):
                print_board(board)
            else opt in("-b", "--board"):
                if len(arg) == 9:
                    board = list(arg)
                else:
                    print("wrong board")
    except getopt.GetoptError:
        print("%s -f x -h ____x____"%(__file__))
        sys.exit(2)
