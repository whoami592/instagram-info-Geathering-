import instaloader

def get_instagram_info(username):
    try:
        # Initialize Instaloader
        L = instaloader.Instaloader()

        # Load the profile
        profile = instaloader.Profile.from_username(L.context, username)

        # Fetch and display public account details
        print(f"Username: {profile.username}")
        print(f"Full Name: {profile.full_name}")
        print(f"Followers: {profile.followers}")
        print(f"Following: {profile.followees}")
        print(f"Posts: {profile.mediacount}")
        print(f"Bio: {profile.biography}")
        print(f"Is Private: {profile.is_private}")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Error: The profile '{username}' does not exist.")
    except instaloader.exceptions.ConnectionException:
        print("Error: Connection issue. Please check your internet or try again later.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    target_username = input("Enter the Instagram username: ")
    get_instagram_info(target_username)