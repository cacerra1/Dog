# init for app/main/__init__.py

from flask import Blueprint

main = Blueprint('main', __name__, template_folder='templates')


from app.dogs import routes  #cross refernecing when two files depend on each others
# to correct import routes at the bottom instead of the top