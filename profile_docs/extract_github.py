import requests

username = "Vinylango25"
output_file = "github_data.txt"

response = requests.get(f"https://api.github.com/users/{username}/repos")
repos = response.json()

with open(output_file, "w") as f:
    for repo in repos:
        f.write(f"# {repo['name']}\n")
        description = repo.get("description") or ""
        f.write(description + "\n\n")
        readme_url = f"https://raw.githubusercontent.com/{username}/{repo['name']}/main/README.md"
        r = requests.get(readme_url)
        if r.status_code == 200:
            f.write(r.text + "\n\n")
