from flask import Blueprint
from flask.helpers import _PackageBoundObject


class Router(Blueprint):
    def __init__(self, path, import_name):
        _PackageBoundObject.__init__(self, import_name, template_folder=None, root_path=None)

        path_split = path.split('/')
        root_path = path
        name = path_split[-1]
        super(Router, self).__init__(name, import_name, static_folder=None, static_url_path=None, template_folder=None,
                                     url_prefix=None, subdomain=None, url_defaults=None, root_path=root_path)

    def route(self, rule, **options):
        def decorator(f):
            endpoint = options.pop("endpoint", f.__name__)
            new_rule = self.root_path + rule
            self.add_url_rule(new_rule, endpoint, f, **options)
            return f
        return decorator
