import tempfile
from pages.feedback_page import FeedbackPage


def test_feedback_form(browser):
    with browser.new_context() as context:
        page = context.new_page()
        feedback_page = FeedbackPage(page)

        page.goto("https://mish-website-2023-public-git-dev-mish-design.vercel.app/")

        feedback_page.fill_name("Тестовый пользователь")
        feedback_page.fill_email("mail@gmail.com")
        feedback_page.fill_phone("1234567890")
        feedback_page.fill_description("Тестовое описание задачи")

        # Создание временного файла с тестовыми данными
        with tempfile.NamedTemporaryFile(delete=False) as file:
            file.write(b'Test file content')
            file_path = file.name

        feedback_page.attach_file(file_path)

        feedback_page.check_agreement()
        feedback_page.submit_form()
        feedback_page.wait_for_success_message()

        context.close()
