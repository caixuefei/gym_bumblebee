from gym.envs.registration import register

register(
    id='bumblebee-v0',
    entry_point='gym_bumblebee.env:BumblebeeEnv',
)
