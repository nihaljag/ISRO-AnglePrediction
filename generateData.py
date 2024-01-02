import math
import time
import csv
def main(initMass = 3000,m=-0.14, F = 440):
    csvfile = open("alphabetaDegrees.csv", "w",  newline='')
    cw = csv.writer(csvfile)
    cw.writerow(['Vx','Vy', 'Vz', 'alpha', 'beta'])
    dT = 1   #Time Interval = 1second
    totalTime = 1000 #in seconds
    L = int(totalTime/dT)
    Vx = [0]*L
    Vy = [0]*L
    Vz = [0]*L
    M = [initMass]*L
    for aDeg in range(-5,6, 1):
        for bDeg in range(-5, 6, 1):
            aDeg/=10
            bDeg/=10
            a = math.radians(aDeg)
            b = math.radians(bDeg)
            for k in range(L):
                if k!=0:
                    M[k] = M[k-1] + m*dT
                Vx[k]= F* math.cos(b) * math.cos(a) / M[k]
                Vy[k]= F* math.cos(b) * math.sin(a) / M[k]
                Vz[k]= F* math.sin(b) / M[k]
                cw.writerow([Vx[k], Vy[k], Vz[k], aDeg, bDeg])
    csvfile.close()
    return 

if __name__=="__main__":
    start_time = time.time()
    dat = main()
    print("--- Executed in %s seconds ---" %(time.time() - start_time))

