"""A library for Bayesian Knowledge Tracing(BKT) used MIT License.

Modules:
    Child()
"""

from typing import *

class Question(object):
    """A question.

    You can make it by read an exist file.

    Args:
    contents: A tuple of the content of the topic.
    """
    def __init__(self, contents:List[str]):
        self.contents=contents

class Child(object):

    """A child.

    You can make it by read an exist file use fromFile(filename).
    All arguments must be a dictionary of string and float number.
    
    Args:
    plearn:
        Probability that the child has learned.
    ptransit:
        Probability of transit.
    pslip:
        Probability of slip.
    pguess:
        Probability of guess.

    Raises:
    TypeError: Arguments' type was wrong.
    """

    def __init__(self, plearn: Dict[str, float], ptransit: Dict[str, float],
            pslip:Dict[str, float], pguess: Dict[str, float]) -> None:
        """Init the class by probabilities."""
        if not isinstance(plearn, dict):
            raise TypeError("Argument 'plearn' must be a dictionary, "
                "Not %d." % type(plearn).__name__
            )
        if not isinstance(ptransit, dict):
            raise TypeError("Argument 'ptransit' must be a dictionary, "
                "Not %d." % type(plearn).__name__
            )
        if not isinstance(pslip, dict):
            raise TypeError("Argument 'pslip' must be a dictionary, "
                "Not %d." % type(plearn).__name__
            )
        if not isinstance(pguess, dict):
            raise TypeError("Argument 'pguess' must be a dictionary, "
                "Not %d." % type(plearn).__name__
            )
        self.plearn=plearn
        self.ptransit=ptransit
        self.pslip=pslip
        self.pguess=pguess
        pass
    @classmethod
    def fromFile(cls, filename: str):
        """Init the class by an exist file.

        Warning: This function has no writed over.

        Args:
        filename:
            The name of the file.

        Raises:
        FileNotFoundError:
            No such file or directory.
        """
        # TODO(phao0724@163.com) Write this function
        with open(filename, mode="r") as f:
            pass
        pass
    def savemodel(self):
        pass

    def do(self, question:Question, isCorrect:bool):
        """Do a question.

        Args:
        question: A question of the child
        isCorrect: A bool for the correctness of the quesition.

        Raises:
        ValueError:
            The child won't learned the contents of the question.
        """
        if not all([i in self.plearn for i in question.contents]):
            raise ValueError("The child won't learn the content '%s' of the question" % question.contents[[i in self.plearn for i in question.contents].index(False)])
        for i in question.contents:
            if isCorrect:
                """
                                   P(learn)(1-P(slip))
                P(learn)=---------------------------------------
                         P(learn)(1-P(slip))+1-P(learn)*P(guess)
                """
                self.plearn[i]=self.plearn[i]*(1-self.pslip[i])/ \
                (self.plearn[i]*(1-self.pslip[i])+1-self.plearn[i]*self.pguess[i])
            else:
                """
                                     P(learn)P(slip)
                P(learn)=---------------------------------------
                         P(learn)P(slip)+1-P(learn)*(1-P(guess))
                """
                self.plearn=self.plearn*self.pslip/ \
                (self.plearn*self.pslip+1-self.plearn*(1-self.pguess))
            self.plearn=self.plearn+self.ptransit*(1-plearn)
            pass
        pass
