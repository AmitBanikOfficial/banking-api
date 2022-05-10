try:
    from flask import Blueprint
    from service.register_user_service import register_user_service
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)


register_bp = Blueprint('register_bp',__name__)


@register_bp.route("/register", methods = ['POST'])
def register():
    return register_user_service()
    
