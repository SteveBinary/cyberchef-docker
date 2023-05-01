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

    current_version = str(content["tag_name"])

    desired_asset_file_name = f"CyberChef_{current_version}.zip"
    downloadable_assets = list(filter(lambda asset: str(asset["browser_download_url"]).endswith(desired_asset_file_name), content["assets"]))

    if len(downloadable_assets) == 0:
        exit_with_error(f"No downloadable asset found ('browser_download_url' must end with '{desired_asset_file_name}')")

    download_url = str(downloadable_assets[0]["browser_download_url"])

    print(download_url, sep="")
