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
