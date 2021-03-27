from flask import redirect, url_for,  flash
from flask_admin import expose, AdminIndexView
from flask_login import current_user

from .middleware import Middleware

class AdminPanel(AdminIndexView):

	@expose('/')
	def index(self):
		if current_user.is_authenticated:

			#Checking Authorization
			Middleware.authorizeSuperUser(current_user)
			
			#return super(CustomAdminIndexView, self).index()
			return self.render('admin.html')		

		flash("You must be logged in to access that page", 'danger')			
		return redirect(url_for('login'))




