# Git

This role is designed to provide a repeatable way for installing git and configuring it with a few customisations.
 
## Requirements

If you run ansible in a virtualenv ensure you have the system package python-apt installed and you use the --system-site-packages flag to make sure the required apt module is available.

* python-apt 

## Role Variables

* `git_global_config`: ($HOME/.gitconfig) The default gitconfig that is used when the global flag is set.
* `git_user_name` The name to use for commit messages.
* `git_user_email` The email to use for commit messages.

## Dependencies

No dependencies on other roles.

## Example Playbook

Simple use case, installs the configuration on all hosts in servers. Can also be run against localhost for convenience. See `tests/main.yml` for examples.

    - hosts: servers
      roles:
         - git

## Testing

### With docker

```
$ docker build -f tests/Dockerfile .
```

### Without docker

Requires sudo to install git. Ensure you use `-K` to ask for the sudo password or have it provided via other means.

```
$ ansible-playbook tests/main.yml --syntax-check
$ ansible-playbook tests/main.yml --check
```

## License

BSD

## Author Information

mjohno
