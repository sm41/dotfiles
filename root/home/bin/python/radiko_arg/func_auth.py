
from base64 import b64encode
from urllib import request


def set_users_header():
  head_dict_1:dict = {
  "X-Radiko-App":         "pc_html5",
  "X-Radiko-App-Version": "0.0.1",
  "X-Radiko-Device":      "pc",
  "X-Radiko-User":        "dummy_user"
  }
  return head_dict_1


def get_header(auth_n_url:str, head_dict_n:list):
  req = request.Request(url=auth_n_url, headers=head_dict_n, method="GET")
  with request.urlopen(req) as res:
    auth_n = res.headers
  return auth_n


def set_head_dict(auth_one:dict):

  AuthToken:str = str(auth_one['x-radiko-authtoken'])
  KeyLength:int = int(auth_one["x-radiko-keylength"])
  KeyOffset:int = int(auth_one["x-radiko-keyoffset"])

  head_res:dict = {
    "AuthToken": AuthToken,
    "KeyLength": KeyLength,
    "KeyOffset": KeyOffset
  }
  return head_res


def get_partial(head_res:dict, authkey:str):

  KeyOffset:int = head_res['KeyOffset']
  KeyLength:int = head_res['KeyLength']

  tmp_auth = authkey[KeyOffset:  KeyOffset + KeyLength]
  partialkey = b64encode(tmp_auth.encode('utf-8')).decode('utf-8')

  return partialkey


def set_head_dict_2(partialkey:str, head_res:dict):

  X_Radiko_AuthToken:str = head_res['AuthToken']

  head_dict_2:dict = {
    "X-Radiko-Device":      "pc",
    "X-Radiko-User":        "dummy_user",
    "X-Radiko-AuthToken":   X_Radiko_AuthToken,
    "X-Radiko-PartialKey":  partialkey
  }
  return head_dict_2