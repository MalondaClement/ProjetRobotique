import unittest
from .. import arene
import math as m

class TestArene (unittest.TestCase):
	def setUp(self):
		t=arene.Obstacle(6,6)
		c=arene.Obstacle(-5,-6)
		b=arene.Robot(14,17,m.pi/4)
		self.p = arene.Arene(22,18)
		self.p.list_obj=t
		self.p.list_rob=b
		self.c = arene.Arene(22,18)
		self.c.list_rob=b
		self.c.list_obj=t

	def test_coord(self):
		self.assertEqual(self.p.nb_ligne,22)
		self.assertEqual(self.p.nb_colonne,18)
		self.assertEqual(self.p.list_rob,self.c.list_rob)
		self.assertEqual(self.p.list_obj,self.c.list_obj)

	'''def test_get_object(self):
		self.p.inserer_obs(p)
		self.assertEqual(self.p.get_object(6,6),1)
		self.assertEqual(self.b.get_object(14,17),2)'''

	'''def test_est_dans_matrice(self):
		self.assertTrue(self.p.est_dans_matrice(c))
		self.assertTrue(self.p.est_dans_matrice(a))'''

	#il faut ajouter la variable i dans est_vide

	'''def test_est_vide(self):
		self.c.remplir_matrice(20,1)
		self.assertFalse(self.c.est_vide(c))
		self.c.remplir_matrice(20,0)
		self.assertTrue(self.c.est_vide(c))'''

	#def test_remplir_matrice(self):

	
	#def test_calcul_angle(self):
		#self.assertEqual(self.c.calcul_angle(1))

	#def test_calcul_hypo(self):
		#self.assertEqual(self.c.calcul_angle(1))

