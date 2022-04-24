import random as rand
from time import *
import inspect
import itertools
import copy
import numpy as np
import pyjack

#Super Reality => The class of object that can contain reality at different location
class infinity_Stones:
    def __init__(self , Owner , location , Object , Color , Ability):
        self.location = location
        self.Owner = Owner
        self._Color = Color
        self.Object = Object
        self._Ability = Ability

    def show_StonesInfo(self):
        print(self._Ability)
    
    def show_Color(self):
        print(self._Color)
      
    
class MindType:
    def __init__(self,  data):
        self.dt = data

class SpaceType:
    def __init__(self,  data):
        self.dt = data

class RealityType:
    def __init__(self,  data = str):
        self.dt = data

    def __eq__(self, other):
        return self.dt == other.dt
    
        
#Object : Life object , World object , Time object (Derived from World) , Soul object 


class Utility:
    def UpdateVallst(value , lst = list):
        lst2 = lst.copy()
        lst2.append(value)
        return lst2
        #self.ValueFromExp = lst1.copy()
        #del self.__dict__["lst"]

class Time:
    def __init__(self, year, month , day , hour , minute , second):
        self.year = year
        if month in [x for x in range(1,13)]:
            self.month = month
        elif month not in [x for x in range(1,13)]:
            print("Month can only be in 1-12")

        if day in [x for x in range(1,32)]:
            self.day = day
        elif day not in [x for x in range(1,32)]:
            print("Day can only be in 1-31")

        if hour in [x for x in range(0,24)]:
            self.hour = hour
        elif hour not in [x for x in range(0,24)]:
            print("Hour can only be in 0-23")

        if minute in [x for x in range(0,60)]:
            self.minute = minute
        elif minute not in [x for x in range(0,60)]:
            print("Minute can only be in 0-59")

        if second in [x for x in range(0,60)]:
            self.second = second
        elif second not in [x for x in range(0,60)]:
            print("Second can only be in 0-59")

    def __repr__(self):
        return f"{self.year}/{self.month}/{self.day}-{self.hour}:{self.minute}:{self.second}"

    def __eq__(self , other):
        return (self.year , self.month , self.day , self.hour , self.minute , self.second) == (other.year , other.month , other.day , other.hour , other.minute , other.second)

    def __hash__(self):
        return hash((self.year , self.month , self.day , self.hour , self.minute , self.second))

class Soul:
    def __init__(self , name = str , control_status = bool , state  = str, numSplit = 0):
        self.name = name
        if isinstance(control_status , bool) == True: 
          self.control_status = control_status
        elif isinstance(control_status , bool) == False:
          return "The status is not correct"
        lst = ["s" , "d" , "a", "p"] #{s : Split , d : death , a : alive , p : pain}
        if state in lst :
          self.state = state
        elif state not in lst:
          return "The State have only 4 state , {s : Split , d : death , a : alive , p : pain}"
        if self.state == "s":
          self.numSplit = numSplit
        else : 
          pass
    def __eq__(self, other):
        return [self.name,self.control_status,self.state] == [other.name,other.control_status,other.state]

    def __hash__(self):
        return hash(self.name)
          

class Matter:
    def __init__(self , Name = str  ,Mass = float , Shape = str , location = str ,matterState = str,state = str,propertime = Time,timerate= int,exprlist = [], **kwargs):
        self.Name = Name
        self.Shape = Shape
        self.location = location
        StatusForm = ["s" , "l" , "g",  "p","cr","mul"]
        if matterState in StatusForm: #State of matter: solid ,liquid, gas , plasma ,chemical reaction and multi-state
            self.matterState = matterState #Status description
        if matterState not in StatusForm :
            return f"The status should be only in this list , {StatusForm}"
        if matterState == "cr" :
            self.Mass = 0
        elif matterState != "cr":
            self.Mass = Mass
        if state in ["i" , "r"]: # "i" stand for illusion and "r" stand for real
            self.state = state
        elif state not in ["i" ,"r"]:
            return "Matter has only two states illusion (i) or real (r)"
        self.propertime = propertime
        self.timerate= timerate
        self.ValueFromExp = []
        argdict = {"Name" : self.Name , "Mass" : self.Mass, "Shape" : self.Shape , "location" : self.location , "matterState" : self.matterState , "state" : self.state , "propertime" : self.propertime,"timerate" : self.timerate,  "Vallst" : self.ValueFromExp}
        argdict.update(kwargs)
        self.exprlist = exprlist
        obj = Utility
        self.Uti = obj
        self.kw = kwargs
        #self.Abillity  = argdict #Other atrribute we should know about the object





    def run(self , exp): #exp is expression of a function create under reality stone and if "name" == main: #May need realities where you do it
        Abi = self.__dict__
        #print(Abi)

        if all(isinstance(x , RealityType) for x in self.exprlist):
            pass
        else:
            print("All elements in expression list should be Reality type")
        if exp in self.exprlist:
            pass
        elif exp not in self.exprlist:
            print(f"You can choose the ability only from the expression list, {self.exprlist}")

        if isinstance(exp , RealityType) == True:
            expT = exp.dt
            #print(expT.rstrip())
            #code = compile(expT, "<string>", "eval")
            #loc = {}
            ans = exec(expT, Abi)
            #ans = loc['return_me']
        elif isinstance(exp , RealityType) == False:
            return "the expression should been create by reality stone"
    # *exec() won't return values

    def __repr__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        return (self.__dict__) == (other.__dict__)


class Life(Matter):
  def __init__(self , Name = str  ,Mass = float , Shape = str , location = str ,matterState = str,state = str ,  MindState = bool , age = float , Souls = Soul,Strength = float,Limit_Strength = float,Pain_limit = float,propertime= Time,timerate = int,exprlist= [] , **kwargs):
      super().__init__(Name ,Mass, Shape , location, matterState , state,propertime, timerate,exprlist,  **kwargs)

      self.MindState = MindState #Control by a mind stone or not? (T/F)
      self.age = age
      if isinstance(Souls , Soul) == True and Souls.name == self.Name:
        self.Souls = Souls
      elif isinstance(Souls , Soul) == False:
        print("It's must be a Soul object")
      else:
        print("Soul.name must be the same like name OR Soul.state must be \"a\" or alive ")
      #If you want to create a non specific life object you can let name = "all" and assume Mindstate ,placelive and age to be average
      self.propertime = propertime
      obj = Utility
      self.Uti = obj
      #argdict =  {"Name" : self.Name , "location" : self.location , "Mass" : self.Mass , "Shape" : self.Shape , "matterState" : self.matterState , "state" : self.state , "MindState" : self.MindState , "age" : self.age , "Souls" : self.soul , "propertime" : self.propertime,"timerate" : self.timerate,  "Vallst" : self.ValueFromExp}
      #argdict.update(kwargs)
      #self.Abillity = argdict
      self.Limit_Strength = Limit_Strength

      if Pain_limit < Limit_Strength:
          self.Pain_limit = Pain_limit
          if Strength < Pain_limit:
              pass
          elif Strength >= Pain_limit:
              self.Souls.state = "p"
      elif Pain_limit >= Limit_Strength:
          self.Pain_limit = Limit_Strength / 2 #Default Pain limit
          raise Exception("Pain limit should lower than the limit of strength")

      if Strength < Limit_Strength:
          self.Strength =  Strength
      elif Strength >= Limit_Strength:
          self.Shape = "Pieces"
          self.Souls.state = "d"
          self.Strength = Strength








class Reality: #Create your own reality simulation world (When using reality stone) , ilusion reality
    def __init__(self, location , theme ,state, timeIllu = None , Temp = float , lifelist = list ,matter_list = list , propertime= Time, timerate = int ,Multiverse = []): #lifelist and matter_list is all the life or the matter inside this reality object (just SOME specific object)
        self.location = location #Position in space
        self.theme = theme
        self.timeIllu = timeIllu
        if state in ["i" , "r"]: # "i" stand for illusion and "r" stand for real
            self.state = state
        elif state not in ["i" ,"r"]:
            print("Reality has only two states illusion (i) or real (r)")
        self.Temp = Temp
        if all(isinstance(k , Life) for k in lifelist) == True and all(k.location == self.location for k in lifelist) == True:
            self.lifelist = lifelist
        else:
            print("all life should be life object or the state of the life object should be illusion (i)")
        if all(isinstance(k , Matter) for k in matter_list) == True  and all(k.location == self.location for k in matter_list) == True:
            self.matter_list = matter_list
        else:
            print("all matter should be matter object or the matter should not be a life object")

        self.propertime = propertime
        if all(x.timerate == timerate for x in lifelist) == True and all(x.timerate == timerate for x in matter_list) == True:
            self.timerate = timerate
        else:
            #print("In that reality and that location ,everything have the same time rate")

            for x in lifelist:
                if x.timerate == timerate:
                    pass
                elif x.timerate != timerate:
                    self.lifelist.remove(x)

            for x in matter_list:
                if x.timerate == timerate:
                    pass
                elif x.timerate != timerate:
                    self.matter_list.remove(x)

            self.timerate = timerate




    def dictSlice(self , obj = Matter or Life or Reality, length = int):
        dic = obj.__dict__
        print(dic)
        print(length)
        slidic = dict(itertools.islice(dic.items(), length))
        return slidic

    def __eq__(self ,other):
        return (self.location , self.timerate , set(self.lifelist) , set(self.matter_list)) == (other.location ,other.timerate, set(other.lifelist) , set(other.matter_list))

    def __repr__(self):
        return f"{self.__dict__}"

class Timeline:
    def __init__(self , World = Reality):
        self.timeline = {} #{Time : event}
        self.World = World

    def __eq__(self, other):
        return (self.World) == (other.World)

    def Update(self,tS = Time,interObj = list): #,length = list): #add = {Key , [values]},   This is the update for situation that you want the propertime of the object in the reality to be equal to the reality time
        self.World.propertime = tS
        World = self.World

        objlst = [] #World will be a part of objlst
        objlst2 = []
        for i in interObj:
            if i.timerate == 0:
                raise Exception("The object will change through time as its time rate isn't equal 0")
            elif i.timerate != 0:
                pass
            i.propertime = tS
            #print(tS)
            #i.ValueFromExp = i.__dict__["ValueFromExp"]
            dic = i.__dict__
            if "__builtins__" in dic:
                del dic["__builtins__"]
            elif "__builtins__" not in dic:
                pass
                #print(f"{i} don't have \"__builtins__\" as a key in the dictionary")
            #
            #print(dic.copy())
            objlst.append(copy.deepcopy(i))
            #objlst2.append(i.copy())

        #objlst.append(World.__dict__.copy()) #World will be append as the last element in the list
        #objlst.append(objlst2)
        dic1 = World.__dict__
        if "__builtins__" in dic1:
            del dic1["__builtins__"]
        elif "__builtins__" not in dic1:
            pass
        objlst.append(copy.deepcopy(World))
        Newdic =  {tS : objlst}
        self.timeline.update(Newdic)
        #print(self.timeline)

        '''
        for i,k in zip(interObj,length):
            i.propertime = tS
            dic = World.dictSlice(i ,k)
            #print("$dic")
            #print(dic)
            objlst.append(dict(itertools.islice(dic.items(), k)))
            #print("$obj")
            #print(objlst)

        Newdic = {tS : objlst}
        self.timeline.update(Newdic)
        #print("$$")
        #print(self.timeline)
        '''

        """
        dic= self.timeline
        for i in interObj:
            if isinstance(i ,Matter) == True or isinstance(i ,Life) == True or isinstance(i ,Reality) == True :
                pass
            else:
                print("Object should be type, Matter or Life")
        t = list(add.keys())[0]
        if len(add) == 1 and isinstance(list(add.keys())[0] , Time):
            for i in interObj:
                i.propertime =  t     #Chnage the attribute: propertime of the object to suitable with the time it's stay in the timeline

        Newdic = dic.update(add)
        return Newdic
        """

    def Interaction(self ,tObj, st = Time , ft= Time ,expr = str , interObj = list ,tS = list, **kwargs): #Time => Reality proper time
        World = self.World
        for x in interObj:
            #print("i***")
            #print(interObj)
            #print(World.lifelist)
            if x in World.matter_list:
                pass
                #print(True , x)
            elif x in World.lifelist:
                pass
                #print(True , x)
            else:

                if isinstance(x, Life):
                    print(x.__dict__)
                    print(World.lifelist[0].__dict__)
                    print(x.__dict__["exprlist"] == World.lifelist[0].__dict__["exprlist"] )
                    print(x.__dict__["soul"] == World.lifelist[0].__dict__["soul"])
                elif isinstance(x , Matter):
                    print(x.__dict__)
                    print(World.matter_list[0].__dict__)
                    print(x.__dict__["exprlist"] == World.matter_list[0].__dict__["exprlist"] )

                print(False , x)

        if all(x in World.matter_list or x in World.lifelist for x in interObj) == True:
            pass
        elif all(x in World.matter_list or x in World.lifelist for x in interObj) == False:
            return "Object that can interact in this realiy must be the elements of this reality"
        if World.propertime == st:
            pass
        elif World.propertime != st:
            return "Start time should be the same as the proper time of that reality"
        if all(x.location == World.location for x in interObj) == True:
            pass
        elif all(x.location == World.location for x in interObj) == False:
            return "every object in this reality should be in the same location"

        if isinstance(tObj , Timeline) == True:
            pass
        elif isinstance(tObj , Timeline) == False:
            return "tObj should be Timeline Object"
        if World == tObj.World:
            self.tObj = tObj
        elif World != tObj.World:
            return "tObj can only be the Timeline object that has the same attribute, World"

        argdict = {"st" : st ,"ft"  : ft, "World" : World , "interObj" : interObj , "timeline" : self.timeline , "tObj" : self.tObj, "tS" : tS}
        argdict.update(kwargs)

        ans = exec(expr , argdict)

        """
        Advice for create expression for interaction
        1.At the end, you should set [World.propertime = ft] 
        2.When there has some change to the argument, there should be some update to the timeline BEFORE that event happen
        3.Value in the timeline dictionary should be a string describe what happen if there has no change to the arguments
        but if there has, then the value should be an arguments before the change OR af the change.
        4.Timestamp => timeline.update(dict) => dict means the new time that you want to update ,for Ex. {Time() , self.Ability} 
        *self.Ability is the dictionary of the arguments of that matter at that time
        5.If you want a value return from the expr ,you can use self.ValueFromExp (in dict will call Vallst )that is a list to 
        contain that value ,append to that list.
        6.Object that interact in the reality can use there own ability that had been DESIGNED for return value in the interaction expression.
        """


class Universe:
    def __init__(self , Reality_list = list):
        if all(isinstance(x , Reality) for x in Reality_list) == True:
            self.Reality_list = Reality_list
        elif all(isinstance(x , Reality) for x in Reality_list) == False:
            raise Exception("All element in reality list should be Reality type object")

class Multiverse:
    def __init__(self , tl_list = list):
        # {location1 : {starttime1 : Timeline , starttime2 : Timeline} , location2 : {starttime1 : Timeline , starttime2 : Timeline}}
        wsame = []
        stsame= []
        worldset = set()
        stset = set()
        superdic = {}
        subdic  = {}
        if len(tl_list) > 0:
            if all(isinstance(x , Timeline) for x in tl_list) == True:
                for i1 in tl_list:
                    worldset.add(i1.World) #Time rate and location of the world is the identification
                for i2 in worldset:
                    for x in tl_list:
                        if x.World == i2:
                            wsame.append(x)
                        elif x.World != i2:
                            pass
                    superdic[i2] = wsame.copy()
                    wsame.clear()

                for i3 in worldset:
                    lst = superdic[i3]
                    for i4 in lst: # Create stset
                        x = list(i4.timeline)
                        stset.add(x[0]) # Add start time
                    for i5 in stset:
                        for i6 in lst:
                            x1 = list(i6.timeline)
                            if x1[0] == i5:
                                stsame.append(x1)
                            elif x1[0] != i5:
                                pass
                        subdic[i5] = stsame.copy()
                        stsame.clear()
                    superdic[i3] = subdic.copy()
                    subdic.clear()

                self.multiverse = superdic

            elif all(isinstance(x , Timeline) for x in tl_list) == False:
                raise Exception("Multiverse can carry only timeline object")

        elif len(tl_list) == 0:
            self.Multiverse = {}














        
class Space_Stone(infinity_Stones): 
    __name = "Space Stone"
    #1.Teleport object (Export object) to here  2.create black holes 

    def __init__(self, Owner, location, Object, Color = "Blue", Ability= "Travel between places instantaneously" ):
        super().__init__(Owner, location, Object, Color, Ability)
        
    def Teleport(self , Origin  ,Destination , what = set): # When you can split yourself ,the spuls object will be diffrent;therefore, your life object will be diffrent
        if all(isinstance(x , str) for x in what) == True:
          pass
        elif all(isinstance(x , str) for x in what) == False:
          print("Must be a name")
          
        if len(Origin) == len(Destination) == len(what):
          pass
        else : 
          print("The len is not equal")
          
        for O ,D ,W in zip(Origin , Destination , what):
          print(f"{W} have travel from {O} to {D}")
    
    def SingleOrigin(self , des , wh = set, ori = str): #Multiple Destination  
        tlst = []
        for i in range(len(des)):
          tlst.append(ori)
        self.Teleport(tlst , des , wh)
    
    def SingleDestination(self , ori , wh = set, des = str): #Multiple origin 
        tlst = []
        for i in range(len(ori)):
          tlst.append(des)
        self.Teleport(ori , tlst , wh)
    
    def SingleDesOri(self ,ori = str, des = str, wh = set):
        tlst1 = []
        tlst2 = []
        for i in range(len(wh)):
          tlst1.append(ori)
          tlst2.append(des)
        self.Teleport(tlst1  , tlst2 , wh)
        
          
    def TeleportOwner(self , ori = str , des = str):
        self.Teleport([ori] , [des] , {self.Owner})
        
    
        

    
        
class Mind_Stone(infinity_Stones):
    #Read mind 
    __name = "Mind Stone"

    def __init__(self, Owner, location, Object, Color = "Yellow", Ability = "Control Minds"):
        super().__init__(Owner, location, Object, Color, Ability)

    def ControlState(self, Target, time):
        checklst=  []
        for k,t in zip(Target , time):
            if t <= 10 :
                Mindstatus = False
            elif t > 10 :
                Mindstatus = True
            Tartuple = (k  , t , Mindstatus )
            checklst.append(Tartuple)

        return  MindType(checklst)
      
    def ControlOrder(self ,Minded, order = dict):
        OrderList = []
        Returnlst=  []
        if isinstance(Minded , MindType) == True:
            pass
        elif isinstance(Minded , MindType) == False:
            return "Reject the order"
        for t in Minded.dt:
            if t[2] == True:
                OrderList.append(t[0])
            elif t[2] == False:
                pass
        for k in OrderList:
            Order = order[k]
            tup = (k , Order)
            Returnlst.append(tup)

        return Returnlst
        

class Soul_Stone(infinity_Stones):
    def __init__(self, Owner, location, Object, Color = "Orange", Ability = "Control Souls"):
        super().__init__(Owner, location, Object, Color, Ability)
        self.__Pool = set()
    
    # Identify spirit (check at the state), resurrect (Change states) , split spirit (Copied object ,and make the state to "s" and the control status to T) , control (check the control status and make it to T)
    # Souls have 3 states : 1.Split 2.Death 3.Alive
    def check_state(self , souls):
        Anslst = []
        dicti = {"s" : "split" , "d" : "death" , "a" : "alive"}
        for i in souls :
          statekey = i.state
          stateval = dicti[statekey]
          tupans = ((i.name).pop() , stateval)
          Anslst.append(tupans)
        return Anslst
        
    def check_controlStatus(self , souls):
        Anslst = []
        for i in souls :
          tupans = (i.name , i.control_status)
          Anslst.append(tupans)
        return Anslst
    
    def change_state(self , souls , new_state):
        Anslst = []
        if len(souls) == len(new_state):
          pass
        elif len(souls) != len(new_state):
          return "you must to identify the new state for all the souls"
        if new_state in ["d" , "s", "a"]:
          pass
        elif new_state not in ["d" , "s", "a"]:
          return "The State have only 3 state , {s : Split , d : death , a : alive}"
          
        for i,k in zip(souls , new_state):
          i.state = k
          Anslst.append(i)
        return Anslst
        
    def show_Souls(self , souls):
      Anslst = []
      for i in souls:
        tup = (i.name , i.control_status , i.state)
        Anslst.append(tup)
      return Anslst
      
    def Split_Souls(self , numcop):
        Anslst = []
        #SplitSoul = Soul(name = self.Owner  , control_status = True , state = "s")
        for i in range(numcop):
          SplitSoul = Soul(name = self.Owner , control_status = True , state = "s" , numSplit = i+1)
          Anslst.append(SplitSoul)
        return Anslst
        
    def change_ControlStatus(self, souls ,new_state):
        Anslst = []
        if len(souls) == len(new_state):
          pass
        elif len(souls) != len(new_state):
          return "you must to identify the new control status for all the souls"
        if all(isinstance(x, bool) for x in new_state) == True:  #New Knowledge
          pass
        elif all(isinstance(x, bool) for x in new_state) == False:
          return "the control status of each soul must be boolean "
        for i,k in zip(souls ,new_state):
          i.control_status = k
          Anslst.append(i)
        return Anslst
          
    def trapped(self , souls):
      World = self.__Pool
      for i in souls:
        i.control_status = True
        World.add(i)
      return World
      
    def Show_trapped(self):
      world = self.__Pool
      show = world.copy()
      Ans = self.show_Souls(show)
      return Ans
    
    def RemovePool(self , souls):
      World = self.__Pool
      for k in souls:
        World.remove(k)
      return World
      
      
class Reality_Stone(infinity_Stones):
    def __init__(self, Owner, location, Object, Color = "Red", Ability = "Alter reality and matter"):
        super().__init__(Owner, location, Object, Color, Ability)

    def show_reality(self , World = list):
        Anslst = []
        Realdict=  {"r" : "real" , "i" : "illusion"}
        if all(isinstance(w , Reality) for w in World) == True:
            pass
        elif all(isinstance(w , Reality) for w in World) == False:
            return "Reality stone can only alter reality object"
        for w  in World:
            tup = (Realdict[w.state] , w.location , w.Temp , w.theme)
            Anslst.append(tup)
        return Anslst

    def create_Illusion(self , location = list , theme = list , timeIllu = list , Temp = list , lifelist=  list , matter_list = list): #If you don't have timeIIlu for that reality so  put "None" for that reality in the list
        Worldlst = []

        if len(location) == len(theme) == len(Temp) == len(lifelist) == len(matter_list) == len(timeIllu):
            pass
        else:
            return "length of each list must to be the same in order to create n reality"

        for l, t, tI , T , lif , mat in zip(location , theme, timeIllu , Temp , lifelist , matter_list):
            if all(isinstance(lif , list)) == True and all(isinstance(mat , list)) == True:
                pass
            else:
                return "the element in lifelist or matter_list should be list"
            for lifI in lif:
                if lifI.state == "i":
                    pass
                elif lifI.state != "i":
                    return "In Illusion reality, all life or matter object should be illusion (state = i) "

            for matI in mat:
                if matI.state == "i":
                    pass
                elif matI.state != "i":
                    return "In Illusion reality, all life or matter object should be illusion (state = i) "

            World = Reality(l , t , "i" , tI , T , lif , mat)
            Worldlst.append(World)

        return Worldlst
    #Create REAL reality requires all of the six infinity stones

    def inactivate(self , Worlds = list , Worlds_before = list): #Inactivate the Reality stone and make the illusion reality become normal
        Ans = []
        if len(Worlds) == len(Worlds_before):
            pass
        elif len(Worlds) != len(Worlds_before):
            return "length of each list must to be the same in order to RECREATE n REAL reality"
        if all(isinstance(i , Reality) for i in Worlds) == True:
            pass
        elif all(isinstance(i , Reality) for i in Worlds) == False:
            return "Reality stone can only inactivate reality object, worlds."

        for k in Worlds_before:
            if k.state == "r":
                pass
            elif k.state != "r":
                return "All before world should be REAL realities"


        for i,k in zip(Worlds ,Worlds_before):
            if k.state == "r":
                pass
            elif k.state != "r":
                return "All before world should be REAL realities"
            for lif1 , mat1 in zip(k.lifelist , k.matter_list):
                if lif1.state == "i":
                    return "All life in real realities must be REAl "
                elif lif1.state == "r":
                    pass
                if mat1.state == "i":
                    return "All matter in real realities must be REAL"
                elif mat1.state == "r":
                    pass

            i.state = "r"
            for lif in i.lifelist:
                if lif.state == "i":
                    i.lifelist.remove(lif)
                elif lif.state == "r":
                    pass

            for mat in i.matter_list:
                if mat.state == "i":
                    i.matter_list.remove(mat)
                elif mat.state == "r":
                    pass

            i.theme = k.theme
            i.location = k.location
            i.timeIllu = k.timeIllu
            i.Temp = k.Temp
            Ans.append(i)

        return Ans

    def create_Matter(self , Name = str  ,Mass = float , Shape = str , location = str ,matterState = str ,state = str, **kwargs):
        return Matter(Name , Mass , Shape , location , matterState , state , **kwargs)

    def Function_Matter(self , expr = str):
        return RealityType(expr)

    def Transmute(self , Matters = list , Shapes = list , matterStates = list): #paramter : Shape , matterState , MatterWantToChange #for the abilities of the matter you can create the expr for it as the same as before transmute
        translist =  []
        if len(Matters) == len(Shapes) == len(matterStates):
            pass
        else:
            return "length of each list must to be the same in order to transmute n matter"

        for O , s , ms in zip(Matters , Shapes , matterStates):
            if isinstance(O , Matter) == True or isinstance(O , Life) == True:
                pass
            else:
                return "Matter that can be transmute by Reality stone is Matter object or Life object"

            O.Shape = s
            O.matterState = ms
            translist.append(O)

        return translist
        #The abillity of both life and matter object still be the same. Transmute() cannot change soul or mind of life object

    def Copied_Matter(self, Matters = Matter , num_copied =  int):
        Matlist = []
        for i in range(num_copied):
            Mat = Matters.copy()
            Matlist.append(Mat)
        return Matlist

    def create_illusionMatter(self, Matters): #Matter or life object
        if isinstance(Matters , Matter) == True or isinstance(Matters , Life) == True:
            pass
        else:
            return "Reality stone can only create matter or life object"
        Matters.state = "i"
        return Matters

class Time_Stone(infinity_Stones):
    def __init__(self, Owner, location, Object, Color = "Green", Ability = "Control and manipulate time"):
        super().__init__(Owner, location, Object, Color, Ability)

    def Forward_Reverse(self , Tlo = Timeline , tw = Time , objlst = list , world  =Reality , indexlst = []):
        tl = Tlo.timeline
        if tw in list(tl.keys()):
            pass
        elif tw not in list(tl.keys()):
            return "The wanted time must be in the timeline"
        if Tlo.World == world:
            pass
        elif Tlo.World != world:
            return "World should be the same"
        if len(indexlst) == len(objlst):
            pass
        elif len(indexlst) != len(objlst):
            return "Every object in the list should have an indexes"

        objlsttl = tl[tw]


        #print(objlsttl)
        for l , i in zip(objlst , indexlst):
            #print(objlsttl[i].__name__)
            pyjack.replace_all_refs(l , objlsttl[i])

    def Change_TimeRate(self , objlst = list , world = Reality, tr = list): #This include slow, freeze or increase time rate
        if len(tr) == len(objlst):
            pass
        elif len(tr) != len(objlst):
            return "Every object in this list need there's new time rate"

        for i,r in zip(objlst , tr):
            if i in world.lifelist or i in world.matter_list:
                pass
            else:
                return "World should be the same"
            i.timerate = r

    def FreezeTime(self, objlst = list , world = Reality):
        lst = []
        for i in range(len(objlst)):
            lst.append(0)
        self.Change_TimeRate(objlst= objlst , world = world , tr = lst)

    def Observe_Timeline(self , World = Reality):
        # Start time should all be the same in all possible timeline in the Multiverse
        Multiverse = World.Multiverse
        for ele in Multiverse:
            print(ele)

    def Timeloop(self , st = Time , ft= Time ,expr = str , interObj = list ,tS = list,World = Reality, **kwargs):
        tl = Timeline(World)
        lst = interObj.copy()
        lsti = interObj
        lst.append(World)
        ind = []
        for i in range(len(interObj)+1):
            ind.append(i)
        ln = 1
        while True:
            print(f"loop rounds, {ln}")
            tl.Interaction(tl , st , ft, expr, lsti , tS , **kwargs)
            print(tl.timeline)
            print("After interact" , lst)
            #for i in r
            #ind = [0,1,2]
            #self.Forward_Reverse(tl , st , lst , World,ind)
            inp = input("Whether you will stop this loop? ")
            #ln += 1
            if inp == "y":
                break
            elif inp == "n":
                self.Forward_Reverse(tl , st , lst , World,ind)
                ln += 1
                print("Loop back!" , lst)
                print("")
            else:
                return "Error"


        print("End the loop!")




    '''
            #lst.append(World)
            print("*&")
            #print((tl , st , ft, expr, interObj , tS , kwargs))
            print(World.propertime)
            print(tl.Interaction(tl , st , ft, expr, lsti , tS , **kwargs))
            print(tl.timeline)
            for i in range(len(lst)):
                indexlst.append(i)
            print(len(lst))
            print(len(indexlst))
            print(lst[-1])
            print(self.Forward_Reverse(tl , st , lst , World,indexlst))
            print("&&&&&&&&& Time Stone &&&&&&&&&")
            print(lst[-1])
            print(lst[-1].propertime)
            print(self.Forward_Reverse(tl , st , [World] , World,[-1]))
            print(World.propertime)
            print(World)
            lst = interObj
            inp = input("Whether you will stop this loop? ")
            if inp == "y":
                break
            elif inp == "n":
                tl.timeline  = {}
                print(lst)
            else:
                tl.timeline.clear()

            tl.timeline = {}
            lst.pop(-1)
            indexlst.clear()
        print("The loop is over")
        return tl
'''

class Power_Stone(infinity_Stones):
    def __init__(self, Owner, location, Object, Color = "Purple", Ability = "Manipulate energy; increased strength"):
        super().__init__(Owner, location, Object, Color, Ability)

    def Pain_inducement(self , life = Life):
        lim_s = life.Limit_Strength
        lim_p = life.Pain_limit
        #s = life.Strength
        k = life.__dict__.copy()
        r = rand.randint(int(lim_p) , int(lim_s))
        k["Strength"] = r
        life.__init__(**k)

    def Overload_Strength(self , life = Life):
        lim_s = life.Limit_Strength
        k = life.__dict__.copy()
        addi = lim_s + 50
        r = rand.randint(int(lim_s) , int(addi))
        k["Strength"] = r
        life.__init__(**k)

    def Projection(self , target = Life):
        lim_s = target.Limit_Strength
        s = target.Strength
        k = target.__dict__.copy()
        addi = lim_s + 50
        r = rand.randint(int(s) , int(addi))
        k["Strength"] = r
        target.__init__(**k)

    def Matter_destruction(self , target = Matter or Life):
        if isinstance(target , Matter) == True:
            k = target.__dict__.copy()
            k["matterState"] = "cr"
            k["Shape"] = "Pieces"
            target.__init__(**k)
        if isinstance(target , Life) == True:
            k = target.__dict__.copy()
            soul = k["Souls"]
            k2 = soul.__dict__.copy()
            k2["state"] = "d"
            soul.__init__(**k2)
            target.__init__(**k)

    def Planet_destruction(self , World = Reality):
        liflst = World.lifelist
        matlst = World.matter_list
        klst = []
        for i in liflst:
            klst.append(i)
        for i1 in matlst:
            klst.append(i1)
        for i2 in klst:
            self.Matter_destruction(i2)
        #map(lambda x : self.Matter_destruction(x) , klst)
        k = World.__dict__.copy()
        k["lifelist"] = []
        k["matter_list"] = []
        World.__init__(**k)














        
        
        
          
          
          
  
  
if __name__ == '__main__':

    S1 = Space_Stone("Loki" , "Asgard", "Tesserract")
    S1.show_Color()
    S1.show_StonesInfo()
    S1.Teleport("Earth" , "Coruscant", [])
    print(Space_Stone._Space_Stone__name)

    S2  =Mind_Stone("Vision" , "Earth" , "Scepter")
    Contorllst =  S2.ControlState(Target = ["Tony" , "James"] , time =[15,20])
    print(Contorllst.dt)
    print(type(Contorllst))
    print(S2.ControlOrder(Contorllst , {"Tony" : "Kill President" , "James" : "build the Pyramid" , "Luis" : "Open the portal"}))
    print(S2.ControlOrder([('Tony', 15, True), ('James', 20, True)] , {"Tony" : "Kill President" , "James" : "build the Pyramid" , "Luis" : "Open the new store"}))

    S3 = Soul_Stone("Odin" , "Asgard" , "Asgard pool")
    Souls1 = Soul("Tony" , False , "a")
    Souls2 = Soul("Steve" , False , "d")
    print(S3.show_Souls([Souls1 , Souls2]))
    a = (S3.change_ControlStatus([Souls1 , Souls2] , [True , True]))
    print(S3.check_controlStatus(a))
    print(S3.trapped([Souls1 , Souls2]))
    print(S3.Show_trapped())
    print(S3.RemovePool([Souls2 , Souls1]))
    print(S3.Show_trapped())
    L1 = Life(Name = "John" , Mass = 45 , Shape = "Human shape" , location = "Earth" , matterState = "mul" ,state = "r" , MindState= False , age = 17 ,Souls= Soul("John" , False , "a"), Strength=50 , Limit_Strength=100, propertime = Time(2022,4,16,12,5,34) , timerate = 10 , Pain_limit= 70)
    M1 = Matter(Name = "Laptop" , Mass = 2  ,Shape = "laptop shape" , location = "Earth" , matterState= "s" , state = "r", propertime = Time(2022,4,16,12,5,34)  ,timerate = 10)
    '''
    k = L1.__dict__.copy()
    #k["Limit_Strength"] = L1._limit_strength
    k["Strength"] = 100
    L1.__init__(**k)
    print(L1)
    print(L1.Souls.state)
    '''
    W1 = Reality(location = "Earth" , theme = "New york" , state = "r" , Temp= 20 , lifelist = [L1] , matter_list = [M1] , propertime = Time(2022,4,16,12,5,34) , timerate = 10  )
    S6 = Power_Stone("Thanos" , "Xandar" , "Orb")
    S6.Planet_destruction(W1)
    print(L1.Souls.state)
    print(M1.Shape)
    print(W1.matter_list)

'''

#Mat1 = Matter(Name = "Macbook" , Mass = 12 , Shape = "Notebook shape" , location = "Earth" , matterState = "s" ,state = "r", cpu = 1500 , ram = 16 , owner = "James Madison")
#print(Mat1.Abillity)
exp1 = """ 
if cpu == 1500 and ram == 16:
    print(cpu + ram)
else:
   print(None)
"""

exp2 = "a = cpu + ram\nprint(a+ 10)"
exp3 = """
def hello(cpu , ram , owner):
    if cpu == 1500 and ram == 16:
        print(f"Hello {owner}")
    else:
        print("Oh")
"""
exp4 ="""
if cpu == 1500 and ram == 16:
    print(f"Hello {owner}")
else:
    print("Oh")


"""

exp5 = """
if len(kill_lst) == num:
    pass
else:
    print("The number of the bullet must equal to the shooting target")
for i in kill_lst:
    if i.soul.state == "a":
        i.soul.state = "d"
    elif i.soul.state != "a":
        print("The traget should alive first!")
for k in kill_lst:
    if k.soul.state == "d":
        j = "death"
        print(k.Name + " is " + j)
"""
#kLst = [Life("Maria" ,"Earth",50,"Human shape","s","r",  False ,25, Soul("Maria" , False , "a")) , Life("Jim" ,"Volmir",45,"Human shape","s","r",  False ,24, Soul("Jim" , False , "a") )]
#print(exp2)
#Mat2 = Matter(Name = "Killer Weapon" , Mass = 20 , Shape = "Gun shape" , location = "Volmir" , matterState = "s" ,state = "r", num = 2 , kill_lst = [Life("Maria" , False , "Earth" ,"r", 50, Soul("Maria" , False , "a")) , Life("Jim" ,False , "Wakanda" ,"r", 41 , Soul("Jim", False , "a" ))])
#print(exp2)
##Matrun = Mat1.run(RealityType(exp4))
#Matrun2 = Mat2.run(RealityType(exp5))
#Matrun3  = Mat3.run(RealityType(exp5))
#print(kLst[0].soul.state) #Output : d
#print(Matrun)
#Matrun1 = Mat1.run(RealityType("cpu + ram"))
#print(Matrun1)
#S4 = Reality_Stone("The Collector" , "Collector museum" , "Aether")
#Mat41 = S4.create_Matter(Name = "Killer Weapon" , Mass = 20 , Shape = "Gun shape" , location = "Volmir" , matterState = "s" ,state = "r", num = 2 , kill_lst = [Life("Maria" ,"Earth",50,"Human shape","s","r",  False ,25, Soul("Maria" , False , "a")) , Life("Jim" ,"Volmir",45,"Human shape","s","r",  False ,24, Soul("Jim" , False , "a"))])
#exprS4 = S4.Function_Matter(exp5)
#Mat41.run(exprS4)
explif = """
if "Blast" in kw["power"] and kw["blastpower"] >= 15:
    ValueFromExp  = Uti.UpdateVallst(value = kw["blastpower"] + 50 , lst = ValueFromExp.copy()).copy() #Don't Use a Variable ! Just put it directly
    #ValueFromExp.append(kw["blastpower"] + 50)
    
    
else:
    lst1 = ValueFromExp.copy()
    lst1.append(kw["blastpower"])
    ValueFromExp  = lst1
    #ValueFromExp.append(kw["blastpower"])
"""
#Uti1 = Utility
lifelst = [Life(Name= "James" , location= "Earth" , Mass=45 , Shape=  "Human shape" , matterState="s" , state=  "r" , MindState= False , age= 13 , Souls= Soul("James" , False , "a") ,propertime= Time(2022 , 3 ,8,11,50,10) ,timerate=10 ,exprlist=[RealityType(explif)],
                power = ["Blast" , "Transmute reality"] , blastpower = 18  )]
Matterlst=  [Matter(Name = "Ultron" , Mass= 150 , Shape=  "Human Shape" , location = "Earth" , matterState = "s" , state = "i" ,
                    propertime= Time(2022 , 3 ,8,11,50,10) , timerate = 10 , exprlist=[RealityType(None)]  )]
w1 = Reality(location = "Earth" , theme = "Roman empire" , state = "i" , Temp = 25 , lifelist = lifelst ,
             matter_list= Matterlst, propertime =Time(2022 , 3 ,8,11,50,10) , timerate = 10 )


# for i in lifelst:
#     i.run(i.exprlist[0])
#     print(i.ValueFromExp)


interexp = """
import itertools

obj1 = interObj[0]
obj2 = interObj[1]
lo1 = inilen[0]
lo2 = inilen[1] 
St1 = {st : [World.dictSlice(obj1 , lo1), World.dictSlice(obj2 , lo2)]}
timeline.update(St1)

obj1.ValueFromExp.clear()
timeline.update({ tS[0] : [World.dictSlice(obj1 , lo1), World.dictSlice(obj2 , lo2)]}) #World.dictsSlice is required for taking the right dictionary 

obj1.run(obj1.exprlist[0]) 
#Try to format the expression of the abillity to the real code HERE!
#%s
del obj1.__dict__["lst1"]
timeline.update({ tS[1] : [World.dictSlice(obj1 , lo1), World.dictSlice(obj2 , lo2)]}) #Note : What happen when timeline has been updated?


blastvalue = obj1.ValueFromExp[0]
if blastvalue >= 18:
    obj2.Shape = "Pieces"
    timeline.update({ tS[2] : [World.dictSlice(obj1 , lo1), World.dictSlice(obj2 , lo2)]})
else:
    timeline.update({ tS[2] : [World.dictSlice(obj1 , lo1), World.dictSlice(obj2 , lo2)]})


timeline.update({ft : [World.dictSlice(obj1 , lo1), World.dictSlice(obj2 , lo2)] }) #**Key**
World.propertime = ft                                                               #**Key**
"""#% lifelst[0].exprlist[0].dt

interexp2 = """
import itertools
obj1 = interObj[0]
obj2 = interObj[1]

Objlst = interObj


#print(obj1.ValueFromExp)
tObj.Update(tS = st , interObj = Objlst )


obj1.ValueFromExp.clear()
#print(obj1.ValueFromExp)
#t2.Update([obj1 , obj2 , World] , {tS[0] : [World.dictSlice(obj1 , lo1), World.dictSlice(obj2 , lo2) , World.dictSlice(World , loW)]} ) #World.dictsSlice is required for taking the right dictionary 
tObj.Update(tS = tS[0] , interObj = Objlst)



obj1.run(obj1.exprlist[0]) 


#Try to format the expression of the abillity to the real code HERE!
#%s

#print(obj1.ValueFromExp)
#t2.Update([obj1 , obj2 , World] , {tS[1] : [World.dictSlice(obj1 , lo1), World.dictSlice(obj2 , lo2) , World.dictSlice(World,loW)]} ) #World.dictsSlice is required for taking the right dictionary 
tObj.Update(tS = tS[1] , interObj = Objlst)



blastvalue = obj1.ValueFromExp[0]
if blastvalue >= 18:
    obj2.Shape = "Pieces"
    #t2.Update([obj1 , obj2 , World] , {tS[2] : [World.dictSlice(obj1 , lo1), World.dictSlice(obj2 , lo2) , World.dictSlice(World,loW)]} ) #World.dictsSlice is required for taking the right dictionary 
    tObj.Update(tS = tS[2] , interObj = Objlst)
    
else:
    #t2.Update([obj1 , obj2 , World] , {tS[2] : [World.dictSlice(obj1 , lo1), World.dictSlice(obj2 , lo2) , World.dictSlice(World,loW)]} ) #World.dictsSlice is required for taking the right dictionary 
    tObj.Update(tS = tS[2] , interObj = Objlst)

tObj.Update(tS = ft , interObj = Objlst)
#t2.Update([obj1 , obj2 , World] , {ft : [World.dictSlice(obj1 , lo1), World.dictSlice(obj2 , lo2) , World.dictSlice(World,loW)]} ) #World.dictsSlice is required for taking the right dictionary 
"""#% lifelst[0].exprlist[0].dt

inter2 = """
print("Hello World")

"""
#t1 = Timeline(World = w1)
Ft = Time(2022,3,8,14,10,5)
#t1.Interaction( st = w1.propertime , ft =  Ft, expr = interexp,interObj = [lifelst[0] , Matterlst[0]] , tS = [Time(2022 , 3 ,8,12,30,10) ,Time(2022 , 3 ,8,12,50,5) , Time(2022 , 3,8,13,20,5)  ] , inilen = [len(lifelst[0].__dict__) , len(Matterlst[0].__dict__) , len(w1.__dict__)] )
#print(t1.timeline)
print(w1.propertime.hour)
#print(t1.timeline[Time(2022 , 3,8,13,20,5)])
lifelst[0].__dict__.update({"__builtins__" : {"James" : "male" , "Maria" : "female"}})
print(lifelst[0].__dict__)
#print(lifelst[0].location)
l1 = Life(Name= "James" , location= "Earth" , Mass=45 , Shape=  "Human shape" , matterState="s" , state=  "r" , MindState= False , age= 13 , Souls= Soul("James" , False , "a") ,propertime= Time(2022 , 3 ,8,11,50,10) ,timerate=10 ,exprlist=[RealityType(explif)],power = ["Blast" , "Transmute reality"] , blastpower = 20)
#print(l1.Abillity)
print("***")
print(Matterlst[0].Shape)
print("**")
S5 = Time_Stone("Dr.Strange" ,"Earth" , "Eye of Agamotto")
#t2 = Timeline(World = w1)
#S5.Timeloop(st = w1.propertime , ft =  Ft, expr = interexp2,interObj = [lifelst[0] , Matterlst[0]] ,tS = [Time(2022 , 3 ,8,12,30,10) ,Time(2022 , 3 ,8,12,50,5) , Time(2022 , 3,8,13,20,5)  ],World = w1,inilen = [len(lifelst[0].__dict__) , len(Matterlst[0].__dict__) , len(w1.__dict__)] )
#print(lifelst[0])
#S5.FreezeTime([lifelst[0]] , w1)
#print(lifelst[0])
#print(w1)

'''
'''
t2 = Timeline(World = w1)
t2.Interaction(st = w1.propertime , ft =  Ft, expr = interexp2,interObj = [lifelst[0] , Matterlst[0]] ,tObj=t2, tS = [Time(2022 , 3 ,8,12,30,10) ,Time(2022 , 3 ,8,12,50,5) , Time(2022 , 3,8,13,20,5)  ]) #, inilen = [len(lifelst[0].__dict__) , len(Matterlst[0].__dict__) , len(w1.__dict__)]  , t2 = t2)
print(t2.timeline)
print(Matterlst[0].Shape)
print("See this +++")
print(t2.timeline[Time(2022 , 3 ,8,12,30,10)])
ti = t2.timeline
S5 = Time_Stone("Dr.Strange" ,"Earth" , "Eye of Agamotto")
#print(lifelst[0])
#obj1 = lifelst[0]
print(lifelst[0])
print(Matterlst[0])
obj2 = S5.Forward_Reverse(t2 , Time(2022 , 3 ,8,12,30,10) ,[lifelst[0] ,Matterlst[0]], w1 , [0,1])
print(lifelst[0])
print(Matterlst[0])
a = Matterlst[0]
print(a.Shape)
print(w1)
S5.FreezeTime([lifelst[0]] , w1)
print(lifelst)
'''
'''
#Check whether each interobj and worlds have the same according Time() as the key
timewant = Time(2022 , 3 ,8,12,50,5)  #You can adjust Time based on the tS lis (arguments in t2.interaction())

for i in ti[timewant]:
    if isinstance(i , dict) == True:

        pt = i["propertime"]
        if i["propertime"] == timewant:
            print(f"{i}, pt = {pt} , timewant =  {timewant}")
        elif i["propertime"] != timewant:
            print(f"{i} , Not match!")
    else:
        pass


print("**$")
#print(Matterlst[0].Abillity)
##print(a[0]["Name"])
print(Ft)
print(lifelst[0].ValueFromExp)
print(t2.World.propertime)

S5 = Time_Stone("Dr.Strange" ,"Earth" , "Eye of Agamotto")
S5.Forward2(t2 , Time(2022 , 3 ,8,12,50,5) ,[lifelst[0]], w1 , [0])
print(lifelst[0].propertime)


#print(t1.timeline[Ft][1])
a = (Matterlst[0].__dict__)
b= (lifelst[0].__dict__)

'''
'''

print("******")
#print(b)
dic1 = l1.__dict__
print(len(dic1))
exe1 = """
#%s
l1.run(exp)
""" #% l1.exprlist[0].dt
#print(b)
exec("print(dir())" ,{"l1": l1 , "exp" : l1.exprlist[0] } ) #Output : dict(itertools.islice(d.items(), n))
exec(exe1 , {"l1": l1, "exp" : l1.exprlist[0]  })
#print(l1.__dict__)
dic = l1.__dict__

print(dic["ValueFromExp"][0])
print(dic["kw"]["power"][1])
#print(dic["__builtins__"])

#slidic = dict(itertools.islice(dic.items(), 14 )) #slice Dictionary in python ,USE in t1.timeline
#print(slidic)
if "__builtins__" in dic:
    del dic["__builtins__"]
else:
    pass
print(dic)
'''

#print(dic[""])
#ti = {}
#ti.update({Time(2022 , 3 ,8,13,40,5) : [a, b] })
#print(ti)
#print(b)
#print(t1.timeline[Time(2022 , 3 ,8,13,40,5)][1])
'''
#Time object should have __repr__ for represent the value. So we can use the str (return from the __repr__()) to check what time object match what we desire.
'''

