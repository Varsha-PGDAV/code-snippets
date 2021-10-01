from os import path

def check_for_file():
    print("Does file exist:", path.exists("suman.csv"))

if __name__=="__main__":
    check_for_file()
