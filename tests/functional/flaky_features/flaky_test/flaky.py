from lettuce import world, before, step


step_actions = {'pass': True, 'fail': False}


@before.each_feature
def set_up(feature):
    setattr(world, 'flaky_config', {})
    world.flaky_config['run'] = 2


@step("this test step (.*)")
def this_step(_step, action):
    assert step_actions[action]


@step("execute the steps")
def conditional_step(_step):
    world.flaky_config['run'] -= 1

    if world.flaky_config['run'] <= 0:
        assert True
    else:
        assert False


@step('I have the number (\d+)')
def have_the_number(step, number):
    world.number = int(number)


@step('I compute its factorial')
def compute_its_factorial(step):
    world.number = factorial(world.number)


@step('I see the number (\d+)')
def check_number(step, expected):
    expected = int(expected)
    assert world.number == expected, "Got %d" % world.number


def factorial(number):
    number = int(number)
    if (number == 0) or (number == 1):
        return 1
    else:
        return number*factorial(number-1)
