from django import template

register = template.Library()

@register.filter(name='censor')
def censor(value):
    words_to_censor = ['badword1', 'badword2']  # Add words you want to censor
    for word in words_to_censor:
        value = value.replace(word, '*' * len(word))
    return value
