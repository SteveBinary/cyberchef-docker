import sys
import requests


CYBER_CHEF_RELEASE_API_URL = "https://api.github.com/repos/gchq/CyberChef/releases/latest"


def exit_with_error(message: str):
    print(f"ERROR: {message}", flush=True, file=sys.stderr)
    exit(1)


if __name__ == "__main__":
    response = requests.get(CYBER_CHEF_RELEASE_API_URL)

    if not response.ok:
        exit_with_error(f"Could not retreive current release information from the API (status_code={response.status_code})!")

    content = response.json()

    current_version = str(content["tag_name"]).removeprefix("v")

    print(current_version, sep="")
