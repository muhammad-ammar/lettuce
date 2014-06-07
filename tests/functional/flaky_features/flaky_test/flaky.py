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