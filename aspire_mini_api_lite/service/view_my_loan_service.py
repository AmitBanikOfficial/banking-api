try:
    from flask import jsonify
    from model.user_model import User
    from model.loan_model import Loan, loans_schema
    from model.loan_repay_model import LoanRepay, loans_repay_schema
    from flask_jwt_extended import get_jwt_identity
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)



def view_my_loan():
    try:
        # Get User
        user_id = get_jwt_identity()
        user = User.query.filter_by(id=user_id).first()
        
        # User exists validation
        if not user:
            return jsonify({"error":f"Userid {user_id} does not exist"}),404
        
        # User is admin check
        if (user.admin == 'yes'):
            return jsonify({"message":"Admin is not eligible for loan"}),401
        else:
            # Getting loan details for the USER
            loan_data = Loan.query.filter_by(user_id=user_id)
            loan_data_result = loans_schema.dump(loan_data)
            loan_repay_data = LoanRepay.query.filter_by(user_id=user_id)
            loan_repay_result = loans_repay_schema.dump(loan_repay_data)
        
            if len(loan_data_result) > 0:
                if len(loan_repay_result) > 0:
                    return jsonify({"loan_data":loan_data_result,"loan_repay_data":loan_repay_result}),200
                else:
                    return jsonify({"loan_data":loan_data_result}),200
            else:
                return jsonify({"msg":"You dont have any loan data"}),404
    except KeyError as key_err:
        return jsonify({"error":f"{key_err}"}),400
    except Exception as e:
        return jsonify({"error":f"{e}"}),400