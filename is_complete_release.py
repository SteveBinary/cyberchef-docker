import sys
import requests


CYBER_CHEF_RELEASE_API_URL = "https://api.github.com/repos/gchq/CyberChef/releases/latest"


def exit_with_error(message: str):
    print(message, flush=True, file=sys.stderr)
    exit(1)


if __name__ == "__main__":
    response = requests.get(CYBER_CHEF_RELEASE_API_URL)

    if not response.ok:
        exit_with_error(f"ERROR: Could not retreive current release information from the API (status_code={response.status_code})!")

    content = response.json()

    is_draft = bool(content["draft"])
    is_pre_release = bool(content["prerelease"])

    if is_draft or is_pre_release:
        print("no", sep="")  # the release is not a complete one
    else:
        print("yes", sep="")  # the release is complete
