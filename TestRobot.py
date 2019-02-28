import unittest
from .. import robot
import math as m

class TestRobot (unittest.TestCase):
	def setUp(self):
		self.p = robot.Robot(0,0,m.pi/2)
		self.j = robot.Robot(1,1,m.pi)
		self.i = robot.Robot(1,1,-3*(m.pi/2))
		self.k = robot.Robot(0,0,m.pi/2)

	def tearDown(self):
		print('Nettoyage !')

	def test_coord(self):
		self.assertEqual(self.p.x,0)
		self.assertEqual(self.p.y,0)
		self.assertEqual(self.p.angle, m.pi/2)
		self.assertEqual(self.p.largeur,20)
		self.assertEqual(self.p.longueur,50)

	def test_changer_angle(self):
		self.p.changer_angle(self.j.angle)
		self.assertEqual(self.p.angle,3*(m.pi/2))
		self.k.changer_angle(self.i.angle)
		self.assertEqual(self.k.angle,m.pi)

	'''def test_avancer(self):
		self.k.avancer(self.k,5)
		self.assertEqual(self.k.x,5)'''

	#def test_calcul_angle(self):
	#	self.assertEqual(self.j.calcul_angle(),0.380506377)

	def test_calcul_hypo(self):
		self.assertEqual(self.p.calcul_hypo(),26.92582403567252)

	def test_get_position(self):
		self.assertEqual(self.j.get_position(),(1,1))
