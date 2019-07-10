
import random

def create_bingo_number_file(names):
    f = open("bingo_numbers.txt","w+")
    for name in names:
        f = bingo_numbers(f, name)


def bingo_numbers(f, name):
    number_array = []
    for x in range(25):
        rand_num = random.randint(1,75)
        while rand_num in number_array:
            rand_num = random.randint(1,75)
        number_array.append(rand_num)

    f.write(name + ",,,,\n")

    for idx in range(0, 25, 5):
        idx_start = idx
        idx_end = idx + 5
        vals = ",".join(list(map(lambda x: str(x), number_array[idx_start:idx_end]))) + '\n'
        f.write(vals)
        print(vals)

    return f
    # for num in number_array:
        # print(num)

create_bingo_number_file(["Jason", "Adhaar", "Astha"])
