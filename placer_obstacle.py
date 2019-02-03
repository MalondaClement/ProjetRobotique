def placer_obstacle(self,x,y,int forme):   #PROVISOIRE A MODIFIER
	if x<LONGUEUR and y<LARGEUR:
		if Mat_Arene[x]!=1 and Mat_Arene[y]!=1: #selon le nom de la matrice de la classe Arène
			if forme=1:
				Obstacle._init_(self,x,y,1)
			elif forme=2:
				Obstacle._init_(self,x,y,2)
			elif forme=3:
				Obstacle._init_(self,x,y,3)
				




#test placer obstacle
placer_obstacle(5,5,1);
placer_obstacle(499,450,1);
placer_obstacle(45,45,2);
placer_obstacle(89,89,3);
placer_obstacle(46,46,1);
