
try:
    from flask import Flask
    from config import db_path, secrete_key,jwt_access_expires
    from flask_jwt_extended import JWTManager
    from extensions import db,ma
    
    from route.register_user_route import register_bp
    from route.login_user_route import login_bp
    from route.apply_loan_route import apply_loan_bp
    from route.approve_loan_route import approve_loan_bp
    from route.repay_loan_route import repay_loan_bp
    from route.view_my_loan_route import my_loan_bp
    
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)


app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
app.config['SECRET_KEY'] = secrete_key
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = jwt_access_expires


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app)
db.init_app(app)
ma.init_app(app)


app.register_blueprint(register_bp)
app.register_blueprint(login_bp)
app.register_blueprint(apply_loan_bp)
app.register_blueprint(approve_loan_bp)
app.register_blueprint(repay_loan_bp)
app.register_blueprint(my_loan_bp)

if __name__ == '__main__':
    app.run()
