import os

def main():
    try:
        f = open(r"C:\Users\USER\Documents\Python Developer Brainnest Course\class_3\mbox-short.txt")
        get_mail(f)
        f.close()
    except FileNotFoundError:
        print("File not found")

def get_mail(f):
    emails = []
    n = 0
    for line in f.readlines():
        if line.startswith('From '):
            email = line.split()
            emails.append(email[1])
            print('Sender: ' + email[1])
            n+=1
    
    print(f"Count: {n}")

    frequency(emails)


def frequency(emails):
    freq = {}
    for line in emails:
        if line not in freq.keys():
            freq[line] = 1
        else:
            freq[line] = freq[line] + 1
    print(freq)
    most_frequent_sender = max(freq, key=freq.get)
    print('The most frequent sender is ' + most_frequent_sender)

def third_exercise():   
    d = dict()                      
    fname = 'mbox-short.txt'
    fhand = open(fname)
    for line in fhand:
        words = line.split()
        if len(words) < 3 or words[0] != 'From': continue
        else:
            line = words[1]
            words = line.split("@")[1]
            d[words] = d.get(words, 0) + 1    
    print(d)



if __name__ == "__main__":
    main()