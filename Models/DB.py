
import os
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor


class DB(object):
	"""Initialize mysql database using environment variables with sensible defaults.

	Environment variables used:
	- LMS_DB_HOST (default: localhost)
	- LMS_DB_PORT (default: 3306)
	- LMS_DB_USER (default: root)
	- LMS_DB_PASSWORD (default: empty)
	- LMS_DB_NAME (default: lms)
	"""

	host = os.getenv('LMS_DB_HOST', 'localhost')
	port = int(os.getenv('LMS_DB_PORT', 3306))
	user = os.getenv('LMS_DB_USER', 'root')
	password = os.getenv('LMS_DB_PASSWORD', '')
	db = os.getenv('LMS_DB_NAME', 'lms')
	table = ""

	def __init__(self, app):
		# Configure flask-mysql using values (note: keys expected by flask-mysql)
		app.config["MYSQL_DATABASE_HOST"] = self.host
		app.config["MYSQL_DATABASE_PORT"] = self.port
		app.config["MYSQL_DATABASE_USER"] = self.user
		app.config["MYSQL_DATABASE_PASSWORD"] = self.password
		app.config["MYSQL_DATABASE_DB"] = self.db

		# Initialize the MySQL extension
		self.mysql = MySQL(app, cursorclass=DictCursor)

	def cur(self):
		return self.mysql.get_db().cursor()

	def query(self, q):
		h = self.cur()

		if (len(self.table) > 0):
			q = q.replace("@table", self.table)

		h.execute(q)

		return h

	def commit(self):
		self.query("COMMIT;")