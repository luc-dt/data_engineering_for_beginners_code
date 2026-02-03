import re

EMAIL_REGEX = re.compile(r"^[^@]+@[^@]+\.[^@]+$")

def validate_emails_with_regex(email_list):
    seen = set()
    valid_emails = []
    invalid_emails = []

    for email in email_list:
        if email in seen:
            continue 
        seen.add(email)

        if EMAIL_REGEX.match(email):
            valid_emails.append(email)
        else:
            invalid_emails.append(email)
    return {
        "valid_emails": valid_emails,
        "invalid_emails": invalid_emails
    }
if __name__ == "__main__":
    email_list = [
        "john.doe@company.com",
        "jane.smith@email.co.uk",
        "invalid-email",
        "bob@gmail.com",
        "alice.brown@company.com",
        "john.doe@company.com", # duplicate
        "missing@domain",
        "test@example.org",
        "@nodomain.com",
        "jane.smith@email.co.uk", # duplicate
        "valid.user@site.net",
        "no-at-symbol.com",
        "another@teast.io"
    ]
    print(validate_emails_with_regex(email_list))