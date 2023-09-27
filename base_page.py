from urllib.parse import urlparse


class BasePage(object):
    def __init__(self, driver, url, timeout=40):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def find_el(self, by, location):
        return self.driver.find_element(by, location)
