from core.common.cpanel.locators.dashboard_page import DashboardPageLocators as DPL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import core


class CPanelDashboard:

    def __init__(self):
        self.driver = core.get(core.res['chrome'], feature="browser")._res.driver.webdriver

    TIME_SEC = 3

    def check_page(self, pagetitle=""):
        """
        This method checks if the page you have arrived on is the one you are looking for

        args:
            pagetitle: insert title of the page (text from H1 tag)

        returns:
            true or failure message below
        """

        WebDriverWait(self.driver, self.TIME_SEC).until(EC.presence_of_element_located(DPL.PAGE_TITLE))
        title = self.driver.find_element(*DPL.PAGE_TITLE).text
        assert title == pagetitle, \
            'Access failed, the page  <<' + pagetitle + '>> is not displayed'

    # navigate SETUP menu

    def expand_setup(self):
        """Method to expand Setup menu in CPANEL

        returns:
            menu expands to display submenus

        All access to submenu items are captured in the methods below
        """
        self.driver.find_element(*DPL.M_SETUP).click()

    def access_products_submenu(self):
        self.driver.find_element(*DPL.SM_PRODUCTS).click()
        self.check_page('Products')

    def access_fulfillments_menu(self):
        self.driver.find_element(*DPL.SM_FULFILLMENT).click()
        self.check_page('Electronic delivery')

    def access_pricelists(self):
        self.driver.find_element(*DPL.SM_PRICE_LISTS).click()
        self.check_page('Price lists')

    def access_renewal(self):
        self.driver.find_element(*DPL.SM_RENEWAL).click()
        self.check_page('Subscriptions - System overview')

    def access_generatelinks(self):
        self.driver.find_element(*DPL.SM_GENERATE_LINKS).click()
        self.check_page('Checkout links')

    def access_interface_templates(self):
        self.driver.find_element(*DPL.SM_INTERFACE_TEMPLATES).click()
        self.check_page('Interface templates')

    def access_ordering_options(self):
        self.driver.find_element(*DPL.SM_ORDERING_OPTIONS).click()
        self.check_page('Ordering options')

    def access_partner_invoice_settings(self):
        self.driver.find_element(*DPL.SM_PARTNER_INVOICE_SETTINGS).click()
        self.check_page('Partner invoice settings')

    def access_media_center(self):
        self.driver.find_element(*DPL.SM_MEDIA_CENTER).click()
        self.check_page('Media center')

    # navigate MARKETING TOOLS menu

    def expand_marketing_tools(self):
        """Method to expand Accounting menu in CPANEL

            returns:
                menu expands to display submenus

        All access to submenu items are captured in the methods below
        """
        self.driver.find_element(*DPL.M_MARKETING_TOOLS).click()

    def access_overview_menu(self):
        self.driver.find_element(*DPL.SM_OVERVIEW).click()
        self.check_page('Marketing tools')

    def access_promotions(self):
        self.driver.find_element(*DPL.SM_PROMOTIONS).click()
        self.check_page('Regular promotions')

    def access_cross_selling(self):
        self.driver.find_element(*DPL.SM_CROSS_SELLING).click()
        self.check_page('Cross-selling campaigns')

    def access_upselling(self):
        self.driver.find_element(*DPL.SM_UPSELLING).click()
        self.check_page('Upselling')

    def access_retention_tools(self):
        self.driver.find_element(*DPL.SM_RETENTION_TOOLS).click()
        self.check_page('Auto-renewal enrollment')

    def access_email_marketing(self):
        self.driver.find_element(*DPL.SM_EMAIL_MARKETING).click()
        self.check_page('Email marketing program')

    def access_lead_mgmt(self):
        self.driver.find_element(*DPL.SM_LEAD_MANAGEMENT).click()
        self.check_page('Manage your leads')

    def access_ab_testing(self):
        self.driver.find_element(*DPL.SM_AB_TESTING).click()
        self.check_page('A/B testing overview')

    def access_email_editor(self):
        self.driver.find_element(*DPL.SM_EMAIL_EDITOR).click()
        self.check_page('Email editor')

    def access_channel_resources(self):
        self.driver.find_element(*DPL.SM_CHANNEL_RESOURCES).click()
        self.check_page('Affiliate marketing resources')

    # navigate Affiliate network menu

    def expand_affiliate_network(self):
        """Method to expand Affiliate Network menu in CPANEL

        returns:
            menu expands to display submenus

        All access to submenu items are captured in the methods below
        """
        self.driver.find_element(*DPL.M_AFFILIATE_NETWORK).click()

    def access_settings(self):
        self.driver.find_element(*DPL.SM_SETTINGS).click()
        self.check_page('Open the affiliates sales channel')

    def access_relationships(self):
        self.driver.find_element(*DPL.SM_RELATIONSHIPS).click()
        self.check_page('Relationships')

    def access_build_your_network(self):
        self.driver.find_element(*DPL.SM_BUILD_YOUR_NETWORK).click()
        self.check_page('Affiliates sign-up links')

    def access_newsletter(self):
        self.driver.find_element(*DPL.SM_NEWSLETTER).click()
        self.check_page('Affiliate newsletter management')

    def access_bonus_programs(self):
        self.driver.find_element(*DPL.SM_BONUS_PROGRAMS).click()
        self.check_page('Bonus programs')

    # navigate Partner management menu

    def expand_partner_management(self):
        """Method to expand Partner Management menu in CPANEL

        returns:
            menu expands to display submenus

        All access to submenu items are captured in the methods below
        """
        self.driver.find_element(*DPL.M_PARTNER_MANAGEMENT).click()

    def access_partners(self):
        self.driver.find_element(*DPL.SM_PARTNERS).click()
        self.check_page('Partners')

    def access_partnership_programs(self):
        self.driver.find_element(*DPL.SM_PARTNERSHIP_PROGRAMS).click()
        self.check_page('Partnership programs')

    # navigate Orders customers menu

    def expand_orders_customers(self):
        """Method to expand Orders and Customers menu in CPANEL

        returns:
            menu expands to display submenus

        All access to submenu items are captured in the methods below
        """
        self.driver.find_element(*DPL.M_ORDERS_CUSTOMERS).click()

    def access_order_search(self):
        self.driver.find_element(*DPL.SM_ORDER_SEARCH).click()
        self.check_page('Order search')

    def access_place_partner_order(self):
        self.driver.find_element(*DPL.SM_PLACE_PARTNER_ORDER).click()
        self.check_page('Place partner order')

    def access_fulfillment_confirmations(self):
        self.driver.find_element(*DPL.SM_FULFILLMENT_CONFIRMATIONS).click()
        self.check_page('Fulfillment confirmations')

    def access_partner_invoices(self):
        self.driver.find_element(*DPL.SM_PARTNER_INVOICES).click()
        self.check_page('Partner invoices')

    def access_customers(self):
        self.driver.find_element(*DPL.SM_CUSTOMERS).click()
        self.check_page('Customers')

    def access_subscriptions(self):
        self.driver.find_element(*DPL.SM_SUBSCRIPTIONS).click()
        self.check_page('Subscriptions management')

    def access_refunds(self):
        self.driver.find_element(*DPL.SM_REFUNDS).click()
        self.check_page('Refunds')

    # navigate Integrations menu

    def expand_integrations(self):
        """Method to expand Integrations menu in CPANEL

        returns:
            menu expands to display submenus

        All access to submenu items are captured in the methods below
        """
        self.driver.find_element(*DPL.M_INTEGRATIONS).click()

    def access_webhooks_api(self):
        self.driver.find_element(*DPL.SM_WEBHOOKS_API).click()
        self.check_page('Webhooks & API')

    def access_salesforce_integration(self):
        self.driver.find_element(*DPL.SM_SALESFORCE_INTEGRATION).click()
        self.check_page('Salesforce integration')

    def access_apps_plugins(self):
        self.driver.find_element(*DPL.SM_APPS_PLUGINS).click()
        self.check_page('Apps & plugins')

    # navigate Reports center menu

    def expand_reports_center(self):
        """Method to expand Reports Center menu in CPANEL

        returns:
            menu expands to display submenus

        All access to submenu items are captured in the methods below
        """
        self.driver.find_element(*DPL.M_REPORTS_CENTER).click()

    def access_main_reports(self):
        self.driver.find_element(*DPL.SM_MAIN_REPORTS).click()
        self.check_page('Main reports')

    def access_custom_reports(self):
        self.driver.find_element(*DPL.SM_CUSTOM_REPORTS).click()
        self.check_page('Custom reports')

    def access_users_activity(self):
        self.driver.find_element(*DPL.SM_USERS_ACTIVITY).click()
        self.check_page('Users activity')

    def access_authorization_report(self):
        self.driver.find_element(*DPL.SM_AUTHORIZATION_REPORT).click()
        self.check_page('Authorization report')

    def access_api_webhooks(self):
        self.driver.find_element(*DPL.SM_API_WEBHOOKS).click()
        self.check_page('API & Webhooks')

    # navigate Accounting menu

    def expand_accounting(self):
        """Method to expand Accounting menu in CPANEL

        returns:
            menu expands to display submenus

        All access to submenu items are captured in the methods below
        """
        self.driver.find_element(*DPL.M_ACCOUNTING).click()

    def access_estimated_balance(self):
        self.driver.find_element(*DPL.SM_ESTIMATED_BALANCE).click()
        self.check_page('Estimated balance')

    def access_payments(self):
        self.driver.find_element(*DPL.SM_PAYMENTS).click()
        self.check_page('Accounting summary')

    def access_finance_documents(self):
        self.driver.find_element(*DPL.SM_FINANCE_DOCUMENTS).click()
        self.check_page('Period net sales')
