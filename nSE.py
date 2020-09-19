import  numpy as np
import matplotlib.pyplot as plt
"""
class nse:
    intensity  = np.empty(0)
    s = 1
    l1 = 2
    l2 = 3
    a = 0.00003
    lmb = 1
    n = 2
    @classmethod
    def points(cls):
        cls.points = numpy.linspace(-cls.a/2,cls.a/2,1000)
        return cls.points

    @classmethod
    def no_of_slits(cls,n):
        cls.n=n
        print('The no of slits are %i')


    @classmethod
    def slitintensity(cls):
        cls.ist=




    @classmethod
    def intensity(cls,i):
        cls.beta = np.pi*cls.a*np.sin(np.arctan(cls.points/l2))/lmb
        cls.intensity.append(cls.ist*np.sin(cls.beta)**2)
        return cls.intensity


    @classmethod
    def position(cls,):

"""

def intensity(i,a,s,l2,lmd,n,sw=0.0):
    if n==1:
        sw =0
    intensity=[]
    points=[]
    s1=np.empty(n)
    s2=np.empty(n)
    if n%2==0:
        for k in range(int(n/2)):
            s1[k]=s/2-(sw*n/2*(n/2-k))
            s2[k]=-s/2-(sw*n/2*(n/2-k))
        for k in range(int(n/2),n):
            s1[k] = s / 2 + (sw * n / 2 * (n / 2 - k))
            s2[k] = -s / 2 + (sw * n / 2 * (n / 2 - k))
    else:
        if n!=1:
            for k in range(int(n / 2)):
                s1[k] = s / 2 - (sw * n / 2 * (n / 2 - k))
                s2[k] = -s / 2 - (sw * n / 2 * (n / 2 - k))

            s1[int(n / 2)] = s / 2
            s2[int(n / 2)] = -s / 2

            for k in range(int(n / 2) + 1, n):
                s1[k] = s / 2 + (sw * n / 2 * (n / 2 - k))
                s2[k] = -s / 2 + (sw * n / 2 * (n / 2 - k))
        else:
            s1[int(n / 2)] = s / 2
            s2[int(n / 2)] = -s / 2





    for j in range(n):
        points.append(np.linspace(s1[j], s2[j] , 1000))
        print(s1[j],s2[j])
        beta = np.pi * a * np.sin(np.arctan(points[j] / l2)) / lmd
        intensity.append(i * (np.sin(beta) ** 2) / beta ** 2)

    return intensity,points
s=0.001
ist,points = intensity(1,0.003,s,10,0.00000003,2,0.0001)
plt.plot(ist[0],points[0])
plt.plot(ist[1],points[1],'r')
plt.ylim((-s/2,s/2))
plt.show()
print(points[0][0],points[0][-1])