from github import Github
import os

# GitHub authentication (you'll need an access token)
ACCESS_TOKEN = 'YOUR_TOKEN_HERE'
g = Github(ACCESS_TOKEN)

# Base directory where the notebook folders are located
base_directory = 'notebooks'

# Iterate through the folders in the base directory
for folder_name in os.listdir(base_directory):
    folder_path = os.path.join(base_directory, folder_name)
    if os.path.isdir(folder_path):
        # Create a repository on GitHub with the folder name
        repo_name = folder_name.replace(' ', '-')  # Remove spaces in folder name
        user = g.get_user()
        repo = user.create_repo(repo_name)

        # Add the .ipynb file to the repository
        notebook_file = [file for file in os.listdir(folder_path) if file.endswith('.ipynb')]
        if len(notebook_file) == 1:
            notebook_file = notebook_file[0]
            notebook_path = os.path.join(folder_path, notebook_file)
            with open(notebook_path, 'rb') as file_content:
                repo.create_file(notebook_file, f"Initial commit of {notebook_file}", file_content.read())
        else:
            print(f'Error: .ipynb file not found in folder {folder_name}')
            continue

        # Add the images folder to the repository
        img_folder = os.path.join(folder_path, 'img')
        if os.path.exists(img_folder):
            # Upload images to the repository
            for root, dirs, files in os.walk(img_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, img_folder)  # Relative path to the "img" directory
                    # Create directory structure in the remote repository
                    with open(file_path, 'rb') as file_content:
                        repo.create_file("img/"+rel_path, f"Initial commit of img/{rel_path}", file_content.read())
        else:
            print(f'Error: "img" folder not found in folder {folder_name}')

print('Process completed.')
