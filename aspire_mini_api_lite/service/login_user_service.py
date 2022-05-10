try:
    from flask import request,jsonify
    from extensions import db
    from model.user_model import User
    from werkzeug.security import check_password_hash
    from flask_jwt_extended import create_access_token
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)


def login_user_service():
    try:
        # Getting data for login
        username = request.json['username']
        password = request.json['password']
        
        # Checking if the USER exists
        user = User.query.filter_by(username=username).first()
        if user:

            # Check if the USER had provided correct password
            if (check_password_hash(user.password,password)):
                
                # Generating Token for USER
                access = create_access_token(identity=user.id)
                admin = ''
                if (user.admin == 'yes'):
                    admin = 'Admin'
                return jsonify({"Message":f" Welcome: {admin} {username}!","access": access}),201
            else:
                return jsonify({"Message":f" Incorrect password for: {username}!!"}),401
        else:
                return jsonify({"Message":f" Username: {username} does not exist!!"}),401
    except KeyError as key_err:
        return jsonify({"error":"Please provide username and password"}),400
    except Exception as e:
        return jsonify({"error":f"{e}"}),400