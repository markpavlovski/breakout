import hashlib
import fileinput
import operator
from GameConstants import *

class HighScore:
    def __init__(self):
        self.__highscore = []
        # self.load()

    def get_scores(self):
        return self.__highscore

    def load(self):
        highscore = []
        for line in fileinput.input(GameConstants.HIGHSCORE_DATA):
            name, score, md5 = line.split('[::]')
            md5 = md5.replace('\n','')

            if str(hashlib.md5(str.encode(str(name+score+"pygame"))).hexdigest()) == str(md5):
                highscore.append([str(name), int(score), str(md5)])

            highscore.sort(key=operator.itemgetter(1), reverse=True)
            highscore = highscore[0:11]

            return highscore

    def add(self, name, score):
        score_hash = hashlib.md5((str(name+str(score)+"pygame")).encode("utf-8"))
        self.__highscore.append([name,str(score),score_hash.hexdigest()])

        f = open(GameConstants.HIGHSCORE_DATA,"w")
        for name, score, md5 in self.__highscore:
            f.write(str(name)+"[::]"+str(score)+"[::]"+str(md5)+"\n")

        f.close()
