import sys

def sub(a,b):
    return a-b

if __name__ == "__main__":
    if len(sys.argv)==3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        print("USER INPUT PROVIDED")

    else:
        x = 10
        y = 5

    print("Substration: ",sub(x,y))            
