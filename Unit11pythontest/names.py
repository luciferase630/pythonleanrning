def get_formatted_name(first , last , mid=''):
    """Generate a neatly formatted full name"""
    if mid:
        full_name = first + ' '+mid+' ' + last
    else:full_name=first+" "+last
    return full_name.title()
