try:
    from flask import Blueprint
    from service.login_user_service import login_user_service
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)


login_bp = Blueprint('login_bp',__name__)


@login_bp.route("/login", methods = ['POST'])
def login():
    return login_user_service()
    
