import os
import shutil
import pip


def main():
    shutil.rmtree(os.path.expanduser('~') + '/{{ cookiecutter.project_slug }}', ignore_errors=True)
    pip.main(["uninstall", '{{ cookiecutter.project_slug }}'])
    os.remove(os.path.expanduser('~') + '/Desktop/{{ cookiecutter.project_slug }}.lnk')


if __name__ == '__main__':
    main()
