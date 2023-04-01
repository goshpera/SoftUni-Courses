usernames = input().split(", ")
allowed_usernames = []

for username in usernames:
    if 3 < len(username) < 16:
        if username.isalpha() or username.isdigit() or username.isalnum() or "-" in username or "_" in username:
            allowed_usernames.append(username)

print("\n".join(allowed_usernames))
