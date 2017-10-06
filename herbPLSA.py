import math
import random
import herbPLSA_GV as gv
import time
import os

def init():
	nD = gv.nSyndrome
	nH = gv.nHerb
	nS = gv.nSymptom
	nP = gv.nPatient
	
	norm = .0
	for i in range(nD):
		gv.p_D[i]=random.random()
		norm += gv.p_D[i]
	for i in range(nD):
		gv.p_D[i] /= norm
		
	for z in range(nD):
		norm = .0
		for h in range(nH):
			gv.p_H_D[h][z] = random.random()
			norm += gv.p_H_D[h][z]
		for h in range(nH):
			gv.p_H_D[h][z] /= norm

	for z in range(nD):
		norm = .0
		for s in range(nS):
			gv.p_S_D[s][z] = random.random()
			norm += gv.p_S_D[s][z]
		for s in range(nS):
			gv.p_S_D[s][z] /= norm

	for z in range(nD):
		norm = .0
		for p in range(nP):
			gv.p_P_D[p][z] = random.random()
			norm += gv.p_P_D[p][z]
		for p in range(nP):
			gv.p_P_D[p][z] /= norm
	
	for p in range(nP):
		if p not in gv.p_P_S_H_D:
			gv.p_P_S_H_D[p] = {}
		for s in gv.transection_PSH[p]:
			if s not in gv.p_P_S_H_D[p]:
				gv.p_P_S_H_D[p][s] = {}
			for h in gv.transection_PSH[p][s]:
				if h not in gv.p_P_S_H_D[p][s]:
					gv.p_P_S_H_D[p][s][h] = {}
				norm = 0.
				for d in range(nD):
					gv.p_P_S_H_D[p][s][h][d] = random.random()
					norm += gv.p_P_S_H_D[p][s][h][d] 
				for d in range(nD):
					gv.p_P_S_H_D[p][s][h][d] /= norm		  
				
	print "init finished",time.strftime("%Y-%m-%d %X", time.localtime())

def likelihood():
	nD = gv.nSyndrome
	nH = gv.nHerb
	nS = gv.nSymptom
	nP = gv.nPatient
	
	like = .0
	for p in range(nP):
		for s in gv.transection_PSH[p]:
			for h in gv.transection_PSH[p][s]:	
				norm = 0.
				for d in range(nD):
					norm += get_PHSD(p,h,s,d)
				like += math.log(norm,math.e)
	return like		

def m_step():
	nD = gv.nSyndrome
	nH = gv.nHerb
	nS = gv.nSymptom
	nP = gv.nPatient

	#update gv.p_D
	norm = 0.
	for d in range(nD):
		gv.p_D[d] = 0.
		for p in range(nP):
			for s in gv.transection_PSH[p]:
				for h in gv.transection_PSH[p][s]:				
					gv.p_D[d] += gv.p_P_S_H_D[p][s][h][d]
		norm += gv.p_D[d]
	for d in range(nD):
		gv.p_D[d]/=norm

	print "P(D) finished",time.strftime("%Y-%m-%d %X", time.localtime())

	#update p_H_D
	for d in range(nD):
		norm = 0.
		for h in range(nH):
			gv.p_H_D[h][d]=0.
			for p in range(nP):
				for s in gv.transection_PSH[p]:	
					if h not in gv.transection_PSH[p][s]:
						continue
					gv.p_H_D[h][d] += gv.p_P_S_H_D[p][s][h][d]
			norm += gv.p_H_D[h][d] 
		for h in range(nH):
			gv.p_H_D[h][d] /= norm  
			
	print "p_H_D finished",time.strftime("%Y-%m-%d %X", time.localtime())
	
	#update p_S_D
	for d in range(nD):
		norm = 0.
		for s in range(nS):
			gv.p_S_D[s][d]=0.
			for p in range(nP):
				if s not in gv.transection_PSH[p]:
					continue
				for h in gv.transection_PSH[p][s]:
					gv.p_S_D[s][d] += gv.p_P_S_H_D[p][s][h][d]
			norm += gv.p_S_D[s][d] 
		for s in range(nS):
			gv.p_S_D[s][d] /= norm  
			
	print "p_S_D finished",time.strftime("%Y-%m-%d %X", time.localtime())

	#update p_P_D
	for d in range(nD):
		norm = 0.
		for p in range(nP):
			gv.p_P_D[p][d]=0.
			for s in gv.transection_PSH[p]:
				for h in gv.transection_PSH[p][s]:
					gv.p_P_D[p][d] += gv.p_P_S_H_D[p][s][h][d]
			norm += gv.p_P_D[p][d]
		for p in range(nP):
			gv.p_P_D[p][d] /= norm  
			
	print "p_P_D finished",time.strftime("%Y-%m-%d %X", time.localtime())
					   
def e_step():
	
	nD = gv.nSyndrome
	nH = gv.nHerb
	nS = gv.nSymptom
	nP = gv.nPatient

	for p in range(nP):
		for s in gv.transection_PSH[p]:
			for h in gv.transection_PSH[p][s]:
				norm = 0.
				for d in range(nD):
					norm += get_PHSD(p,h,s,d)
				for d in range(nD):
					gv.p_P_S_H_D[p][s][h][d] = get_PHSD(p,h,s,d) / norm
   
	print "P(Wl,Z|D,Wh) finished",time.strftime("%Y-%m-%d %X", time.localtime())   
	
def em():
	init()
	for i in range(gv.itera):
		e_step()	
		#like = likelihood()
		m_step()			
		output_data(i)
		like = likelihood()
		print "iter:",i,"likelihood=",like,time.strftime("%Y-%m-%d %X", time.localtime())

def input_data():
	print "start read word dict"
	
	fin = open("..\..\data\HIS_tuple.txt","r")
	tN=0
	for line in fin:
		gv.transection_PSH[tN] = {}
		w = line.strip().split('\t')
		if len(w)<2:
			continue
		sl = w[0].split(':')
		hl = w[1].split(':')
		for s in sl:
			if len(s)==0:
				continue
			sid = int(s)
			if sid > 3000:
				continue
			if sid > gv.nSymptom:
				gv.nSymptom = sid
			gv.transection_PSH[tN][sid] = set()
			for h in hl:
				if len(h)==0:
					continue
				hid = int(h)
				if hid > gv.nHerb:
					gv.nHerb = hid
				gv.transection_PSH[tN][sid].add(hid)
		tN += 1
	fin.close()
	gv.nHerb += 1
	gv.nSymptom += 1
	gv.nPatient = tN
	fin = open("..\..\data\clean_data\sym_dct.txt","r")
	for line in fin:
		w = line.strip().split('\t')
		id = int(w[1])
		gv.symptomDict[id] = w[0]
	fin.close()
	fin = open("..\..\data\clean_data\herb_dct.txt","r")
	for line in fin:
		w = line.strip().split('\t')
		id = int(w[1])
		gv.herbDict[id] = w[0]
	fin.close()
	print "#Herbs",gv.nHerb
	print "#Symptoms",gv.nSymptom
	print "#Syndroms",gv.nSyndrome
	print "#Patients",gv.nPatient

	print " finished read"
   


def get_PHSD(p,h,s,d):
	ans = gv.p_D[d]*gv.p_H_D[h][d]*gv.p_S_D[s][d]*gv.p_P_D[p][d]
	if ans == 0.:
		print p,h,s,d
		print gv.p_D[d],gv.p_H_D[h][d],gv.p_S_D[s][d],gv.p_P_D[p][d]
	return ans

def output_data(citera):
	root = "..\..\\output\\result\\"
	if not os.path.isdir(root):
		os.mkdir(root)
	nD = gv.nSyndrome
	nH = gv.nHerb
	nS = gv.nSymptom
	nP = gv.nPatient
	nwords = nH
	indicesl = range(nH)
	fout=open(root+str(nD)+'_herb.topic'+str(citera),'w')
	for z in range(nD):
		indicesl.sort(lambda x,y: -cmp(gv.p_H_D[x][z], gv.p_H_D[y][z]))
		for j in range(nwords):
			if indicesl[j] == 0:
				break
			fout.write(str(gv.herbDict[indicesl[j]])+':'+str(gv.p_H_D[indicesl[j]][z])+'\t')			
		fout.write('\n')
	fout.close()
	
	nwords = nS
	indicesl = range(nS)
	fout=open(root+str(nD)+'_symptom.topic'+str(citera),'w')
	for z in range(nD):
		indicesl.sort(lambda x,y: -cmp(gv.p_S_D[x][z], gv.p_S_D[y][z]))
		for j in range(nwords):
			if indicesl[j] == 0:
				break
			fout.write(str(gv.symptomDict[indicesl[j]])+':'+str(gv.p_S_D[indicesl[j]][z])+'\t')
		fout.write('\n')
	fout.close()
	
	nwords = nH
	indicesl = range(nH)
	norm_herb={}
	for i in range(nH):
		for z in range(nD):
			norm_herb[i] = norm_herb.get(i,0) + gv.p_H_D[i][z]/nD		
			
	fout=open(root+str(nD)+'_norm_herb.topic'+str(citera),'w')
	for z in range(nD):
		indicesl.sort(lambda x,y: -cmp(gv.p_H_D[x][z]-norm_herb[x], gv.p_H_D[y][z]-norm_herb[y]))
		for j in range(nwords):
			if indicesl[j] == 0:
				break
			fout.write(str(gv.herbDict[indicesl[j]])+':'+str(gv.p_H_D[indicesl[j]][z]-norm_herb[indicesl[j]])+'\t')
		fout.write('\n')
	fout.close()

	nwords = nS
	indicesl = range(nS)
	norm_symptom={}
	for i in range(nS):
		for z in range(nD):
			norm_symptom[i] = norm_symptom.get(i,0) + gv.p_S_D[i][z]/nD		
	fout=open(root+str(nD)+'_norm_symptom.topic'+str(citera),'w')
	for z in range(nD):
		indicesl.sort(lambda x,y: -cmp(gv.p_S_D[x][z]-norm_symptom[x], gv.p_S_D[y][z]-norm_symptom[y]))
		for j in range(nwords):
			if indicesl[j] == 0:
				break
			fout.write(str(gv.symptomDict[indicesl[j]])+':'+str(gv.p_S_D[indicesl[j]][z]-norm_symptom[indicesl[j]])+'\t')
		fout.write('\n')
	fout.close()


if __name__ == '__main__':
	input_data()
	em()
