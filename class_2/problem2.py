def main():
    list = []
    while True:
        message = "Enter a number: "
        response = input(message)
        if response != "done":
            try:
                number = int(response)
                list.append(number)
            except ValueError: print("Invalid input")
        else:
            print(f"Sum: {sum(list)}, Count: {len(list)}, Average: {sum(list)/len(list)}")
            break

if __name__ == "__main__":
    main()