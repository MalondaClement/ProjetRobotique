import unittest

class TestArene (unittest.TestCase):
	def setUp(self):
		p=Obstacle(6,6,1)
		b=Robot(14,17,m.pi/4)
		self.p = Arene(22,18,[p],[b])
		
	def test_coord(self)
		self.assertEqual(self.p.nb_ligne,22)
		self.assertEqual(self.p.nb_colonne,18)
		self.assertEqual(self.p.list_rob,[b])
		self.assertEqual(self.p.list_obj,[p])

	def test_get_object(self)
		self.assertEqual(self.p.get_object(6,6),1)
		self.assertEqual(self.b.get_object(14,17),2)

		