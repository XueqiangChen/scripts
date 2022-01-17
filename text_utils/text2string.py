import getopt
import sys


def main(argv):
    input_file = ''
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.GetoptError:
        print('text2string.py -i <input_file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('text2string.py -i <input_file>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
    print('input file is: ', input_file)
    with open(input_file) as file:
        lines = file.readlines()
    str_result = ''
    for line in lines:
        str_result += line.strip() + ','
    print('output result is: ', str_result)


if __name__ == "__main__":
    main(sys.argv[1:])