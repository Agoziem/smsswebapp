from django import template

register = template.Library()

@register.filter
def split(value, arg):
    """
    Split the value by the argument and return the list.
    Usage: {{ value|split:" " }}
    """
    return value.split(arg)

@register.filter
def get_first_name(value):
    """
    Split the full name by space and return the first name.
    Usage: {{ full_name|get_first_name }}
    """
    if value:
        return value.split()[0] if value.split() else value
    return value

@register.filter
def get_last_name(value):
    """
    Split the full name by space and return the last name.
    Usage: {{ full_name|get_last_name }}
    """
    if value:
        parts = value.split()
        if len(parts) > 1:
            return parts[-1]
        return ""
    return value

@register.filter
def first_letter(value):
    """
    Return the first letter of a string.
    Usage: {{ name|first_letter }}
    """
    if value:
        return value[0].upper() if value else ""
    return ""

@register.filter
def initials(value):
    """
    Return the initials of a full name.
    Usage: {{ full_name|initials }}
    """
    if value:
        parts = value.split()
        return ''.join(part[0].upper() for part in parts if part)
    return ""
