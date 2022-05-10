try:
    import json
    from flask import request,jsonify
    from extensions import db
    from model.user_model import User
    from werkzeug.security import generate_password_hash
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)


def register_user_service():
    try:
        # Getting data 
        username = request.json['username']
        password = request.json['password']
        admin = request.json['admin']

        # Checking if password length withing 8 and 16 character
        if len(password) < 8 or len(password) > 16:
            return jsonify({'error': "Password must be at least 8 characters long and less than 16 characters"}), 400

        # Checking if username length withing 8 and 16 character
        if len(username) < 8 or len(username) > 16:
            return jsonify({'error': "User Name must be at least 8 characters long and less than 16 characters"}), 400
        
        # Checking if the username is not alphanumeric or EMPTY
        if not username.isalnum() or " " in username or (len(password) <= 0):
            return jsonify({'error': "Username should be only alphanumeric, also no spaces"}), 400
        
        # Checking if the password is not alphanumeric or EMPTY
        if " " in password:
            return jsonify({'error': "Password can not have blank space(s)"}), 400

        # Checking the admin parameter
        if admin.lower() != "no" and admin.lower() != "yes":
            return jsonify({'error': "value for admin has to be yes or no"}), 400

        # Checking if the username is taken or not
        if User.query.filter_by(username=username).first() is not None:
            return jsonify({'error': "username is already taken"}), 409

        # Encrypting the password
        pwd_hash = generate_password_hash(password)

        # Creating USER bject and storing into database
        user = User(username=username, password=pwd_hash, admin=admin.lower())
        db.session.add(user)
        db.session.commit()

        return jsonify({
            'message': "User created",
            'user': {
                'username': username, "admin": admin.lower()
            }
        }), 201
    except KeyError as key_err:
        return jsonify({"error":"Missing details. Please provide username, password, admin values"}),400
    except Exception as e:
        return jsonify({"error":f"{e}"}),400
