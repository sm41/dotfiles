
from base64 import b64encode
from urllib import request


# def set_users_header():
#   head_dict_1 = {
#   "X-Radiko-App":         "pc_html5",
#   "X-Radiko-App-Version": "0.0.1",
#   "X-Radiko-Device":      "pc",
#   "X-Radiko-User":        "dummy_user"
#   }
#   return head_dict_1


# def get_header(auth_n_url, head_dict_n):
#   req = request.Request(url=auth_n_url, headers=head_dict_n, method="GET")
#   with request.urlopen(req) as res:
#     auth_n = res.headers
#   return auth_n


# def set_head_dict(auth_one):

#   AuthToken = str(auth_one['x-radiko-authtoken'])
#   KeyLength = int(auth_one["x-radiko-keylength"])
#   KeyOffset = int(auth_one["x-radiko-keyoffset"])

#   head_res = {
#     "AuthToken": AuthToken,
#     "KeyLength": KeyLength,
#     "KeyOffset": KeyOffset
#   }
#   return head_res


# def get_partial(head_res, authkey):
#   KeyOffset:int = head_res['KeyOffset']
#   KeyLength:int = head_res['KeyLength']
#   tmp_auth = authkey[KeyOffset:  KeyOffset + KeyLength]
#   partialkey = b64encode(tmp_auth.encode('utf-8')).decode('utf-8')
#   return partialkey


# def set_head_dict_2(partialkey, head_res):

#   X_Radiko_AuthToken = head_res['AuthToken']

#   head_dict_2 = {
#     "X-Radiko-Device":      "pc",
#     "X-Radiko-User":        "dummy_user",
#     "X-Radiko-AuthToken":   X_Radiko_AuthToken,
#     "X-Radiko-PartialKey":  partialkey
#   }
#   return head_dict_2


# def auth(auth1_url, auth2_url, authkey):
#   head_dict_1 = set_users_header()
#   auth_one    = get_header(auth1_url, head_dict_1)
#   head_res    = set_head_dict(auth_one)
#   partialkey  = get_partial(head_res, authkey)
#   head_dict_2 = set_head_dict_2(partialkey, head_res)
#   auth_two    = get_header(auth2_url, head_dict_2)
#   return head_dict_2





class oth:
  def __init__(self, auth1_url, auth2_url, authkey):

    __head_dict_1 = {
    "X-Radiko-App":         "pc_html5",
    "X-Radiko-App-Version": "0.0.1",
    "X-Radiko-Device":      "pc",
    "X-Radiko-User":        "dummy_user"
    }

    __auth_one    = self.get_header(auth1_url, __head_dict_1)
    __head_res    = self.set_head_dict(__auth_one)
    __partialkey  = self.get_partial(__head_res, authkey)
    __head_dict_2 = self.set_head_dict_2(__partialkey, __head_res)
    __auth_two    = self.get_header(auth2_url, __head_dict_2)

    self.xat = __head_dict_2['X-Radiko-AuthToken']


  def get_header(auth_n_url, head_dict_n):
    req = request.Request(url=auth_n_url, headers=head_dict_n, method="GET")
    with request.urlopen(req) as res:
      auth_n = res.headers
    return auth_n


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
