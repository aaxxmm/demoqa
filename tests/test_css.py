from pages.text_box import TextBox


def test_text_box_submit(browser):
    demo_page = TextBox(browser)
    demo_page.visit()
    demo_page.submit_btn.check_css('color', 'rgba(255, 255, 255, 1')
    demo_page.submit_btn.check_css('backgroundColor', 'rgba(73, 80, 87, 1')
    demo_page.submit_btn.check_css('borderColor', 'rgb(0, 123, 255')