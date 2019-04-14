from MinGen import *


input_file_name = 'input.txt'
output_file_name = 'output.txt'


def main():
    with open(input_file_name, 'r') as f:
        signs_count = int(f.readline())
        objects_count = int(f.readline())
        data = []
        for i in range(objects_count):
            data.append(list(map(int, f.readline().split())))

    mg = MinGen(signs_count, objects_count, data)
    mg.print_data()
    mg.print_prom_tab()


if __name__ == '__main__':
    main()
