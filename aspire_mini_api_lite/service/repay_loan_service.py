try:
    from flask import request,jsonify
    from model.user_model import User
    from model.loan_model import Loan
    from model.loan_repay_model import LoanRepay
    from flask_jwt_extended import get_jwt_identity
    from extensions import db
    import datetime
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)



def repay_scheduled_loan():
    try:
        # Get USER
        user_id = get_jwt_identity()
        user = User.query.filter_by(id=user_id).first()

        # Get loan details
        input_loan_id = int(request.json['loanrepay_id'])
        input_loan_amount = float(request.json['repay_amount'])
        loan_obj = LoanRepay.query.filter_by(loanrepay_id=input_loan_id).first()

        # User exists check
        if not user:
            return jsonify({"error":f"USER - {user_id} does not exists"}),404
        
        # Loan exists check
        if not loan_obj:
            return jsonify({"error":f"Loan - {input_loan_id} does not exists"}),404
        
        # User is admin check
        if (user.admin == 'yes'):
            return jsonify({"message": "Admin can not repay loan"}),401
        
        # Loan status check
        elif (loan_obj.repay_status != "APPROVED"):
            return jsonify({"message":f"You cannot repay {input_loan_id} as it is not APPROVED"}),401
        
        # Check if loan owener is the USER
        elif (loan_obj.user_id != user_id):
            return jsonify({"error": "You are not allowed to repay loan which is not yours"}),401
        
        # Check if repay amount matches with the database
        elif (loan_obj.repay_amount != input_loan_amount):
            return jsonify({"error": "You have to pay the exact loan repay amount"}),401
        else:
            # Updating repay status
            LoanRepay.query.filter_by(loanrepay_id=input_loan_id).update({"repay_status": "PAID"})
            db.session.commit()
            # Check if all repayments are PAID, if yes update loan table 
            loanrepay_loan_id = loan_obj.loan_id
            
            loanrepay_loan_id_obj = LoanRepay.query.filter_by(loan_id=loanrepay_loan_id, repay_status='APPROVED').first()
            
            # Check if all schedule payments were PAID
            if loanrepay_loan_id_obj:
                pass
            else:
                # Updating the Loan table
                Loan.query.filter_by(loan_id=loanrepay_loan_id).update({"loan_status": "PAID"})
                db.session.commit()
            return jsonify({"message": f"Loan {input_loan_id} has been PAID successfully!"}),201
    except KeyError as key_err:
        return jsonify({"error":"Please provide loanrepay_id and repay_amount"}),400
    except Exception as e:
        return jsonify({"error":f"{e}"}),400