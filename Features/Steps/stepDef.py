from behave import given, when, then
from Utility.browser_setup import BrowserSetup
from Pages.inputPage import InputPage
from Pages.resultPage import ResultPage

@given("I launch the Agrichain input page")
def launch_browser(context):
    context.driver = BrowserSetup().get_driver()
    context.input_page = InputPage(context.driver)

@when('I enter "{text}" in the input field')
def enter_text(context, text):
    context.input_page.enter_text(text)

@when("I click the submit button")
def click_submit(context):
    context.input_page.click_submit()

@then('I should see the output "{expected_output}" on the result page')
def verify_output(context, expected_output):
    context.result_page = ResultPage(context.driver)
    assert context.result_page.get_output_text() == expected_output, "Output mismatch!"

def after_scenario(context, scenario):
    context.driver.quit()
