from model.group import Group
from random import randint


class GroupHelper:
    def __init__(self, app):
        self.app = app
        self.menu = app.menu

    def create(self, group: Group):
        wd = self.app.wd
        self.menu.groups()

        wd.find_element_by_name("new").click()
        self.fill(group)

        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def edit_any_group(self, group: Group):
        wd = self.app.wd
        self.menu.groups()

        checkbox_list = wd.find_elements_by_name("selected[]")
        assert len(checkbox_list) > 0

        checkbox = checkbox_list[randint(0, len(checkbox_list) - 1)]
        checkbox.click()

        wd.find_element_by_name("edit").click()

        self.fill(group)

        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def delete_any_group(self):
        wd = self.app.wd
        self.menu.groups()

        checkbox_list = wd.find_elements_by_name("selected[]")
        assert len(checkbox_list) > 0

        checkbox = checkbox_list[randint(0, len(checkbox_list) - 1)]
        checkbox.click()

        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def fill(self, group):
        self.type_in_field("group_name", group.name)
        self.type_in_field("group_header", group.header)
        self.type_in_field("group_footer", group.footer)

    def type_in_field(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(value)

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.menu.groups()

        return len(wd.find_elements_by_name("selected[]"))
