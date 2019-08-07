
mandatory_attributtes = {
        'Unix': ['ip', 'user', 'password'],
        'Website': ['ip', 'browser'],
        'Mysql': ['ip', 'user', 'password'],
    }


class GenericResource:
    """Generic resource class to represent any resource used in automation"""
    def __init__(self, resource_info):
        """Initialize resource. Takes every top level key passed in the dictionary of the resource inside the testbed
        YAML file and makes it into an attribute of the resource object, except for - config

        If the 'config' key is present, its contents are pulled out and made direct attributes of resource object.

        Finally, if items in lists under 'config' have a 'role', or 'name', or 'device' attribute, those lists are
        converted into dictionaries for easy access.

        args:
            :res_info: Dict info about the resource
        """
        if 'type' not in resource_info:
            raise ValueError(f"'type' key is not provided for resource needed for resource - {resource_info['role']}")
        resource_info.setdefault('password', None)
        resource_info.setdefault('cookies', None)
        resource_info.setdefault('product_hint', None)

        if resource_info['type'] in mandatory_attributtes:
            for attribute in mandatory_attributtes[resource_info['type']]:
                if attribute not in resource_info:
                    raise ValueError(f"Mandatory key '{attribute}' not provided for resource - {resource_info['role']}")

        for key, value in resource_info.items():
            setattr(self, str(key), value)
        self.connected = False
        # self.version = GenericVersion(self.role, res_info.get('version', "1.0.0"))
        # self.version_info = {}

        self.bootstrap()

    def bootstrap(self):
        """Abstract method that must be implemented fully inside a real resource class"""
        pass

