def check_email_quality(email_list):
    seen = set()
    valid_emails = []
    invalid_emails = []

    for email in email_list:
        if email in seen:
            continue
        seen.add(email)

        split_email = email.split('@')
        if len(split_email) == 2 and split_email[0] and '.' in split_email[1]:
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
        "another@test.io"
    ]
    print(check_email_quality(email_list))