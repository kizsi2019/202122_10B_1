import math

def main():
    n= 23
    i=0
    while n>math.pow(2,i):
        i+=1
    i=i+-1
    print("n: "+str(n)+" i: "+str(i))

    eredmeny=""
    while i>=0:
        if math.pow(2,i)<=n:
            eredmeny+="1"
            n=n-math.pow(2,i)
        else:
            eredmeny+="0"
        i=i-1

    print("eredmeny: "+eredmeny)

if __name__ 