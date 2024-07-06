from past.builtins import raw_input

import letters
import random
import string
from collections import Counter
import json


def guidelines():
   return '''
    scraHS: αρχειο αποθηκευσης highscores
    pointsp: λεξικο με τους ποντους καθε γραμματος
    lets2: λεξικο με τις φορες που θα εμφανιστει καθε γραμμα
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    class sak: κατασκευαστης σακουλι με γραμματα 
    def randomize_sak: ανακατευει το σακουλι με γραμματα
    def getletters: δεχεται ενα νουμερο και δινει πισω τοσα γραμματα
    def putbackletters: χρεισιμοποιειται κυριως στο πασω και αλλαζει ολα τα γραμματα απο το χερι
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    class player: κατασκευαστης παικτων γονεας απο computer και human
    def srcr: συναρτηση που σπαει ενα string σε λιστα απο χαρακτηρες
    def elenxos: ελενχει αν η λεξη που εδωσε ο χρηστης ειναι αποδεκτη
    def points: βαθμολογει την λεξη που εδωσε ο παικτης
    def pkor: συνολικοι ποντοι για human
    def ckor: συνολικοι ποντοι για computer
    *τα παραπανω θα μπορουσαν να μπουν στις κλασεις παιδια αλλα ειχε σχεδιαστει απο την αρχη να κραταει
    ενα σκορ
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    class human: κατασκευαστης κανονικων παικτων
    def hplay: χρεισιμοποιει τις συναρτισεις του player και εκτυπωνει ενα 20%
    def hprint: εκτυπωνει το υπολοιπο 80% της εφαρμογης
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    class computer: κατασκευαστης παικτων υπολογιστων
    def minalg: αλγοριθμος που βρισκει την μικροτερη λεξη με τα γραμματα
    def maxalg: αλγοριθμος που βρισκει την μεγαλητερη λεξη με τα γραμματα
    def smartalg: αλγοριθμος βασισμενος στον smart με μια προσαρμογη smart-fail γιατι
    ηταν πολυ αδικο για τον χρηση ετσι τωρα παιρνει την πιο προσφατη λεξη με 5 ποντους
    λιγοτερους και θα μπορουσε να ρυθμιστει απο τις ρυθμησεις σε 3-4 δυσκολιες
    def cplay: συναρτηση που εκτελει και εκτιπωνει αποτελεσματα απο το player
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    class game: κατασκευαστης μιας παρτιδας παιχνιδιου
    def setup: αρχικοποιει το sak και παιρνει το ονομα του παικτη
    def run: τρεχει μεχρι να κλεισει ή να τελιοσουν τα γραμματα με ολους τους 
    κανονες του παιχνιδιου
    def end: μετραει ποντους βρισκει και ανακηρισει νικητη μετα παιρνει τα 
    δεδομενα και τα αποθηκευει στο scraHS.json
    '''
    #return

#code pou pernei lexeis apo to greek7.txt kai tis bazei se lista

with open ('scraHS.json','r',encoding="utf-8") as fin:
        highskors = json.load(fin)


words=[]
with open ('greek7.txt','r') as f7:
    for line in f7:
        words.append(line.strip('\n'))


pointsp={'Α':1,'Β':8,'Γ':4,'Δ':4,'Ε':1,
        'Ζ':10,'Η':1,'Θ':10,'Ι':1,'Κ':2,
        'Λ':3,'Μ':3,'Ν':1,'Ξ':10,'Ο':1,
        'Π':2,'Ρ':2,'Σ':1,'Τ':1,'Υ':2,
        'Φ':8,'Χ':8,'Ψ':10,'Ω':3
        }

lets2={'Α':12,'Β':1,'Γ':2,'Δ':2,'Ε':8,
        'Ζ':1,'Η':7,'Θ':1,'Ι':8,'Κ':4,
        'Λ':3,'Μ':3,'Ν':6,'Ξ':1,'Ο':9,
        'Π':4,'Ρ':5,'Σ':7,'Τ':8,'Υ':4,
        'Φ':1,'Χ':1,'Ψ':1,'Ω':3
        }


class SakClass:

    def __init__(self):
        self.sak=[]
        for i, x in lets2.items():
            tm =lets2[i]
            for j in range(tm):
                #sak.append(lets2.key())
                self.sak.append(i)
        #print("sak is",self.sak, "with length", len(self.sak))

    def __len__(self):
        return len(self.sak)

    def randomize_sak(self):
        #sak2=sak
        random.shuffle(self.sak)
        #print("sak got randomzised", self.sak)
        return self.sak


    def getletters(self,gra):
        plst=[]
        for i in range(gra):
            plst.append(self.sak[i])
            self.sak.pop(i)
        #print(self.sak)
        #print(len(self.sak))
        #print(plst)
        return plst


    def putbackletters(self,lst):
        plst=[]
        for i in range(len(lst)):
            #print(i)
            plst.append(self.sak[i])
            self.sak.pop(i)
            self.sak.append(lst[i])
        #print(self.sak)
        #print(len(self.sak))
        #print(plst)
        return plst

'''edo teliose i kalsi sakclass ke xekinaei i player'''

class Player:
    def __init__(self,name):
        self.skor=0
        self.xeri=[]
        self.name=name
        self.pskor=0
        self.cskor=0
        #print(self.name,self.xeri,self.skor)

    def srcr (self,lexi):

        self.lex=[char for char in lexi]
        #print(self.lex)
        return self.lex

    def elenxos(self,lex,xeri,lexi):
        flag1= False
        flag2=False
        #elenxos 1 an ta grammata iparxoun sto xeri
        result = all(elem in xeri for elem in lex)
        if (result):
            flag1=True
            #print("ok gramata")

        #elenxos 2 elenxei tin lexi sto arxio
        for i in words:
            if(lexi==i):
                flag2=True

        if(flag1==True and flag2==True):
            for i in range (len(lex)):
                #for j in range(len(xeri)):
                for j in xeri:
                    if(lex[i]==j):
                        #print("grama",j)
                        st=xeri.index(j)
                        xeri.pop(st)

            #print(xeri)
            #print("lexi apodexti")
            return True
        else:
            #print("lathos")
            return False


    def points(self,lex):
        pods=0
        for i in range(len(lex)):
            for e, p in pointsp.items():
                if(lex[i]==e):
                    #ww=points[ee]
                    ww=p
                    pods+=ww
                    #print(e,p)
        #print("podoi ine",pods)
        self.skor+=pods
        #print(self.skor)

        return pods

    def pkor(self):
        #print("skor", self.skor)

        return self.pskor

    def ckor(self):
        #print("skor", self.skor)

        return self.cskor

'''edo teleionei i class player ke xekinane human kai computer'''

class Human(Player):

    def hplay(self,lexi,xeri):

        gram=Player.srcr(self,lexi)
        #print("hplay",lexi)
        helenxos=Player.elenxos(self,gram,xeri,lexi)
        if(lexi=="pass"):
            print("πασο")
            return False
        if(helenxos==False):
            print("Δεν υπαρχει τετοια λεξη")
            return False
        if(helenxos==True):
            ppoints=Player.points(self,gram)
            #self.pskor=Player.pkor(self)
            self.pskor+=ppoints
            print("Λέξη: ",lexi)
            print("Πόντοι λέξης: ",ppoints)
            print("*** Παίκτης: ", self.name, "   *** Σκορ: ", self.pskor)
            return True
        #return(skor)




    def hprint(self,xeri):
        print("*******************")
        print("*** Παίκτης: ",self.name,"   *** Σκορ: ",self.pskor)
        print(">>> Γράμματα: ", xeri)


class Computer(Player):
    #min algorithm περνει την μικροτερη λεξη 
    def minalg(self,xeri, words):
        pod=0
        char_count = Counter(xeri)
        for string in words:
            string_chars = list(string)
            string_count = Counter(string_chars)
            if all(string_count[char] <= char_count[char] for char in string_chars):
                print("i lexi min tou pc", string_chars)
                return string_chars
        for i in range(len(string_chars)):
                    for e, p in pointsp.items():
                        if (string_chars[i] == e):
                            ww = p
                            pod = ww
                #words2[string] = pod
        #print(words2)
        for e, p in words2.items():
            if(len(e)>1):
                return e

      
        return None

    def maxalg(self,xeri, words):
        pod=0
        char_count = Counter(xeri)
        for string in reversed(words):
            string_chars = list(string)
            string_count = Counter(string_chars)
            if all(string_count[char] <= char_count[char] for char in string_chars):
                print("i lexi max tou pc", string_chars)
                return string_chars

        for i in range(len(string_chars)):
                    for e, p in pointsp.items():
                        if (string_chars[i] == e):
                            ww = p
                            pod = ww
                #words2[string] = pod
        #print(words2)
        reversed_list = words2.reverse()
        for e, p in reversed_list():
            if(len(e)>1):
                return e
        return None

    #smart fail περνει την λεξει που εχει τουλαχιστον 5 ποντους λιγοτερους απο την καλυτερη
    def smartalg(self,xeri, words):
        #smart fail algorithm
        words2={}
        pod=0
        mpod=0
        char_count = Counter(xeri)
        for string in words:
            string_chars = list(string)
            string_count = Counter(string_chars)
            if all(string_count[char] <= char_count[char] for char in string_chars):

                for i in range(len(string_chars)):
                    for e, p in pointsp.items():
                        if (string_chars[i] == e):
                            ww = p
                            pod += ww
                words2[string]=pod
                if (mpod < pod):
                    mpod = pod
                pod=0
        mpod-=5
        for e, p in words2.items():
            #print(e)
            if (mpod <= p):
                return e

        return False


  #smart algorithm περνει την καλυτερη λεξη σε ποντους
    def smart2alg(self,xeri, words):
          #smart fail algorithm
          words2={}
          pod=0
          mpod=0
          char_count = Counter(xeri)
          for string in words:
              string_chars = list(string)
              string_count = Counter(string_chars)
              if all(string_count[char] <= char_count[char] for char in string_chars):
  
                  for i in range(len(string_chars)):
                      for e, p in pointsp.items():
                          if (string_chars[i] == e):
                              ww = p
                              pod += ww
                  words2[string]=pod
                  if (mpod < pod):
                      mpod = pod
                  pod=0
          for e, p in words2.items():
              #print(e)
              if (mpod <= p):
                  return e
  
          return False
  
    def minmaxalg(self, xeri, words):
        # min max algorithm
        words2 = {} #καταληλες λεξεις
        pod = 0
        lexs=""
        char_count = Counter(xeri)
        for string in words:
            string_chars = list(string)
            string_count = Counter(string_chars)
            if all(string_count[char] <= char_count[char] for char in string_chars):

                for i in range(len(string_chars)):
                    for e, p in pointsp.items():
                        if (string_chars[i] == e):
                            ww = p
                            pod = ww
                words2[string] = pod
        #print(words2)
        for e, p in words2.items():
            if(len(e)>1):
                return e
        return False

    def cplay(self,xeri,alg):
        if(self.smartalg(xeri,words)==False and alg==1):
            print("pass")
            return False
        if(self.minmaxalg(xeri,words)==False and alg==2):
            print("pass")
            return False
        else:
            print("*******************")
            print("*** Παίκτης: ",self.name,"   *** Σκορ: ",self.cskor)
            print(">>> Γράμματα: ", xeri)
            if (alg==1):
                clex = self.smartalg(xeri, words)
            elif(alg==2):
                clex=self.minmaxalg(xeri,words)
            elif(alg==3):
                clex=self.smart2alg(xeri,words)
            elif(alg==4):
                clex=self.maxalg(xeri,words)
            elif(alg==5):
                clex=self.minalg(xeri,words)
            print("Παίζω την λέξη: ",clex)
            cgram = string_chars = list(clex)
            cpoints = Player.points(self,cgram)
            print("Πόντοι λέξης: ",cpoints)
            self.cskor += cpoints
            #self.cskor = Player.ckor(self)
            print("*** Παίκτης: ", self.name, "   *** Σκορ: ", self.cskor)
            return True


'''arxi class game'''
class Game:
    def __init__(self):
        #self.pln
        self.pxeri=[]
        self.pskor=0
        self.cxeri=[]
        self.cskor=0
        self.con="pc"
    def setup(self,alg):
        #print(alg)
        self.pln=input("Ονομα παικtη:")
        #self.pln=pln
        self.sak = SakClass()
        self.sak.randomize_sak()
        self.pxeri= self.sak.getletters(7)
        self.cxeri= self.sak.getletters(7)
        self.pl1 = Human(self.pln)
        self.com= Computer("pc")

        if(alg==1):
            print("Ο υπολογιστης παιζει με fail αλγοριθμο")
        elif(alg==2):
            print("O υπολογιστης παιζει με min max αλγοριθμο")
        elif(alg==3):
          print("O υπολογιστης παιζει με smart αλγοριθμο")
        elif(alg==4):
          print("O υπολογιστης παιζει με max αλγοριθμο")
        elif(alg==5):
          print("O υπολογιστης παιζει με min αλγοριθμο")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Καλοσορισες",self.pln," σε παιχνιδι scrambble εναντια σε εναν υπολογιστη, καλη διασκεδαση")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.run(alg)

    def run(self,alg):
        self.pl1.hprint(self.pxeri)
        self.lex=input("Λεξη: ")
        while(self.lex !="q" or len(self.sak) < 7):
            #code for player turn
            flagp= self.pl1.hplay(self.lex, self.pxeri)
            if(flagp==True):
                nsak=len(self.lex)
                self.pxeri= self.pxeri + self.sak.getletters(nsak)
                self.pskor += self.pl1.points(self.pl1.srcr(self.lex))
            else:
                self.sak.putbackletters(self.pxeri)
                self.pxeri= self.sak.getletters(7)
            flagp=False

            #code for computer turn
            flagc=self.com.cplay(self.cxeri,alg)
            if (flagc == True):
                #isos lathos
                if(alg==1):
                    cl=self.com.smartalg(self.cxeri,words)
                elif(alg==2):
                    cl=self.com.minmaxalg(self.cxeri,words)
                elif(alg==3):
                    cl=self.com.smart2alg(self.cxeri,words)
                elif(alg==4):
                    cl=self.com.maxalg(self.cxeri,words)
                elif(alg==5):
                    cl=self.com.minalg(self.cxeri,words)

                nsak = len(cl)
                wr=[]
                for string in cl:
                    wr+=string
                #print (wr)
                '''
                for i in range (len(self.cxeri)-1):
                    for j in range (len(wr)-1):
                        if(wr[j]==self.cxeri[i]):
                            self.cxeri.pop(i)
                            wr.pop(j)
                            '''
                for i in wr:
                    if i in self.cxeri:
                        self.cxeri.remove(i)

                #print(self.cxeri)
                #print(wr)
                self.cxeri =self.cxeri+ self.sak.getletters(nsak)
                self.pskor += self.com.points(self.pl1.srcr(cl))
            else:
                self.sak.putbackletters(self.cxeri)
                self.cxeri = self.sak.getletters(7)
            flagc=False
            #code for player turn and end of while
            self.pl1.hprint(self.pxeri)
            self.lex = input("Λεξη: ")

        ps1=self.pl1.pkor()
        ps2=self.com.ckor()
        print(ps1,ps2)
        self.end(ps1,ps2)


    def end(self,ans,pcs):
        print("Παικτης: ", self.pln," συγκέντροσε: ",ans)
        print("Παικτης: ", self.con, " συγκέντροσε: ", pcs)
        if(ans>pcs):
            print("Νικητης του παιχνιδιου: ",self.pln)
        elif(ans<pcs):
            print("Νικητης του παιχνιδιου: ", self.con)
        else:
            print("ισοπαλια")
        print("ευχαριστουμε που παιξατε το παιχνιδι αυτο")
        #print(highskors)
        highskors[self.pln]=self.pskor

        with open('scraHS.json','w') as fout:
            json.dump(highskors,fout)

        exit(403)












#MAIN



#sak=SakClass()
#sak.randomize_sak()
#sak.getletters(2)
#sak.putbackletters(['α','β','γ'])

#pl=Player("ginas")
#pl.srcr("ΛΕΞΗ")
#pl.elenxos(['Λ','Ε','Ξ','Η'],['Α','Η','Λ','Ξ','Ε'],"ΛΕΞΗ")
#pl.elenxos(['Α','Λ','Ε','Ξ','Η'],['Α','Η','Λ','Ξ','Ε'],"ΑΛΕΞΗ")
#pl.points(['Λ','Ε','Ξ','Η'])
#pl.tskor()

#pl1=Human("gior")
#pl1.hplay("ΛΕΞΗ",['Α','Η','Λ','Ξ','Ε']) #ok
#pl1.hplay("pass",['Α','Η','Λ','Ξ','Ε'])
#pl1.hprint(sak.getletters(7))

#comp1=Computer("pc")
#comp1.minalg(sak.getletters(7),words)
#comp1.maxalg(sak.getletters(7),words)
#comp1.smartalg(sak.getletters(7),words)
#comp1.cplay(sak.getletters(7))
#game1=Game()
#game1.setup()
#game1.end()