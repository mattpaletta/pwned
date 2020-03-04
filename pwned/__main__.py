import sys
from pwned import email, password

def main():
	assert len(sys.argv) > 1, "Include an email or password"
	item = sys.argv[1]
	count = email(item) if "@" in item else password(item)
	if count == 0:
		print("SAFE")
	else:
		print("You have been pwned.")
		exit(1)

if __name__ == "__main__":
	main()
