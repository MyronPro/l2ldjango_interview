from django import template
import datetime

register=template.Library()

@register.filter(name='l2l_dt')
def l2l_dt(val):
    try:
        # convert strings to datetime obj
        if isinstance(val, str):
            try:
                # string expected format: %Y-%m-%dT%H:%M:%S
                val = datetime.datetime.strptime(val, '%Y-%m-%dT%H:%M:%S')
            except ValueError:
                return '{INVALID_STRING_FORMAT}'

        #return datetime obj in %Y-%m-%d %H:%M:%S format
        return val.strftime('%Y-%m-%d %H:%M:%S')

    except AttributeError:
        return '{INVALID_DATA_TYPE}'

    except Exception as e:
        print(e)
        return '{ERROR}'
