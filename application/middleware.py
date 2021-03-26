from flask import abort

class Middleware:

	@classmethod
	def authorize(cls, user):
		"""
		Allows Authorization to only Super Uers, aborts if not super user
		@params user: current logged in user
		"""

		if user.rank:
			return abort(403)