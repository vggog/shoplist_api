from jinja2 import Environment, PackageLoader, select_autoescape


class TemplateEngine:
    env = Environment(
        loader=PackageLoader('src'),
        autoescape=select_autoescape(),
    )

    def render_html(self, html: str, **kwargs) -> str:
        template = self.env.get_template(html)

        return template.render(**kwargs)
