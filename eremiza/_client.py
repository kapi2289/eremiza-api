import requests

from ._utils import gen_jwt


class Client:

    def __init__(self, email, password, api_url="https://e-remiza.pl/Terminal"):
        self.email = email
        self.password = password
        if api_url[-1] == '/':
            api_url = api_url[0:-1]
        self.api_url = api_url
        self.user = None
        self.login()

    def _request(self, method="GET", endpoint=None, **kwargs):
        headers = {
            "Accept": "application/json",
            "JWT": gen_jwt(self.email, self.password),
        }
        if endpoint[0] != '/':
            endpoint = '/' + endpoint
        r = requests.request(method, self.api_url + endpoint, headers=headers, **kwargs)
        r.raise_for_status()
        return r.json()

    def _get(self, endpoint, **kwargs):
        return self._request(method="GET", endpoint=endpoint, **kwargs)

    def _post(self, endpoint, **kwargs):
        return self._request(method="POST", endpoint=endpoint, **kwargs)

    def login(self):
        self.user = self._get("/User/GetUser")

    def get_alarms(self, count=3, offset=0):
        return self._get("/Alarm/GetAlarmList",
                         params={"ouId": self.user["bsisOuId"], "count": count, "offset": offset})
