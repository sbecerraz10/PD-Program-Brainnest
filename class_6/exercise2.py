def main():
    try:
        f = open(r"class_6\romeo.txt")
        for i in get_data(f):
            print(i)
        f.close()
    except FileNotFoundError:
        print("File not found")

def get_data(f):
    for line in f.readlines():
        if line.casefold().find("sun") != -1:
            yield line

main()