try:
    from flask import Blueprint
    from service.repay_loan_service import repay_scheduled_loan
    from flask_jwt_extended import jwt_required
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)

repay_loan_bp = Blueprint('repay_loan_bp',__name__)

@repay_loan_bp.route("/repay_loan",methods = ['PUT'])
@jwt_required()
def repay_loan():
    return repay_scheduled_loan()
