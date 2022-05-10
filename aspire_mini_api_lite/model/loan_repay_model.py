try:
    from extensions import db,ma
    from sqlalchemy import Column, Integer, String, Float, ForeignKey, DATE
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)


# database models
class LoanRepay(db.Model):
    __tablename__ = 'loanrepay'
    loan_id = Column(Integer, ForeignKey('loan.loan_id'))
    loanrepay_id = Column(Integer, nullable = False, primary_key=True)
    repay_amount = Column(Float,nullable = False)
    repay_date = Column(DATE,nullable = False)
    user_id = Column(Integer,ForeignKey('loan.user_id'))
    repay_status = Column(String,nullable = False)


class LoanRepaySchema(ma.Schema):
    class Meta:
        fields = ('loan_id','loanrepay_id', 'repay_amount', 'repay_date', 'user_id','repay_status')


loan_repay_schema = LoanRepaySchema()
loans_repay_schema = LoanRepaySchema(many=True)