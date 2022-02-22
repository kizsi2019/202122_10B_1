import math

def main():
    n= 33
    i=0
    while n>math.pow(8,i):
        i+=1
    i=i+-1
    print("n: "+str(n)+" i: "+str(i))

    eredmeny=""
    while i>=0:
        if math.pow(8,i)<=n:
            x=math.floor(n/math.pow(8,i))
            eredmeny+="1"
            n=n-x*math.pow(8,i)
        else:
            eredmeny+="0"
        i=i-1
    
    print("eredmeny: "+eredmeny)