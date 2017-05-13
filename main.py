#import des bibliotheques

#variables globales 
	x,y,z

#définition des caractéristiques du drone
	#nombre de moteurs
		nb_moteurs = 3
	#centre de gravité
		cg = x, y, z
	#instantation du nombre d'ailes requis
		Aile1= Aile(x, y, coeff, puissance, angle)
		Aile2= Aile(x, y, coeff, puissance, angle)
		Aile3= Aile(x, y, coeff, puissance, angle)


#séquence de calibration
	#test vol stationnaire et calibration


############ PROGRAMME PRINCIPAL #############

#Déterminer x, y, z
	#dialogue avec gyroscope pour obtenir le vecteur G

#Déterminer si commande pilote
	#script de commande
	#détermine vecteur D si déplacement ordonné
	#détermine vecteur R si rotation ordonnée

#calcul des équations de vol
	#boucle for (nombre de moteurs)
		#calcul de l'équation vectorielle
		aile.maj_puissance
		aile.maj_angle
