# These details can be stored in env variables

import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_file = os.path.join(basedir, 'aspire.db')
db_path = 'sqlite:///' + os.path.join(basedir, 'aspire.db')

secrete_key = "True"

jwt_access_expires = 600