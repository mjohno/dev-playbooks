# docker-bootstrap

[![Build Status](https://travis-ci.org/mjohno/docker-bootstrap.svg?branch=master)](https://travis-ci.org/mjohno/docker-bootstrap)

This role sets up the docker-ce repository for my dev machine. A role implementation of the [docker installation instructions](https://docs.docker.com/engine/installation/linux/ubuntu/).

## Requirements

None

## Role Variables

* `docker_bs_key_url`: The URL where to download the docker repository key.
* `docker_bs_apt_repo`: The docker repository URL where the package is available.
* `docker_bs_fingerprint`: The fingerprint to validate the key.

## Dependencies

None

## Example Playbook

See tests/main.yml. This role should be able to be run standalone.

    - hosts: servers
      roles:
         - docker-bootstrap

## Testing

### With docker

```
$ docker build -f tests/Dockerfile .
```

### Without docker

Requires sudo to install vim. Ensure you use `-K` to ask for the sudo password or have it provided via other means.

```
$ ansible-playbook tests/main.yml --syntax-check
$ ansible-playbook tests/main.yml --check
```

## License

BSD

## Author Information

Matthew Johnson
