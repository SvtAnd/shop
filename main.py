# -*- coding: utf-8 -*-

import os
import web
from web.contrib.template import render_jinja
from jinja2 import Environment,FileSystemLoader

urls = (
    '/index.html', 'index',
    '/products.html', 'products',
    '/contact.html', 'contact',
)

app = web.application(urls, globals())

ROOT = os.path.dirname(__file__)
TEMPLATE = os.path.join(ROOT, 'templates')

# render = web.template.render(TEMPLATE)

# render = render_jinja('templates', encoding = 'utf-8', )
render = render_jinja(TEMPLATE, encoding = 'utf-8')


# def render_template(index1, **context):
#     extensions = context.pop('extensions', [])
#     globals = context.pop('globals', {})
#
#     jinja_env = Environment(
#             loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
#             extensions=extensions,
#             )
#     jinja_env.globals.update(globals)
#
#     #jinja_env.update_template_context(context)
#     return jinja_env.get_template(index1).render(context)


class index:
    def GET(self):
    # You can use a relative path as template name, for example, 'ldap/hello.html'.
        return render.index1()


class products:
    def GET(self):
        return render.products()


class contact:
    def GET(self):
        # return "hello"
        return render.contact()

if __name__ == "__main__":
    app.run()