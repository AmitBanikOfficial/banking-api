
# Banking API

A simple banking API which can:

    - register users and admin
    - allow users to login
    - allow users to apply for loan using JWT
    - allow admin to approve loan using JWT
    - automatically adds payment schedule with weekly frequency
    - allow user to repay the loan
    - mark the loan as PAID once all the repayments are PAID

### Requirements

You will need Python and virtualenv module installed. Remaning will be installed via requriements.txt.

### Install

Clone the repo, create a virtualenv and install the requirements:

```
git clone https://github.com/AmitBanikOfficial/banking-api.git
cd banking-api/aspire_mini_api_lite
virtualenv miniaspireenv
for Windows:
miniaspireenv\Scripts\activate
for linux:
source miniaspireenv/bin/activate
pip install -r requirements
```

### Run 

```
for Windows:
python app.py
for linux:
python3 app.py
```

### Routes

```
http://127.0.0.1:5000/register
http://127.0.0.1:5000/login
http://127.0.0.1:5000/apply_loan
http://127.0.0.1:5000/approve_loan
http://127.0.0.1:5000/view_my_loan
http://127.0.0.1:5000/repay_loan
```

### API

#### Register User

```
http://127.0.0.1:5000/register
```
Method  - POST

Accepts - username(str), password(str), admin(str) - in form of JSON

Returns - JSON

Username length validation:
![Register](screenshots/username_length_validation.png)

Username type validation:
![Register](screenshots/username_should_be_only_alphanumeric.png)

Password length validation:
![Register](screenshots/password_length_validation.png)

Password type validation:
![Register](screenshots/password_cannot_have_space.png)

Username already taken validation:
![Register](screenshots/username_is_already_taken.png)

Admin value validation:
![Register](screenshots/admin_can_be_yes_or_no.png)

Registering a normal user with missing details:
![Register](screenshots/register_normal_user_with_missing_details.png)

Registering a normal user with proper details:
![Register](screenshots/register_normal_user_with_proper_details.png)

Registering an admin user with proper details:
![Register](screenshots/admin_created.png)


After successfull registration, User table looks like:

![Register](screenshots/user_data_in_table.png)


#### Login User

```
http://127.0.0.1:5000/login
```

Method  - POST 

Accepts - username(str), password(str) in form of JSON

Returns - JSON, if successfull then with Access Token

If the user does not exist in the database:
![Login](screenshots/login_user_does_not_exist.png)

If user provides incorrect password:
![Login](screenshots/login_user_with_incorrect_password.png)

Successfull user login:
![Login](screenshots/login_user_does_not_have_loan_data.png)

Successfull admin login:
![Login](screenshots/login_admin_user.png)


#### Apply Loan

```
http://127.0.0.1:5000/apply_loan
```

Method  - POST 

Accepts - loan_amount(float), term(int) in form of JSON, requires access token as Authorization

Returns - JSON

Admin cannot apply for loan:
![Apply](screenshots/admin_cant_apply_loan.png)

User successfully applies for a loan:
![Apply](screenshots/loan_application_submitted_successfully.png)


Loan data after successfull application and before admin approval:
![Apply](screenshots/loan_data_after_application_before_admin_approval.png)


#### Approve Loan

```
http://127.0.0.1:5000/approve_loan
```

Method  - PUT 

Accepts - loan_id(int) in form of JSON, requires access token as Authorization

Returns - JSON


Only admin can approve loan request:
![Approve](screenshots/only_admin_can_approve_loan_request.png)


Admin approves the loan request:
![Approve](screenshots/loan_has_been_approved.png)

Loan data after admin approval:
![Approve](screenshots/loan_data_table_after_loan_has_been_approved.png)


Loan repay data after admin approval, this app will automatically add repayment schedule weekly basis based of the term:
![Approve](screenshots/loanrepay_data_table_after_loan_has_been_approved.png)



#### View My Loan

```
http://127.0.0.1:5000/view_my_loan
```

Method  - GET 

Accepts - requires access token as Authorization

Returns - JSON

Returns loan and loan repayment details for user:
![View](screenshots/user_can_see_their_loan_details.png)


#### Repay Loan

```
http://127.0.0.1:5000/repay_loan
```

Method  - PUT 

Accepts - loanrepay_id and repay_amount in form of JSON, requires access token as Authorization

Returns - JSON

Admin cannot repay loan:
![Repay](screenshots/when_admin_tries_repay_loan.png)


User paid scheduled payment:
![Repay](screenshots/user_paid_1st_payment.png)

Loan repay table data after scheduled payment:
![Repay](screenshots/repay_table_data_after_user_paid_1st_payment.png)

Loan repay table data after user paid all scheduled payments:
![Repay](screenshots/repay_table_data_after_user_paid_all_payment.png)

Loan table data after after user paid all scheduled payments, the loan is PAID automatically:
![Repay](screenshots/loan_table_data_after_user_paid_all_payment.png)




## Run Unittest

```
cd banking-api/aspire_mini_api_lite
python test_app.py
```
















