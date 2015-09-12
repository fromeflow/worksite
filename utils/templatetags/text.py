from django.template import Library, TemplateSyntaxError
from django.template.defaultfilters import stringfilter
register = Library()


@register.filter
@stringfilter
def mark_to_text(value):
    MARKS = {
        '2': 'неудовлетворительно',
        '3': 'удовлетворительно',
        '4': 'хорошо',
        '5': 'отлично'
    }
    return MARKS.get(value, str(value))


@register.filter
@stringfilter
def plural_ru(value, arg):
    try:
        name1, name2, name5, *_ = arg.split(',')
        value_int = int(value)
        if (value_int // 10 % 10) == 1:
            return name5
        elif 2 <= (value_int % 10) <= 4:
            return name2
        elif value_int % 10 == 1:
            return name1
        else:
            return name5
    except:
        raise TemplateSyntaxError