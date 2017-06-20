import numpy as np
trial= np.ones(4)
trial3= np.ones((4,5))
print"2"#2
print(trial3)
print "3"#3
trial2= np.ones(5)
trial2[1:5]=0
print(trial2)
#4
print"4"
mult=trial2*trial3
print(trial2*trial3)
#5
print "5"
mult[1,2]=10
print(mult)
#6
print "6"
trial3=trial3*2
print trial3
#7
print "7"
sum1=trial3.sum()
print(sum1)
#8
print"8"
sumr=trial3.sum(axis=1)
print(sumr)
#9
print"9"
sumc=trial3.sum(axis=0)
print(sumc)