try:
    from flask_sqlalchemy import SQLAlchemy
    from flask_marshmallow import Marshmallow
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)


db = SQLAlchemy()
ma = Marshmallow()