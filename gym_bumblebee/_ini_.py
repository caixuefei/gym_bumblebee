from gym.envs.registration import register

register(
    id='bumblebee_0',
    entry_point='gym_bumblebee.envs:BumblebeeEnv',
)
