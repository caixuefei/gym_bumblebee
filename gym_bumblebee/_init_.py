from gym.envs.registration import register

register(
    id='bumblebee-v0', # -v0 is needed
    entry_point='gym_bumblebee.env:BumblebeeEnv',
)
