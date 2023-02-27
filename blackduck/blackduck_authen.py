# coding: utf-8
# Author: Siwanont Sittinam

import os
import requests
from dotenv import load_dotenv
load_dotenv()


class BlackduckAuthentication:
    def getHostname(self):
        HOSTNAME = os.getenv("BLACKDUCK_HOSTNAME")
        return HOSTNAME

    def getRequestHeader(self):
        HOSTNAME = os.getenv("BLACKDUCK_HOSTNAME")
        BLACKDUCK_KEY = os.getenv("BLACKDUCK_KEY")

        HEADER = {
            'Accept': 'application/vnd.blackducksoftware.status-4+json',
            'Authorization': BLACKDUCK_KEY
        }

        r = requests.post(HOSTNAME + "/api/tokens/authenticate", headers=HEADER, verify=False)

        if r.status_code == 200:
            r = r.json()

            return r


print(BlackduckAuthentication().getRequestHeader())
