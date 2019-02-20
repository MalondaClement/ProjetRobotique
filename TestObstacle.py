import unittest

#from rep import Obstacle 
class TestObstacle (unittest.TestCase):
	def test_Obstacle(self):
		self.assertEqual(Obstacle(10,10,1,10,20).x,10)
		self.assertEqual(Obstacle(10,10,1,10,20).y,10)
		self.assertEqual(Obstacle(10,10,1,10,20).forme,1)
		self.assertEqual(Obstacle(10,10,1,10,20).para1,10)
		self.assertEqual(Obstacle(10,10,1,10,20).para2,20)

	def test_creer_carree(self):
			self.creer_carree(1,1)
			self.assertEqual(self.longueur,30)
			self.assertEqual(self.largeur,30)
			self.creer_carree(10,0)
			self.assertEqual(self.longueur,10)
			self.assertEqual(self.largeur,10)

	def test_creer_rond(self):
			self.creer_rond(1,1)
			self.assertEqual(self.rayon,10)
			self.creer_rond(10,0)
			self.assertEqual(self.rayon,10)

	def test_creer_triangle(self):
			self.creer_triangle(0,0)
			self.assertEqual(self.base,10)
			self.assertEqual(self.hauteur,10)
			self.creer_triangle(20,30)
			self.assertEqual(self.base,20)
			self.assertEqual(self.hauteur,30)

	def test_creer_rectangle(self):
			self.creer_rectangle(0,0)
			self.assertEqual(self.longueur,10)
			self.assertEqual(self.largeur,20)
			self.creer_rectangle(20,30)
			self.assertEqual(self.longueur,20)
			self.assertEqual(self.largeur,30)			
			
	def test_get_position(self):
		self.assertEqual(Obstacle(10,10,1,10,20).x,(10,10))


	def test_forme(self):
		def setUp(self):
			self.obs=Obstacle(10,10,1,10,20)
		
		def test_get_forme(self):
			self.assertEqual(self.obs.get_forme(),1)

	






