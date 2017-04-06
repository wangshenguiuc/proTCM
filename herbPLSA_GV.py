#####parameter######
itera = 100
nHerb = 0
nSyndrome = 100
nSymptom = 0
nPatient = 0


#####parameter######
MAXSYNDROMNUM = 130
MAXHERBNUM = 700
MAXSYMPTOMNUM = 5000
MAXPATIENTNUM = 11000

transection_PSH = {}

p_P_S_H_D = {}
    
p_D=[0.]*MAXSYNDROMNUM

p_H_D=[0.]*MAXHERBNUM
p_S_D=[0.]*MAXSYMPTOMNUM
p_P_D=[0.]*MAXPATIENTNUM

for i in range(MAXHERBNUM):
    p_H_D[i]=[0.]*MAXSYNDROMNUM
	
for i in range(MAXSYMPTOMNUM):
    p_S_D[i]=[0.]*MAXSYNDROMNUM
	
for i in range(MAXPATIENTNUM):
    p_P_D[i]=[0.]*MAXSYNDROMNUM
	
herbDict = {}
symptomDict = {}