try:
    from extensions import db,ma
    from sqlalchemy import Column, Integer, String, Float, ForeignKey, DATE
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)


# database models
class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String,nullable = False, unique = True)
    password = Column(String,nullable = False)
    admin = Column(String,nullable = False)
    # loans = db.relationship('Loan', backref="user")


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password', 'admin')


user_schema = UserSchema()
users_schema = UserSchema(many=True)