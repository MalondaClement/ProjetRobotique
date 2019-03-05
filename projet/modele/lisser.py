class Lisser:
	def __init__(self, controler,):
		self.size=5
		self.controler=controler
		self.hist=[0]*5
		self.cpt=0
	def __getattr__(self,name):
		self.hist[self.cpt]=self.controler.get_distance()
		self.cpt=(self.cpt+1)%(self.hist)
		return getattr(self.controler, name)
	def get_distance(self):
		return sum(self.hist) /len(self.hist)
