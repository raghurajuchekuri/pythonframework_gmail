# Generated steps for Sample

from behave import *

from features.sample.page_model.google_home_page import HomePage

use_step_matcher("re")


@given("I have navigated to google page")
def navigate_to_google_page(context):
    """
    :type context: behave.runner.Context
    """
    home_page = HomePage()
    home_page.navigate(context.current_config['base_url'])

@when('I enter "python" in search box')
def enter_text_to_search(context):
    """
    :type context: behave.runner.Context
    """
    home_page = HomePage()
    home_page.search("chandra")


@then("I should see search results")
def verify_search_results(context):
    """
    :type context: behave.runner.Context
    """
    home_page = HomePage()
    assert home_page.element_visible
