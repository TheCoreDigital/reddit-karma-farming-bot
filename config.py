import os

def save_config_env():
    id = input("Enter ID: ")
    secret = input("Enter Secret: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if os.path.exists("config.env"):
        print("config.env file already exists. Updating the configuration.")
        mode = "w"  # Append mode
    else:
        print("config.env file does not exist. Creating a new configuration.")
        mode = "w"  # Write mode

    with open("config.env", mode) as f:
        f.write(f"id={id}\n")
        f.write(f"secret={secret}\n")
        f.write(f"username={username}\n")
        f.write(f"password={password}\n")

    print("Configuration saved to config.env")

save_config_env()
