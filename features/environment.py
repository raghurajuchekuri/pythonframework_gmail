import core
import time

from core.resources import get_resource
from core import DEFAULT_CONFIG_PATH, load_custom_config
CURRENT_CONFIG = {}

resources = {}


def create_resources(resources_dict):
    res = {}
    for role, res_info in resources_dict.items():
        res_info['role'] = role
        res[role] = get_resource(res_info)
    return res


def before_all(context):
    global CURRENT_CONFIG
    global resources

    config_file = context.config.userdata.get('profile', DEFAULT_CONFIG_PATH)
    if config_file != DEFAULT_CONFIG_PATH:
        config_file += "_config.yaml"
    CURRENT_CONFIG = load_custom_config(config_file)
    if 'resources' not in CURRENT_CONFIG:
        raise ValueError("Resources not given in yaml config file")
    resources = create_resources(CURRENT_CONFIG['resources'])
    core.res = dict(resources)
    context.browser = core.get(resources['chrome'], feature="browser")
    context.browser._res.open_browser_window(browser='chrome')


def before_scenario(context, scenario):
    context.current_config = CURRENT_CONFIG


def after_scenario(context, scenario):
    context.browser = core.get(resources['chrome'], feature="browser")
    if scenario.status == "failed":
        context.browser._res.screenshot(f"/{scenario.name}_{time.strftime('%d-%m-%Y_%H-%M-%S')}.png")
    context.browser._res.restart_driver()


def after_all(context):
    context.browser._res.quit()
