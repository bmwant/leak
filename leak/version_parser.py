from leak import logger


def versions_split(version_str, type_applyer=int):
    dots_count = version_str.count('.')
    if dots_count == 0:
        major, minor, patch = version_str, 0, 0
    elif dots_count == 1:
        major, minor = version_str.split('.')
        patch = 0
    elif dots_count == 2:
        major, minor, patch = version_str.split('.')
    else:
        logger.debug('Incorrect version "%s". Move to bottom when sorting' % version_str)
        major, minor, patch = 0, 0, 0

    return map(type_applyer, (major, minor, patch))
