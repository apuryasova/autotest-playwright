from playwright.sync_api import Page

class FeedbackPage:
    def __init__(self, page: Page):
        self.page = page

    def fill_name(self, name: str):
        self.page.fill('input[name="name"]', name)

    def fill_email(self, email: str):
        self.page.fill('input[name="email"]', email)

    def fill_phone(self, phone: str):
        self.page.fill('input[name="phone"]', phone)

    def fill_description(self, description: str):
        self.page.fill('textarea[name="desc"]', description)

    def attach_file(self, file_path: str):
        self.page.set_input_files('input[type="file"]', file_path)

    def check_agreement(self):
        self.page.check('input#checkbox')

    def submit_form(self):
        self.page.click('button:has-text("Отправить")')

    def wait_for_success_message(self):
        self.page.wait_for_selector('h3.ActionCard_GoodTitle:has-text("Рады познакомиться")')