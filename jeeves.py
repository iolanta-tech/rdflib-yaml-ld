import sh


def update_submodule():
    """Update the version of Lineage submodule."""
    submodule = sh.git.submodule

    submodule.sync()
    submodule.update('--init', '--recursive', '--remote')
