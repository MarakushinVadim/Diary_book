from django import template

register = template.Library()


@register.filter()
def description_filter(description):
    if len(description) > 123:
        return f"{description[:120]}..."
    return description


@register.filter()
def name_filter(name):
    if len(name) > 31:
        return f"{name[:28]}..."
    return name
