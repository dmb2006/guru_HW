from selene import browser, be, have

browser.open('https://ya.ru')
browser.open('https://google.com')
browser.element('[name="text"]').should(be.blank).type('tutu').press_enter()
browser.element('html').should(have.text('Билеты и отели онлайн на официальном сайте'))

browser.element()