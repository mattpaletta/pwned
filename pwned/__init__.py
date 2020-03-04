import requests
import os
import hashlib

_BASE_URL = "https://haveibeenpwned.com/api/"

def email(email, quiet = False):
	BREACHED_API = _BASE_URL + "breachedaccount/{account}".format(account = email)
	api_key_key = "hibp-api-key"
	assert api_key_key in os.environ.keys(), "Failed to find HIBP api key.  You can get one here: https://haveibeenpwned.com/API/Key"
	hibp_api_key = os.environ["hibp-api-key"]
	response = requests.get(BREACHED_API, json = {api_key_key: hibp_api_key})
	assert response.status_code == 200, "An error occured while making the request"
	num_breaches = len(response.json())
	if not quiet:
		print("Found {0} Breaches".format(num_breaches))
		for breach in response.json():
			print("Breach: {0}".format(breach.get("title")))
	return num_breaches

def password(password, quiet = False):
	PASSWORD_API = "https://api.pwnedpasswords.com/range/"
	pass_hash = str(hashlib.sha1(password.encode("utf-8")).hexdigest()).upper()
	response = requests.get(PASSWORD_API + pass_hash[:5])
	lines = response.text.split("\n")
	for h in lines:
		orig, count = h.split(":")
		if pass_hash[:5] + orig == pass_hash:
			if not quiet:
				print("PWNED: Password in {0} breaches.".format(count))
			return count
	return 0
