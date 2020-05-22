from gym.envs.registration import register

register(
    id='bumblebee_0',
    entry_point='gym_foo.envs:BB_Env',
)
