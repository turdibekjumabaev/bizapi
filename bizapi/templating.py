from .globals import template_environment


def render_template(template: str, *args, **kwargs) -> str:
    if args:
        context = args[0] if isinstance(args[0], dict) else {}
    else:
        context = kwargs

    return template_environment.get_template(template).render(**context)
