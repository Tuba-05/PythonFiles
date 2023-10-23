def save_data(data, filename: str):
    with open(filename, "a+") as f:
        for packet in data:
            f.write(",".join(str(item) for item in packet) + "\n")


def read_data(filename: str):
    data = []
    with open(filename, "r") as f:
        for lst in f:
            sub_list = lst.strip().split(",")
            sub_list = [item for item in sub_list]
            data.append(sub_list)
    return data


def entry(bleh_list):
    x = input("Enter user's name: ")
    y = input('Enter id:')
    z = input('Enter account no.:')
    for lst in bleh_list:
        if lst[2] == x and lst[0] == y and lst[1] == z:
            print(lst)
            break
    else:
        print("Nah")

f = open('CurrentAccountRecords.txt', 'r+')
list = [f]
save_data(list, "CurrentAccountRecords.txt")
bleh_list = read_data("CurrentAccountRecords.txt")
entry(bleh_list)