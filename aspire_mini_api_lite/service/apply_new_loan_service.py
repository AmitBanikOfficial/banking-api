try:
    from flask import request,jsonify
    from model.user_model import User
    from model.loan_model import Loan
    from flask_jwt_extended import get_jwt_identity
    from extensions import db
    import datetime
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)



def apply_new_loan():
    try:
        # Getting the data
        loan_amount = float(request.json['loan_amount'])
        term = int(request.json['term'])
        # Setting default status as PENDING
        loan_status = "PENDING"
        # Getting the USER
        user_id = get_jwt_identity()
        user = User.query.filter_by(id=user_id).first()
        if not user:
            return jsonify({"error":f"Userid {user_id} does not exist"}),404
        # Check if USER is admin
        if (user.admin == 'yes'):
            return jsonify({"error":"Admin cant apply for loan"}),401
        else:
            # Inserting New Loan into Database
            loan = Loan(loan_amount=loan_amount,loan_term=term,user_id=user_id,loan_status=loan_status,loan_apply_date=datetime.datetime.now().date())
            db.session.add(loan)
            db.session.commit()
            return jsonify({"message":"Loan application submitted successfully",
                            "loan_amount":loan_amount,
                            "loan_term": term,
                            "loan_status": loan_status}),201
    except KeyError as key_err:
        return jsonify({"error":"Please provide loan_amount and term"}),400
    except Exception as e:
        return jsonify({"error":f"{e}"}),400