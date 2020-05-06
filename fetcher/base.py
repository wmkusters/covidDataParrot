import requests as r


class PickUp:
	def __init__(self, endpnt):
		self.endpnt = endpnt
		self.response = r.get(endpnt)
		
