# pwned

# Installation
```
pip install git+://github.com/mattpaletta/pwned.git
```

# Usage

## Check emails
(replace with your email)
```
pwned jsmith@example.com
```

## Check passwords
(replace `password` with your password)
```
pwned password
```

## Programatically
```python
import pwned

num_email_breaches = pwned.email( email )
check_email = pwned.email( email ) == 0

num_password_breaches = pwned.password( password )
check_password = pwned.password( password ) == 0
```

### API Key
In order to verify emails, you must get an API key at: [https://haveibeenpwned.com/API/Key](https://haveibeenpwned.com/API/Key)
Once you have a key, save it as an environment variable under: `hibp-api-key`
