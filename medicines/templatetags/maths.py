from django import template

register = template.Library()


@register.filter(name="mul")
def mul(value, arg):
    """Multiply two values in templates.

    Example: {{ price|mul:quantity }}
    """
    try:
        return int(value) * int(arg)
    except (TypeError, ValueError):
        try:
            return float(value) * float(arg)
        except (TypeError, ValueError):
            return 0

