import logging
from core.resources.resource import GenericResource
from core.resources.unix import Unix
from core.resources.web import Website
from core.resources.database import Database


def get_resource(res_info):
    """A factory like method that takes dictionary info containing certain vital keys and returns a compatible resource
    object. If no compatible resource is found, a basic GenericResource is returned.

    args:
       :res_info: Dict of info about the resource
    """
    if 'type' not in res_info:
        raise ValueError(f"Mandatory key 'type' not provided for resource - {res_info['role']}")

    try:
        res = globals()[res_info['type']](res_info)
    except KeyError:
        logging.info(f"No matching resource class type found for {res_info['role']}. Providing generic resource.")
        res = GenericResource(res_info)

    return res
