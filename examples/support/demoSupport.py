
def isOffChipForTesting():
    import sys
    computerPlatforms = ['win', 'linux', 'msys', 'os2', 'bsd']
    for platform in computerPlatforms:
        if sys.platform.count(platform) > 0:
            return True
    return False
