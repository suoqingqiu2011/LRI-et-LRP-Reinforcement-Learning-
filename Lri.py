import os
import sys
import math
import random
from random import randint

b=0.5	
mise=0

Amise=0
Bmise=0
Astrat=[]
Bstrat=[]
Acard=0
Bcard=0
Again=0
Bgain=0

nbg5A=0
nbg3A=0
nbg2A=0
nbg1A=0

nbg5B=0
nbg3B=0
nbg2B=0
nbg1B=0


def Esp(i):

	global nbg5A
	global nbg3A
	global nbg2A
	global nbg1A
	global nbg5B
	global nbg3B
	global nbg2B
	global nbg1B
	pA5=nbg5A/i
	pA3=nbg3A/i
	pA2=nbg2A/i
	pA1=nbg1A/i

	pB5=nbg5B/i
	pB3=nbg3B/i
	pB2=nbg2B/i
	pB1=nbg1B/i

	EA=pA5*5+pA3*3+pA2*2+pA1-pB5*5-pB3*3-pB2*2-pB1
	EB=pB5*5+pB3*3+pB2*2+pB1-pA5*5-pA3*3-pA2*2-pA1

	print "Ea:"+str(EA)
	print "Eb:"+str(EB)

def renormalizeStrat():
	global Astrat
	global Bstrat

	for i in range(0,9):
		somme=0.0
		for j in range(0,4):
			somme+=Astrat[i][j]
		for j in range(0,4):
			Astrat[i][j]=Astrat[i][j]/somme

	for i in range(0,9):
		for j in range(0,2):
			somme=0
			for k in range(0,2):
				somme+=Bstrat[i][j][k]
			
			for k in range(0,2):
				Bstrat[i][j][k]=Bstrat[i][j][k]/somme



# 0 -> A win ; 1->Bwin ; 3->draw 
# utility = mise/miseMax = mise/10
def updateStrat(winner,Achoice,Bchoice):
	global Astrat
	global Bstrat
	global b
	global mise
	global Amise
	global Bmise
	global Acard
	global Bcard
	global Again
	global Bgain
	global nbg5A
	global nbg3A
	global nbg2A
	global nbg1A
	global nbg5B
	global nbg3B
	global nbg2B
	global nbg1B

	if(Achoice!=0):

		if (winner==0):
			if(Bchoice==0):
				nbg1A+=1
			elif (Achoice==1):
				nbg2A+=2
			elif (Achoice==2):
				nbg3A+=3
			elif (Achoice==3):
				nbg5A+=5
			Again+=Bmise
			Bgain-=Bmise
			Astrat[Acard][Achoice]=Astrat[Acard][Achoice]+b*(Bmise/5.0)*(1.0-Astrat[Acard][Achoice])
			for i in range(0,4):
				if i!=Achoice:
					Astrat[Acard][i]=Astrat[Acard][i]-b*(Bmise/5.0)*Astrat[Acard][i]
		if (winner==1):

			if (Achoice==1):
				nbg2B+=2
			elif (Achoice==2):
				nbg3B+=3
			elif (Achoice==3):
				nbg5B+=5
			Bgain+=Amise
			Again-=Amise
			Bstrat[Bcard][Achoice-1][Bchoice]=Bstrat[Bcard][Achoice-1][Bchoice]+b*(Amise/5.0)*(1.0-Bstrat[Bcard][Achoice-1][Bchoice])
			for i in range(0,2):
				if (i!=Bchoice):
					Bstrat[Bcard][Achoice-1][i]=Bstrat[Bcard][Achoice-1][i]-b*(Amise/5.0)*Bstrat[Bcard][Achoice-1][i]

	else:
		Bgain+=1
		Again-=1
		nbg1B+=1
		#if (winner==3):
		#	mise=mise/2
		#	Astrat[Acard][Achoice]=Astrat[Acard][Achoice]+b*Bmise/5*(1-Astrat[Acard][Achoice])
		#	for i in range(0,4):
		#		if (i!=Achoice):
		#			Astrat[Acard][i]=Astrat[Acard][i]-b*Amise/5*Astrat[Acard][i]
			
		#	Bstrat[Bcard][Achoice-1][Bchoice]=Bstrat[Bcard][Achoice-1][Bchoice]+b*Amise/5*(1-Bstrat[Bcard][Achoice-1][Bchoice])
		#	for i in range(0,2):
		#		if (i!=Bchoice):
		#			Bstrat[Bcard][Achoice-1][i]=Bstrat[Bcard][Achoice-1][i]-b*Amise/10*Bstrat[Bcard][Achoice-1][i]

	
	#print(Astrat)
	#print(Bstrat)
	

def endTurn(Achoice,Bchoice):
	
	global Amise
	global Bmise

	global Acard
	global Bcard	
	if (Achoice==0):
		updateStrat(1,Achoice,Bchoice)


	elif (Bchoice==0):
		updateStrat(0,Achoice,Bchoice)

	elif(Acard<Bcard):
		updateStrat(1,Achoice,Bchoice)
	elif (Acard>Bcard):
		updateStrat(0,Achoice,Bchoice)
	else:
		updateStrat(3,Achoice,Bchoice)


	


def BTurn(Achoice):
	
	global Astrat
	global Bstrat
	global mise
	global Amise
	global Bmise
	global Acard
	global Bcard


	

	#print Achoice

	if (Achoice==0):
		endTurn(Achoice,-1)
	elif (Achoice==1):
		Amise+=1
	elif (Achoice==2):
		Amise+=2
	elif (Achoice==3):
		Amise+=4
	Bchoice=random.random()
	#pass
	

	if(Bstrat[Bcard][Achoice-1][0]>=Bchoice):
		endTurn(Achoice,0)
	#follow
	else:
		if(Achoice==1):
			Bmise+=1
		elif(Achoice==2):
			Bmise+=2
		elif(Achoice==3):
			Bmise+=4
		endTurn(Achoice,1)
		



def ATurn():
	global Astrat
	global Bstrat
	global b
	global mise
	global Acard
	global Bcard
	Achoice=random.random();
	tmp=0
	t=0
	for i in range(0,3):
		if((tmp+Astrat[Acard][i]>=Achoice) & (t==0)):
			t=1
			BTurn(i)
		else:
			tmp=tmp+Astrat[Acard][i]
	if(t==0):
		BTurn(3)

def startTurn():
	global mise
	global Amise
	global Bmise
	global Acard
	global Bcard
	Amise=1
	Bmise=1
	#generation des cartes
	Acard=randint(0,9)
	Bcard=randint(0,9)
	#print Acard
	#print Bcard
	ATurn()


def moy(out):
	global Astrat
	global Bstrat
	global b
	global mise
	global Acard
	global Bcard
	avB=0
	avA=0
	for i in range(0,10):
		avA+=Astrat[i][3]
		avB+=Bstrat[i][2][1]
	avA=avA/10
	avB=avB/10
	
	out.write(str(avA)+" "+str(avB)+"\n")



def main():
	global Amise
	global Bmise
	global Astrat
	global Bstrat
	global b
	global mise
	global Acard
	global Bcard
	global Again
	global Bgain
	out=open("out.data","w")
	outg=open("outg.data","w")
	for i in range(0,10):
		#init des proba des strats. 1 dimension supplementaire pour B pour reagir au choix de A et 4 strats car suivre depend de la mise de A
		Astrat.append([0.25,0.25,0.25,0.25])
		Bstrat.append([[0.5,0.5],[0.5,0.5],[0.5,0.5]])

	i=0
	for i in range(0,10000000):
		#print Astrat
		#print Bstrat
		Amise=1
		Bmise=1
		startTurn()
		moy(out)
		outg.write(str(Again)+" "+str(Bgain)+"\n")
		#out.write(str(Astrat[4][3])+" "+str(Bstrat[4][2][1])+"\n")
		#renormalizeStrat()
		
		print Astrat
		print Bstrat
	Esp(float(i))	
	out.close()
	outg.close()

main()