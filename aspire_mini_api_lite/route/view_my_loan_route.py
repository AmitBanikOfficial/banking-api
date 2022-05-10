try:
    from flask import Blueprint
    from service.view_my_loan_service import view_my_loan
    from flask_jwt_extended import jwt_required
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)


my_loan_bp = Blueprint('my_loan_bp',__name__)

@my_loan_bp.route("/view_my_loan",methods = ['GET'])
@jwt_required()
def my_loan():
        return view_my_loan()
    