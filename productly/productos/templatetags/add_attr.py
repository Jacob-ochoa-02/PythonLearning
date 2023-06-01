from django import template
register = template.Library()   # Nos creará un decorador para poder registrar este filtro

@register.filter(name="add_attr")
def add_attr(field,css):
    attrs = {}
    clase, valor = css.split(':')
    attrs[clase] = valor
    return field.as_widget(attrs=attrs)  # Este método recibe el argumento nombrado de atribute
