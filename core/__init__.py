import os
import yaml
import logging
from importlib import import_module
from core.resources import get_resource

PACKAGE = 'core'
CONTAINER = 'modules'

DEFAULT_CONFIG_PATH = "default_config.yaml"

res = {}


def load_custom_config(config_path):
    default_config = load_yaml(DEFAULT_CONFIG_PATH)
    custom_config = load_yaml(config_path)
    default_config.update(custom_config)

    if not os.path.exists(default_config['screenshots']):
        os.makedirs(default_config['screenshots'], 0o775)
    return default_config


def load_yaml(yaml_file=DEFAULT_CONFIG_PATH):
    with open(yaml_file) as f:
        content = yaml.safe_load(f)
    return content


def get(resource, feature):
    """Get implements the orchestration logic to look up a feature based on the os version/type of the given resource.

    args:
        :res: Device abstraction for the resource.
        :feature: Name of the feature requested for the resource in string form.

    returns:
        :actor: An instance of the Feature class implemented for the requested feature

    """
    resource.bootstrap()

    path = '.'.join([PACKAGE, CONTAINER, feature])

    importer = Importer()

    try:
        importer.import_mod(path)
        feature_class = importer.fetch_attribute(feature.split('.')[-1].title())
        instance = feature_class(resource, path, feature)
    except ImportError as err:
        raise FeatureNotFound(err, feature)
    except AttributeError as err:
        raise FeatureClassNotFound(err, feature)
    else:
        logging.debug(f"Feature class '{instance.__class__}' initialized")

    return instance


class FeatureNotFound(Exception):
    def __init__(self, err, feature):
        err_msg = f"feature {feature} not found: {err}"
        super(FeatureNotFound, self).__init__(err_msg)


class FeatureClassNotFound(Exception):
    def __init__(self, err, feature):
        err_msg = f"feature class for feature {feature} not found: {err}"
        super(FeatureClassNotFound, self).__init__(err_msg)


class Importer:
    """Importer defines the interface to import a module dynamically, and fetch callable attributes from it.
    """
    def __init__(self, module=None):
        """Initializes the Importer object.

        Kwargs:
            :module: full module path of type string, specified as a python package - a.b.c.d
        """
        self._module = module
        self.imported = None

    def import_mod(self, module):
        """Instance method imports the module dynamically using the builtin import_module.

        Kwargs:
            :module (str): full module path specified as a python package - a.b.c.d

        Raises:
            :ImportError: in the event the module cannot be imported.
        """
        self._module = module
        try:
            self.imported = import_module(module)
        except ImportError:
            raise

    def fetch_attribute(self, attrib):
        """Instance method looks up an imported module for the requested attribute using getattr.

        Args:
            :attrib: callable attribute name of type string, within the imported module

        Returns:
            :callable_attrib: callable form of the attribute.

        Raises:
            :AttributeError: in the event the attribute cannot be fetched from the imported module.
            :TypeError: in the event the attribute fetched cannot be called.
        """
        try:
            callable_expr = getattr(self.imported, attrib)
        except AttributeError:
            raise
        else:
            if not callable(callable_expr):
                raise TypeError(f"{callable_expr} attribute is not callable!")
            return callable_expr
