"""
CP1404 | Practical 05 | Emails and Names
Estimate: 30 minutes
Actual:   27 minutes
"""

def main():
    """Store emails and corresponding names."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm not in ('', 'y', 'yes'):
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name.title()} ({email})")


def get_name_from_email(email):
    """Extract a name from the email address."""
    name_part = email.split('@')[0]
    parts = name_part.replace('.', ' ').title().split()
    return " ".join(parts)


if __name__ == "__main__":
    main()
