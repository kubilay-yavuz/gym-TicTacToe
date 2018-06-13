import gym
from gym import error, spaces, utils
from gym.utils import seeding


class TicTacToeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.action_space = spaces.Discrete(9)
        self.observation_space = spaces.Discrete(256 * 256 * 2)
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.done = False
        self.winner = 0

    def step(self, action):
        #   spe will be either -1 or 1 in terms of o and x
        spe, cell = action[0], action[1]
        if spe == 'x':
            spe = 1
        elif spe == 'o':
            spe = -1
        #   check if is there a 0 in the
        m = cell[0] - 1
        n = cell[1] - 1
        if self.board[m][n] != 0:
            print("Cell is not empty")
        else:
            self.board[m][n] = spe

        #   check if equilibrium reached
        for i in range(3):
            if self.board[i] == [1, 1, 1] or [self.board[1][i], self.board[2][i], self.board[3][i]] == [1, 1, 1]:
                self.done = True
                self.winner = 'x'
            elif self.board[i] == [-1, -1, -1] or [self.board[1][i], self.board[2][i], self.board[3][i]] == [-1, -1,
                                                                                                             -1]:
                self.done = True
                self.winner = 'o'
        if [self.board[0][0], self.board[1][1], self.board[2][2]] == [1, 1, 1] or [self.board[2][0], self.board[1][1],
                                                                                   self.board[0][2]] == [1, 1, 1]:
            self.done = True
            self.winner = 'x'
        elif [self.board[0][0], self.board[1][1], self.board[2][2]] == [-1, -1, -1] or [self.board[2][0],
                                                                                        self.board[1][1],
                                                                                        self.board[0][2]] == [-1, -1,
                                                                                                              -1]:
            self.done = True
            self.winner = 'o'
        return self.board, self.done, self.winner
    def reset(self):
        self.board = [0, 0, 0,
                      0, 0, 0,
                      0, 0, 0]
        self.done=False
        self.winner=0

    def render(self, mode='human', close=False):
        pass
