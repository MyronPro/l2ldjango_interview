from django import template
import datetime

register=template.Library()

@register.filter(name='l2l_dt')
def l2l_dt(val):

    # convert strings to datetime obj
    if isinstance(val, str):
        try:
            # string expected format: %Y-%m-%dT%H:%M:%S
            val = datetime.datetime.strptime(val, '%Y-%m-%dT%H:%M:%S')
        except ValueError:
            return '{INVALID_STRING_FORMAT}'

    return val.strftime('%Y-%m-%d %H:%M:%S')
