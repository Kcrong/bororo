from konlpy.tag import Mecab
from utility.data_manage import return2type
from utility.exception import AnalysisError


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


class Analyzer:
    """
    Tokenize Sentence
    TODO: analyze sentence with https://cloud.google.com/natural-language/
    """
    def __init__(self, sentence):
        self.tag = Tagger(sentence)
        self.name, self.attr, self.mean, self.bool_type = self.__analysis()

    def __repr__(self):
        return f"<Analyser {self.tag.sentence}>"

    def __analysis(self):
        for pos in self.tag.pos_list:
            if pos.startswith("VC"):  # check if sentence have designator
                if "P" in pos:  # positive designator
                    bool_type = True
                elif "N" in pos:  # negative designator
                    bool_type = False
                else:
                    raise AnalysisError("UnKnown Designator")
                break
        else:
            # sentence has no designator
            raise AnalysisError("UnKnown Sentences")

        name, attr, mean = self.find_direct_object_info()

        return name, attr, mean, bool_type

    def find_direct_object_info(self):
        """
        Find the 'direct object' from self.sentence and its meaning.
        """
        name = None
        attr = None
        mean = None

        for idx in range(len(self.tag.pos)):
            morph = self.tag.morph_list[idx]
            if morph in self.tag.word_list:
                if self.tag.pos_list[idx + 1].startswith("VC"):
                    mean = morph
                elif name is not None and len(self.tag.word_list) > 2:
                    attr = morph
                else:
                    name = morph

        return name, attr, mean
