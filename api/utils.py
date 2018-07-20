
def truncate_string(string, count=25):
    return string[:count] + (string[count:] and '...')