from invoke import task

@task
def install(c, tags=None):
    if tags:
        c.run(
            f"ansible-playbook -i inventory --tags {tags} "
            "-K playbooks/bootstrap.yml",
            pty=True
        )
    else:
        c.run(
            "ansible-playbook -i inventory -K playbooks/bootstrap.yml",
            pty=True
        )

@task
def mitmproxy(c, mode='regular'):
    if mode == 'regular':
        c.run(
            f"ansible-playbook -i inventory --tags mitmproxy "
            f"-K -e mitm_proxy_mode={mode} -e mitm_state=unchanged "
            "playbooks/bootstrap.yml",
            pty=True
        )
    elif mode == 'transparent':
        c.run(
            f"ansible-playbook -i inventory --tags mitmproxy "
            f"-K -e mitm_proxy_mode={mode} -e mitm_state=unchanged "
            "playbooks/bootstrap.yml",
            pty=True
        )
