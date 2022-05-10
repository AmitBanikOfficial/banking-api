try:
    from flask import Blueprint
    from service.approve_new_loan_service import approve_new_loan
    from flask_jwt_extended import jwt_required
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)


approve_loan_bp = Blueprint('approve_loan_bp',__name__)


@approve_loan_bp.route("/approve_loan",methods = ['PUT'])
@jwt_required()
def approve_loan():
    return approve_new_loan()