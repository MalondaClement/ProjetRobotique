import unittest

class TestArene (unittest.TestCase):
	def setUp(self):
		p=Obstacle(6,6,1)
		a=Obstacle(-5,-6,1)
		b=Robot(14,17,m.pi/4)
		self.p = Arene(22,18,[p],[b])
		self.c = Arene(22,18,0,0)

	def test_coord(self):
		self.assertEqual(self.p.nb_ligne,22)
		self.assertEqual(self.p.nb_colonne,18)
		self.assertEqual(self.p.list_rob,[b])
		self.assertEqual(self.p.list_obj,[p])

	def test_get_object(self):
		self.assertEqual(self.p.get_object(6,6),1)
		self.assertEqual(self.b.get_object(14,17),2)

	def test_est_dans_matrice(self):
		self.assertTrue(self.p.est_dans_matrice(p))
		self.assertTrue(self.p.est_dans_matrice(a))

	#il faut ajouter la variable i dans est_vide

	def test_est_vide(self):
		self.c.remplir_matrice(20,1)
		self.assertFalse(self.c.est_vide(c))
		self.c.remplir_matrice(20,0)
		self.assertTrue(self.c.est_vide(c))

	#def test_remplir_matrice(self):

	
	#def test_calcul_angle(self):
		#self.assertEqual(self.c.calcul_angle(1))

	#def test_calcul_hypo(self):
		#self.assertEqual(self.c.calcul_angle(1))
