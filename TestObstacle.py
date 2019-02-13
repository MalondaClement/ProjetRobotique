import unittest
import unittest
#from rep import Obstacle 
class TestObstacle (unittest.TestCase):
	def test_Obstacle(self):
		self.assertEqual(Obstacle(10,10,1).x,10)
		self.assertEqual(Obstacle(10,10,1).y,10)
		self.assertEqual(Obstacle(10,10,1).forme,1)

	def test_get_position(self):
		self.assertEqual()

	def test_forme(self):
		def setUp(self):
			self.obs=Obstacle(10,10,1)
		
		def test_get_forme(self):
			self.assertEqual(self.obs.get_forme(),1)

	






