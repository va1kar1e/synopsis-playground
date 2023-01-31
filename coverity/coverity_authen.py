# coding: utf-8
# Author: Siwanont Sittinam

import os
import base64
from dotenv import load_dotenv
load_dotenv()


class CoverityAuthentication:
    def getHostname(self):
        HOSTNAME = os.getenv("COVERITY_HOSTNAME")
        return HOSTNAME

    def getRequestHeader(self):
        COVERITY_USERNAME = os.getenv("COVERITY_USERNAME")
        COVERITY_PASSWORD = os.getenv("COVERITY_PASSWORD")

        TOKEN = (COVERITY_USERNAME + ":" + COVERITY_PASSWORD).encode("ascii")
        TOKEN_AUTH = "Basic " + base64.b64encode(TOKEN).decode("utf-8")

        del COVERITY_USERNAME, COVERITY_PASSWORD, TOKEN

        return {
            'Accept': 'application/json',
            'Authorization': TOKEN_AUTH
        }
