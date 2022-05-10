try:
    from extensions import db,ma
    from sqlalchemy import Column, Integer, String, Float, ForeignKey, DATE
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)


class Loan(db.Model):
    __tablename__ = 'loan'
    loan_id = Column(Integer, nullable = False, primary_key=True)
    loan_amount = Column(Float,nullable = False)
    loan_apply_date = Column(DATE,nullable = False)
    loan_term = Column(Integer, nullable = False)
    user_id = Column(Integer,ForeignKey('user.id'))
    loan_status = Column(String,nullable = False)



class LoanSchema(ma.Schema):
    class Meta:
        fields = ('loan_id', 'loan_amount', 'loan_term', 'user_id', 'loan_status','loan_apply_date')


loan_schema = LoanSchema()
loans_schema = LoanSchema(many=True)

