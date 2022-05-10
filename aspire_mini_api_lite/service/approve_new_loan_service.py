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



def approve_new_loan():
    try:
        # Get the USER
        user_id = get_jwt_identity()
        user = User.query.filter_by(id=user_id).first()
        if not user:
            return jsonify({"error":f"Userid {user_id} does not exist"}),404
        # Check if USER is admin
        if (user.admin == 'yes'):
            loan_id = int(request.json['loan_id'])
            loan = Loan.query.filter_by(loan_id=loan_id).first()
            # Check if the loan exists
            if not loan:
                return jsonify({"error":f"Loan {loan_id} does not exist"}),404
            if (loan.loan_status == 'PENDING'):
                # Updating loan status in loan table
                Loan.query.filter_by(loan_id=loan_id).update({"loan_status": "APPROVED"})
                db.session.commit()

                # Updating schedule payments 
                loan_repay_obj = Loan.query.filter_by(loan_id=loan_id).first()
                term = loan_repay_obj.loan_term
                user_id = loan_repay_obj.user_id
                loan_amount = loan_repay_obj.loan_amount
                repay_amount = loan_amount / term
                repay_amount = round(repay_amount,2)
                loan_apply_date = loan_repay_obj.loan_apply_date
                for i in range(1,term+1):
                    
                    repay_date = loan_apply_date + datetime.timedelta(days=i * 7)
                    # Inserting repay data into LoanRepay table
                    loan_repay = LoanRepay(loan_id=loan_id,repay_amount=repay_amount,user_id=user_id,repay_status='APPROVED',repay_date=repay_date)
                    db.session.add(loan_repay)
                    db.session.commit()

                return jsonify({"message":f"Loan: {loan_id} has been APPROVED"}),201
            else:
                return jsonify({"message": f"{loan_id} status is not PENDING. Cannot approve"}),409
        else:
            return jsonify({"message": "Only Admins can approve loan request"}),401
    except KeyError as key_err:
        return jsonify({"error":"Please provide loan_id"}),400
    except Exception as e:
        return jsonify({"error":f"{e}"}),400
