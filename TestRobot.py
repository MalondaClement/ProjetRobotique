import unittest
import math as m
#from rep import Robot
class TestRobot (unittest.TestCase):
	def setUp(self):
		self.p = Robot(0,0,m.pi/2) 
		self.j = Robot(1,1,m.pi)
		self.i = Robot(1,1,-3*(m.pi/2))
		self.k = Robot(0,0,0)
	def test_coord(self):
		self.assertEqual(self.p.x,0)
		self.assertEqual(self.p.y,0)
		self.assertEqual(self.p.angle, m.pi/2)

	def test_changer_angle(self):
		self.p.changer_angle(self.j)
		self.assertEqual(self.p.angle,m.pi)
		self.p.changer_angle(self.i)
		self.assertEqual(self.p.angle,3*(m.pi/2))

	def test_avancer(self):
		self.k.avancer(self.k,5)
		self.assertEqual(self.k.x,5)
		