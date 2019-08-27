magiclist = ["magic1","magic2","magic3"]

def show_magics():
    for i in range(len(magiclist)):
        print(magiclist[i])

def make_great(magiclist):
    for i in range(len(magiclist)):
        magiclist[i] = "the great "+magiclist[i]

if __name__ == '__main__':
    make_great(magiclist)
    show_magics()