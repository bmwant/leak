INIT_FILE = './leak/__init__.py'


def main():
    with open(INIT_FILE) as f:
        content = f.readlines()

    version_line = content[0]
    _, version = version_line.split('=')
    version = version.strip()[1:-1]  # Remove quotes around version
    major, minor, patch = version.split('.')
    new_patch = int(patch) + 1
    new_version = '{major}.{minor}.{patch}'.format(major=major,
                                                   minor=minor,
                                                   patch=new_patch)
    new_version_line = "__version__ = '{new_version}'\n".format(new_version=new_version)

    content[0] = new_version_line
    with open(INIT_FILE, 'w') as f:
        f.writelines(content)

    print('Version bumped to %s' % new_version)

if __name__ == '__main__':
    main()
