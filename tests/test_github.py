import allure
from selene.support.shared import browser
from selene import have, be, by
from allure_commons.types import Severity

@allure.label("owner", "pavel-go")
@allure.tag('web', 'autotest', 'regression')
@allure.story('STR-665')
@allure.description('Проверка наличия во вкладке Issues ишью с конкретным номером')
@allure.severity(Severity.BLOCKER)
def test_find_specific_issue():
    browser.open('https://github.com/')

    browser.element('[name=q]').click().type('eroshenkoam/allure-example')
    browser.element('[name=q]').press_enter()
    browser.element(by.partial_link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()

    browser.element('#issue_81').should(be.existing).should(be.visible)
    browser.element('#issue_81').should(have.text('#81'))


def test_find_specific_issue_with_dynamic_steps():
    allure.dynamic.label("owner", "pavel-go")
    allure.dynamic.tag('web', 'autotest', 'double')
    allure.dynamic.story('STR-666')
    allure.dynamic.description('Перепроверка наличия во вкладке Issues ишью с конкретным номером')
    allure.dynamic.severity(Severity.CRITICAL)
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com/')

    with allure.step('Запускаем поиск по названию репозитория'):
        browser.element('[name=q]').click().type('eroshenkoam/allure-example')
        browser.element('[name=q]').press_enter()

    with allure.step('Выбираем нужный репозиторий из результатов поиска'):
        browser.element(by.partial_link_text('eroshenkoam/allure-example')).click()

    with allure.step('Переходим на вкладку Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверяем что в списке присутствует issue #81'):
        browser.element('#issue_81').should(be.existing).should(be.visible)
        browser.element('#issue_81').should(have.text('#81'))


@allure.label("owner", "pavel-go")
@allure.tag('web', 'autotest', 'triple')
@allure.story('STR-667')
@allure.description('Переперепроверка наличия во вкладке Issues ишью с конкретным номером')
@allure.severity(Severity.NORMAL)
def test_find_specific_issue_with_lambda_steps():
    open_main_page('https://github.com/')
    search_for_repo('eroshenkoam/allure-example')
    select_from_search_results('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_specific_number(80)

@allure.step('Открываем главную страницу: {link}')
def open_main_page(link):
    browser.open(link)


@allure.step('Запускаем поиск по названию репозитория: {repo}')
def search_for_repo(repo):
    browser.element('[name=q]').click().type(repo)
    browser.element('[name=q]').press_enter()


@allure.step('Выбираем нужный репозиторий из результатов поиска')
def select_from_search_results(repo):
    browser.element(by.partial_link_text(repo)).click()


@allure.step('Переходим на вкладку Issues')
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('Проверяем что в списке присутствует issue #{number}')
def should_see_issue_with_specific_number(number):
    browser.element(f'#issue_{number}').should(be.existing).should(be.visible)
    browser.element(f'#issue_{number}').should(have.text(f'#{number}'))
