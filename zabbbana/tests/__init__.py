from zabbbana import Zabbbana
from .credentials import *

jordan = Zabbbana(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, access_token=ACCESS_TOKEN, state="myrandomkey",\
                  redirect_uri=REDIRECT_URI)
