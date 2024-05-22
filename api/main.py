from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT

from models.account import Account

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://localhost:8081", "http://localhost:1500",
                   "http://172.20.0.3:1500", "http://localhost:1600", "http://172.20.0.2:1500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class PostAccountPayload(BaseModel):
    name: str
    user_name: str
    password: str
    email: Optional[str] = None
    phone: str
    address: Optional[str] = None
    referral_code: Optional[str] = None

class LoginAccount(BaseModel):
    user_name: str
    password: str


@app.get('/account/{account_id}')
def get_account_info(account_id):
    """Get account information"""
    account = (Account.select().where(Account.id == account_id)).dicts()
    account_info = list(account)
    if not account_info or len(account_info) == 0:
        raise Exception("Account not found")
    return account_info[0]

@app.post('/accounts')
def post_account_info(payload:PostAccountPayload):
    """Create new User"""
    payload = payload.dict()
    validate_user_name_invalid(payload["user_name"])
    try:
        Account.create(**payload)
        return Response(status_code=HTTP_204_NO_CONTENT)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post('/logins')
def login(account: LoginAccount):
    """Login"""
    account = account.dict()
    query = Account.select().where(
        (Account.user_name == account['user_name']) & (Account.password == account['password'])).dicts()
    query_len = list(query)
    if len(query_len):
        del query_len[0]["password"]
        return {"code": 200, "data": query_len}
    else:
        return {"code": 400, "data": query_len}

def validate_user_name_invalid(user_name_payload):
    """Validate user name exists"""
    user_names = (Account.select()).dicts()
    user_names_info = list(user_names)
    for user_name_info in user_names_info:
        if user_name_info['user_name'] == user_name_payload:
            raise HTTPException(status_code=400, detail="User name already exists")