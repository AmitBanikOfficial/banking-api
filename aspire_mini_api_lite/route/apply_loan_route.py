try:
    from flask import Blueprint
    from service.apply_new_loan_service import apply_new_loan
    from flask_jwt_extended import jwt_required
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)

apply_loan_bp = Blueprint('apply_loan_bp',__name__)

@apply_loan_bp.route("/apply_loan",methods = ['POST'])
@jwt_required()
def apply_loan():
    return apply_new_loan()
