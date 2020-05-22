from gym.envs.registration import registry, register, make, spec

register(
    id='bumblebee-v0', # -v0 is needed
    entry_point='gym_bumblebee.envs:BumblebeeEnv',
)
