import os

def save_config_env():
    reddit_id = input("Enter ID: ")
    reddit_secret = input("Enter Secret: ")
    reddit_username = input("Enter Username: ")
    reddit_password = input("Enter Password: ")

    if os.path.exists("config.env"):
        print("config.env file already exists. Updating the configuration.")
        mode = "w"  # Append mode
    else:
        print("config.env file does not exist. Creating a new configuration.")
        mode = "w"  # Write mode

    with open("config.env", mode) as f:
        f.write(f"reddit_id='{reddit_id}'\n")
        f.write(f"reddit_secret='{reddit_secret}'\n")
        f.write(f"reddit_username='{reddit_username}'\n")
        f.write(f"reddit_password='{reddit_password}'\n")

    print("Configuration saved to config.env")

save_config_env()
