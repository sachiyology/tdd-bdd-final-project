######################################################################
# Copyright 2016, 2021 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
######################################################################

# pylint: disable=function-redefined, missing-function-docstring
# flake8: noqa
"""
Web Steps

Steps file for web interactions with Selenium

For information on Waiting until elements are present in the HTML see:
    https://selenium-python.readthedocs.io/waits.html
"""
######################################################################
# Web Steps for BDD UI Tests
######################################################################
import logging
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

logger = logging.getLogger(__name__)

######################################################################
# VISIT PAGES
######################################################################
@when('I visit the "Home Page"')
def step_impl(context):
    """Navigate to the home page"""
    context.browser.get(context.base_url)


######################################################################
# PAGE VALIDATION
######################################################################
@then('I should see "{text}" in the title')
def step_impl(context, text):
    """Check the page title"""
    assert text in context.browser.title


@then('I should see "{text}" on the page')
def step_impl(context, text):
    """Check that text appears somewhere on the page"""
    assert text in context.browser.page_source


######################################################################
# FORM INPUT
######################################################################
@when('I set the "{field}" to "{value}"')
def step_impl(context, field, value):
    """Enter text into an input field"""
    element = context.browser.find_element(By.NAME, field)
    element.clear()
    element.send_keys(value)


######################################################################
# BUTTON ACTION
######################################################################
@when('I press the "{button}" button')
def step_impl(context, button):
    """Click a button"""
    btn = context.browser.find_element(By.XPATH, f"//button[text()='{button}']")
    btn.click()


######################################################################
# DROPDOWN SELECTION
######################################################################
@when('I select "{value}" in the "{field}" dropdown')
def step_impl(context, value, field):
    """Select value from dropdown"""
    select = Select(context.browser.find_element(By.NAME, field))
    select.select_by_visible_text(value)


######################################################################
# CHECKBOX
######################################################################
@when('I check "{field}"')
def step_impl(context, field):
    """Check a checkbox"""
    checkbox = context.browser.find_element(By.NAME, field)
    if not checkbox.is_selected():
        checkbox.click()


######################################################################
# RESULTS VALIDATION
######################################################################
@then('I should see "{name}" in the results')
def step_impl(context, name):
    """Verify item appears in results"""
    assert name in context.browser.page_source


@then('I should not see "{name}" in the results')
def step_impl(context, name):
    """Verify item does not appear in results"""
    assert name not in context.browser.page_source