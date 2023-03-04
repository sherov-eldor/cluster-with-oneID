from flask import Config

ONEID_LOGIN = "at_agrosanoat_markazi"
ONEID_PASSWORD = "nCeV5BFAcruvPxW9sK721qdR"
ONEID_URL = "https://sso.egov.uz/sso/oauth/Authorization.do" # defaul https://sso.egov.uz/sso/oauth/Authorization.do 

# SECRET_KEY = '114d7b45bc27a059cfb5f327378eb01d1'

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost:5432/one_ID"
SQLALCHEMY_ECHO = True
