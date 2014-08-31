from django import template

register = template.Library()


@register.filter(name='mark_to_text')
def mark_to_text(value):
    MARKS = {
        2: 'неудовлетворительно',
        3: 'удовлетворительно',
        4: 'хорошо',
        5: 'отлично'
    }
    return MARKS.get(value, str(value))