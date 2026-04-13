import pytest
from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect

scenarios('../add_to_cart.feature')

@given("I open the Flipkart website")
def open_flipkart(page):
    page.goto("https://www.flipkart.com")
    # Close login popup if it appears
    try:
        page.locator("button._2KpZ6l._2doB4z").click(timeout=3000)
    except:
        pass

@when('I search for "iPhone 15"')
def search_item(page):
    page.locator("input.Pke_EE").fill("iPhone 15")
    page.keyboard.press("Enter")

@when("I click on the first product")
def click_first_product(page):
    page.locator("div._1AtVbE").first.click()
    # Switch to new tab that opens
    page.wait_for_timeout(2000)

@when("I click Add to Cart button")
def click_add_to_cart(page):
    # Handle new tab
    pages = page.context.pages
    new_page = pages[-1]
    new_page.locator("button._2KpZ6l.HQ8yph").click()

@then("the item should be added to cart successfully")
def verify_cart(page):
    pages = page.context.pages
    new_page = pages[-1]
    cart_count = new_page.locator("span.countNew")
    assert cart_count.is_visible(), "Cart count not updated"