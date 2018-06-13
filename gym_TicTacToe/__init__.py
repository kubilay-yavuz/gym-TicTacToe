from gym.envs.registration import register

register(
    id='tictactoe-v0',
    entry_point='gym_foo.envs:TicTacToeEnv',
)
register(
    id='foo-extrahard-v0',
    entry_point='gym_foo.envs:FooExtraHardEnv',
)
