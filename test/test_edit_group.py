from model.group import Group


def test_edit_any_group(app):
    group1 = Group().set_all_parameters_to_random_value()
    app.group.create(group1)
    group_new_state = Group().set_random_parameters_to_random_value()
    app.group.edit_any_group(group_new_state)
