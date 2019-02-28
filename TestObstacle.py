import unittest
from .. import obstacle

class TestStringMethods(unittest.TestCase):
	def setUp(self):
		self.p = obstacle.Obstacle(10,10)

	def test_Obstacle(self):
		self.assertEqual(self.p.x,10)
		self.assertEqual(self.p.y,10)



		#self.assertEqual(self.p.forme,1)
		#self.assertEqual(self.p.para1,10)
		#self.assertEqual(self.p.para2,20)


	'''def test_creer_carree(self):
		self.p.creer_carree(1,1)
		self.assertEqual(self.p.longueur,30)
		self.assertEqual(self.p.largeur,30)
		self.p.creer_carree(10,0)
		self.assertEqual(self.p.longueur,10)
		self.assertEqual(self.p.largeur,10)

	def test_creer_rond(self):
		self.p.creer_rond(1,1)
		self.assertEqual(self.p.rayon,10)
		self.p.creer_rond(10,0)
		self.assertEqual(self.p.rayon,10)

	def test_creer_rectangle(self):
		self.p.creer_rectangle(0,0)
		self.assertEqual(self.p.longueur,10)
		self.assertEqual(self.p.largeur,20)
		self.p.creer_rectangle(20,30)
		self.assertEqual(self.p.longueur,20)
		self.assertEqual(self.p.largeur,30)

	def test_forme(self):
		self.assertEqual(self.p.get_forme(),1)


	if __name__ == '__main__':
		unittest.main(exit=False)'''

class TestStringMethods2(unittest.TestCase):
	def setUp(self):
		self.p = a.ObstacleRectangle(10,10,5,20)


	def TestObstacleRectangle(self):
		self.assertEqual(self.p.hauteur,5)
		self.assertEqual(self.p.base,20)
		


