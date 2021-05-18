from abc import *
from state import State
import sys

MAX_FLOAT = sys.float_info.max
MIN_FLOAT = -MAX_FLOAT


class AdversarialSearch(object):
    """
    Apstraktna klasa za suparnicku/protivnicku pretragu.
    """

    def __init__(self, board, max_depth):
        """
        :param board: tabla koja predstavlja pocetno stanje.
        :param max_depth: maksimalna dubina pretrage (koliko poteza unapred).
        :return:
        """
        self.initial_state = State(board, parent=None)
        self.max_depth = max_depth

    @abstractmethod
    def perform_adversarial_search(self):
        """
        Apstraktna metoda koja vrsi pretragu i vraca sledece stanje.
        """
        pass


class Minimax(AdversarialSearch):


    def minimax(self, state, depth, maximizingPlayer):
        if depth == self.max_depth or state.board.game_over: # dosli smo do kraja
            return state.calculate_value()
        
        next_states = state.generate_next_states(maximizingPlayer)
        best_value = MIN_FLOAT if maximizingPlayer else MAX_FLOAT
        best_next_state = None

        delta = 1 if maximizingPlayer else -1 #za odredjivanje max ili min poteza

        for next_state in next_states:
            next_state_value = self.minimax(next_state, depth + 1, not maximizingPlayer)

            if (next_state_value - best_value) * delta > 0:
                best_next_state = next_state
                best_value = next_state_value

        if depth == 0:
            return best_next_state
        
        return best_value

    def perform_adversarial_search(self):
        return self.minimax(self.initial_state, 0, True)


class AlphaBeta(AdversarialSearch):

    def alpha_beta(self, state,depth,maximizingPlayer, alpha, beta):
        if depth == self.max_depth or state.board.game_over: # dosli smo do kraja
            return state.calculate_value()
        
        next_states = state.generate_next_states(maximizingPlayer)
        best_value = MIN_FLOAT if maximizingPlayer else MAX_FLOAT
        best_next_state = None

        delta = 1 if maximizingPlayer else -1 #za odredjivanje max ili min poteza

        for next_state in next_states:
            next_state_value = self.alpha_beta(next_state, depth + 1, not maximizingPlayer, alpha, beta)

            if maximizingPlayer and next_state_value > best_value:
                best_next_state = next_state
                best_value = next_state_value
                alpha = max(alpha, next_state_value)
            
            if not maximizingPlayer and next_state_value < best_value:
                best_next_state = next_state
                best_value = next_state_value
                beta = min(beta, next_state_value)
            
            if alpha >= beta:
                break
        
        if depth == 0:
            return best_next_state
        
        return best_value

    def perform_adversarial_search(self):
        return self.alpha_beta(self.initial_state, 0, True, MIN_FLOAT, MAX_FLOAT)
