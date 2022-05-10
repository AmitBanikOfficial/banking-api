import os
import config
from app import app
import unittest
import json

my_server = 'http://127.0.0.1:5000'

if os.path.exists(config.db_file):
    os.remove(config.db_file)

class TestApp(unittest.TestCase):
            
    def test_01_register_normal_user_with_proper_details(self):
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5678","admin":"no"}
        resp = self.client.post(f"{my_server}/register",data=json.dumps(item),headers={'Content-Type': 'application/json'})
        self.assertEqual(resp.status_code,201)
            
    def test_02_register_normal_user_with_same_username_details(self):
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5678","admin":"no"}
        resp = self.client.post(f"{my_server}/register",data=json.dumps(item),headers={'Content-Type': 'application/json'})
        self.assertEqual(resp.status_code,409)
            
    def test_03_register_normal_user_with_missing_details(self):
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5678"}
        resp = self.client.post(f"{my_server}/register",data=json.dumps(item),headers={'Content-Type': 'application/json'})
        self.assertEqual(resp.status_code,400)
            
    def test_04_register_admin_user_with_proper_details(self):
        self.client = app.test_client()
        item = {"username":"adminusername","password":"adminusername","admin":"Yes"}
        resp = self.client.post(f"{my_server}/register",data=json.dumps(item),headers={'Content-Type': 'application/json'})
        self.assertEqual(resp.status_code,201)
            
    def test_05_register_admin_user_with_missing_details(self):
        self.client = app.test_client()
        item = {"username":"adminusername","password":"adminusername"}
        resp = self.client.post(f"{my_server}/register",data=json.dumps(item),headers={'Content-Type': 'application/json'})
        self.assertEqual(resp.status_code,400)
        
    def test_06_login_normal_user_with_proper_details(self):
        # Initiating client object  
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5678"}
        result = self.client.post(f'{my_server}/login',data=json.dumps(item),headers={'Content-Type': 'application/json'})
        self.assertEqual(result.status_code,201)
        
    def test_07_login_normal_user_with_incorrect_details(self):
        # Initiating client object  
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5688"}
        result = self.client.post(f'{my_server}/login',data=json.dumps(item),headers={'Content-Type': 'application/json'})
        self.assertEqual(result.status_code,401)
        
    def test_08_apply_new_loan_with_correct_details(self):
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5678"}
        result = self.client.post(f'{my_server}/login',data=json.dumps(item),headers={'Content-Type': 'application/json'})
        data = json.loads(result.data)
        access_token = data['access']
        loan_application_data = {'loan_amount':2000,'term':3}
        apply_loan = self.client.post(f'{my_server}/apply_loan',data=json.dumps(loan_application_data),headers={'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"})
        self.assertEqual(apply_loan.status_code,201)
        
    def test_09_apply_new_loan_with_admin_details(self):
        self.client = app.test_client()
        item = {"username":"adminusername","password":"adminusername"}
        result = self.client.post(f'{my_server}/login',data=json.dumps(item),headers={'Content-Type': 'application/json'})
        data = json.loads(result.data)
        access_token = data['access']
        loan_application_data = {'loan_amount':20000,'term':3}
        apply_loan = self.client.post(f'{my_server}/apply_loan',data=json.dumps(loan_application_data),headers={'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"})
        self.assertEqual(apply_loan.status_code,401)
        

    def test_10_approve_new_loan_with_non_admin_details(self):
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5678"}
        result = self.client.post(f'{my_server}/login',data=json.dumps(item),headers={'Content-Type': 'application/json'})
        data = json.loads(result.data)
        access_token = data['access']
        loan_application_data = {'loan_id':1}
        approve_loan = self.client.put(f'{my_server}/approve_loan',data=json.dumps(loan_application_data),headers={'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"})
        self.assertEqual(approve_loan.status_code,401)
        
    
    def test_11_approve_new_loan_with_admin_details(self):
        self.client = app.test_client()
        item = {"username":"adminusername","password":"adminusername"}
        result = self.client.post(f'{my_server}/login',data=json.dumps(item),headers={'Content-Type': 'application/json'})
        data = json.loads(result.data)
        access_token = data['access']
        loan_application_data = {'loan_id':1}
        approve_loan = self.client.put(f'{my_server}/approve_loan',data=json.dumps(loan_application_data),headers={'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"})
        self.assertEqual(approve_loan.status_code,201)
        

    def test_12_view_my_loan_with_admin_details(self):
        self.client = app.test_client()
        item = {"username":"adminusername","password":"adminusername"}
        result = self.client.post(f'{my_server}/login',data=json.dumps(item),headers={'Content-Type': 'application/json'})
        data = json.loads(result.data)
        access_token = data['access']
        view_loan = self.client.get(f'{my_server}/view_my_loan',headers={'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"})
        self.assertEqual(view_loan.status_code,401)
        
    
    def test_13_view_my_loan_with_user_details(self):
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5678"}
        result = self.client.post(f'{my_server}/login',data=json.dumps(item),headers={'Content-Type': 'application/json'})
        data = json.loads(result.data)
        access_token = data['access']
        view_loan = self.client.get(f'{my_server}/view_my_loan',headers={'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"})
        self.assertEqual(view_loan.status_code,200)
        
    
    def test_14_repay_loan_with_admin_details(self):
        self.client = app.test_client()
        item = {"username":"adminusername","password":"adminusername"}
        result = self.client.post(f'{my_server}/login',data=json.dumps(item),headers={'Content-Type': 'application/json'})
        data = json.loads(result.data)
        access_token = data['access']
        repay_loan_data = {'loanrepay_id':1,'repay_amount':666.67}
        repay_loan = self.client.put(f'{my_server}/repay_loan',data=json.dumps(repay_loan_data),headers={'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"})
        self.assertEqual(repay_loan.status_code,401)
        

    def test_15_repay_loan_with_user_details(self):
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5678"}
        result = self.client.post(f'{my_server}/login',data=json.dumps(item),headers={'Content-Type': 'application/json'})
        data = json.loads(result.data)
        access_token = data['access']
        repay_loan_data = {'loanrepay_id':1,'repay_amount':666.67}
        repay_loan = self.client.put(f'{my_server}/repay_loan',data=json.dumps(repay_loan_data),headers={'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"})
        self.assertEqual(repay_loan.status_code,201)

    def test_16_repay_loan_with_incorrect_details(self):
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5678"}
        result = self.client.post(f'{my_server}/login',data=json.dumps(item),headers={'Content-Type': 'application/json'})
        data = json.loads(result.data)
        access_token = data['access']
        repay_loan_data = {'loanrepay_id':19,'repay_amount':666.67}
        repay_loan = self.client.put(f'{my_server}/repay_loan',data=json.dumps(repay_loan_data),headers={'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"})
        self.assertEqual(repay_loan.status_code,404)

    def test_17_repay_loan_with_incorrect_amount(self):
        self.client = app.test_client()
        item = {"username":"username5678","password":"username5678"}
        result = self.client.post(f'{my_server}/login',data=json.dumps(item),headers={'Content-Type': 'application/json'})
        data = json.loads(result.data)
        access_token = data['access']
        repay_loan_data = {'loanrepay_id':1,'repay_amount':66.67}
        repay_loan = self.client.put(f'{my_server}/repay_loan',data=json.dumps(repay_loan_data),headers={'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"})
        self.assertEqual(repay_loan.status_code,401)

if __name__ == "__main__":
    unittest.main()
