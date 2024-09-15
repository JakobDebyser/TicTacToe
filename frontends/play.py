from console.renderers import ConsoleRenderer
from frontends.console.players import ConsolePlayer
from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.game.players import MinimaxComputerPlayer
from tic_tac_toe.logic.models import Mark

player1 = ConsolePlayer(Mark('X'))
player2 = MinimaxComputerPlayer(Mark("O"))

TicTacToe(player1, player2, ConsoleRenderer()).play()