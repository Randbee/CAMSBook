from github import Github
import os

# GitHub authentication (you'll need an access token)
ACCESS_TOKEN = 'YOUR_TOKEN_HERE'
g = Github(ACCESS_TOKEN)

# Base directory where the notebook folders are located
base_directory = '.'

# Iterate through the folders in the base directory
for folder_name in os.listdir(base_directory):
    folder_path = os.path.join(base_directory, folder_name)
    if os.path.isdir(folder_path):
        # Get an instance of the repository if it already exists
        repo_name = folder_name.replace(' ', '-')  # Remove spaces in the folder name
        user = g.get_user()
        repo = user.get_repo(repo_name)

        # Check if the repository exists
        if repo:
            # Delete the repository
            repo.delete()
            print(f'Repository deleted: {repo_name}')
        else:
            print(f'The repository {repo_name} does not exist')

print('Process completed.')
