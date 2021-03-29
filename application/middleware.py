from flask import abort, redirect, flash, url_for
#from .routes import profile

class Middleware:

	@classmethod
	def authorizeSuperUser(cls, user):
		"""
		Allows Authorization to only Super Uers, aborts if not super user
		@params user: current logged in user
		"""

		if user.rank: return abort(403)

	# @classmethod
	# def authorizeGuest(cls, user):

	# 	if user.is_authenticated:
	# 		flash("acc")
	# 		return redirect(url_for('.profile'))
