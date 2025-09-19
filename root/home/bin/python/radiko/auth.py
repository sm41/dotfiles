from base64 import b64encode
import requests

def iinntt():
  auth1_url   = "https://radiko.jp/v2/api/auth1"
  auth2_url   = "https://radiko.jp/v2/api/auth2"
  authkey     = "bcd151073c03b352e1ef2fd66c32209da9ca0afa"

  head_dict_1 = set_users_header()
  auth_one    = get_header(auth1_url, head_dict_1)
  head_res    = set_head_dict(auth_one)
  partialkey  = get_partial(head_res, authkey)
  head_dict_2 = set_head_dict_2(partialkey, head_res)
  auth_two    = get_header(auth2_url, head_dict_2)

  xrat = head_dict_2['X-Radiko-AuthToken']
  return xrat

def set_users_header():
  head_dict_1 = {
    "X-Radiko-App":         "pc_html5",
    "X-Radiko-App-Version": "0.0.1",
    "X-Radiko-Device":      "pc",
    "X-Radiko-User":        "dummy_user"
  }
  return head_dict_1

def get_header(auth_n_url, head_dict_n):
  req = requests.get(url = auth_n_url, headers = head_dict_n)
  return req.headers

def set_head_dict(auth_one):
  AuthToken = str(auth_one['x-radiko-authtoken'])
  KeyLength = int(auth_one["x-radiko-keylength"])
  KeyOffset = int(auth_one["x-radiko-keyoffset"])

  head_res = {
    "AuthToken": AuthToken,
    "KeyLength": KeyLength,
    "KeyOffset": KeyOffset
  }
  return head_res

def get_partial(head_res, authkey):
  KeyOffset:int = head_res['KeyOffset']
  KeyLength:int = head_res['KeyLength']
  tmp_auth = authkey[KeyOffset:  KeyOffset + KeyLength]
  partialkey = b64encode(tmp_auth.encode('utf-8')).decode('utf-8')
  return partialkey

def set_head_dict_2(partialkey, head_res):
  X_Radiko_AuthToken = head_res['AuthToken']

  head_dict_2 = {
    "X-Radiko-Device":      "pc",
    "X-Radiko-User":        "dummy_user",
    "X-Radiko-AuthToken":   X_Radiko_AuthToken,
    "X-Radiko-PartialKey":  partialkey
  }
  return head_dict_2