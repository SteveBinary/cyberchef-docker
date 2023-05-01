# cyberchef-docker

[CyberChef by GCHQ](https://github.com/gchq/CyberChef) is the Cyber Swiss Army Knife. [Most of its features](https://github.com/gchq/CyberChef#features) are executed completely on the client, eliminating most privacy concerns. With this Docker image you can go a step further and self-host CyberChef, localy or on a server, for offline usage and even more privacy.

The Docker image is available for the `linux/amd64` and `linux/arm64` architectures.
[Here](https://github.com/SteveBinary/cyberchef-docker/pkgs/container/cyberchef) you can find more about the available versions and architectures.

[Visit the CyberChef project](https://github.com/gchq/CyberChef#cyberchef) for the documentation of the app.

## Installation

Note that the internal port is `8080`.

### Via `docker run`

```shell
docker run --name CyberChef -p 8080:8080 -d ghcr.io/stevebinary/cyberchef:latest
```

### Via `docker compose`

```yml
version: "3.7"

services:
  cyberchef:
    image: ghcr.io/stevebinary/cyberchef:latest
    container_name: CyberChef
    restart: unless-stopped
    ports:
      - 8080:8080
```

```shell
docker compose up -d
```
