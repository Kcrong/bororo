from konlpy.tag import Mecab
from utility.exception import ignore
from utility.data_manage import return2type


class Tagger:
    __pos_tagger = Mecab()

    def __init__(self, sentence):
        self.sentence = sentence
        self.tag = dict(Tagger.__pos_tagger.pos(self.sentence))

    @property
    @return2type(list)
    def pos_list(self):
        return self.tag.values()

    @property
    @return2type(list)
    def word_list(self):
        return self.tag.keys()

    def __repr__(self):
        return f"<Tagger {self.sentence}>"


class Analyser:
    def __init__(self, tag):
        """
        try:
            assert type(tag) == Tagger
        except AssertionError:
            print("Error!!!")
        """
        with ignore(AssertionError, error_message="Wrong Param!"):
            assert type(tag) == Tagger

        self.tag = tag

    def __repr__(self):
        return f"<Analyser {self.tag.sentence}>"


if __name__ == '__main__':
    tag = Tagger("사과는 과일이다.")
