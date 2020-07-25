# Vim

[![Build Status](https://travis-ci.org/mjohno/vim.svg?branch=master)](https://travis-ci.org/mjohno/vim)

This role is designed to create a repeatable set up for my vim enviornment. This includes installing a vimrc file, the pathogen plugin manager and the python-mode plugin.

## Requirements

If you run ansible in a virtualenv ensure you have python-apt installed and you use the --system-site-packages flag to make sure the required apt module is available.

* python-distutils-extra
* python-apt 
* git

## Role Variables

* `vim_root` ($HOME/.vim) The default .vim directory that is understood by most.
* `vim_autoload` (`vim_root`/autoload) Pathogen gets loaded from here.
* `vim_bundle` (`vim_root`/bundle) Pathogen plugins get stored here.
* `vim_ftdetect` (`vim_root`/ftdetect) All filetype extension detection config goes here.
* `vim_ftplugin` (`vim_root`/ftplugin) All filetype based vim config goes in here.

## Dependencies

No dependencies on other roles.

## Example Playbook

Simple use case, installs the configuration on all hosts in servers. Can also be run against localhost for convenience. See `tests/main.yml` for examples.

    - hosts: servers
      roles:
         - vim

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
