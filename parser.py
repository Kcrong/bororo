from konlpy.tag import Mecab
from utility.data_manage import return2type


class Tagger:
    __pos_tagger = Mecab()

    def __init__(self, sentence):
        self.sentence = sentence
        self.pos = dict(Tagger.__pos_tagger.pos(self.sentence))
        self.__nouns = Tagger.__pos_tagger.nouns(self.sentence)

    @property
    @return2type(list)
    def pos_list(self):
        return self.pos.values()

    @property
    @return2type(list)
    def morph_list(self):
        return self.pos.keys()

    @property
    def word_list(self):
        return self.__nouns

    def __repr__(self):
        return f"<Tagger {self.sentence}>"


class Analyser:
    """
    Tokenize Sentence
    """
    def __init__(self, tag):
        assert type(tag) == Tagger

        self.tag = tag

    def __repr__(self):
        return f"<Analyser {self.tag.sentence}>"


if __name__ == '__main__':
    tag = Tagger("사과는 과일이다.")
