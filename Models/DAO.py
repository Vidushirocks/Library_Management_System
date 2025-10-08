class DAO():
	def __init__(self, app):
		# Import DBDAO here to avoid import-time circular dependencies
		from Models.DBDAO import DBDAO
		self.db = DBDAO(app)