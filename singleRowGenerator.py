import csv, math

def main(aDeg, bDeg, T):
    F = 440
    initMass = 3000
    m=-0.14
    M = initMass +m*T
    a = math.radians(aDeg)
    b = math.radians(bDeg)

    Vx= F* math.cos(b) * math.cos(a) / M
    Vy= F* math.cos(b) * math.sin(a) / M
    Vz= F* math.sin(b) / M
    print([Vx, Vy, Vz, aDeg, bDeg])
    return 

if __name__=="__main__":
    main(0.46345, -0.23, 786)