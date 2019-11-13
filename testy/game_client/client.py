"""
1. Create virtual environment:
mkdir game
python -m venv game
cd game
Scripts\activate.bat

2. Install pip and PyGame:
python -m pip install --upgrade pip
pip install pygame

3. Run example
cd ..
python client.py

4. Do all TODOs

5. Close virtual environment:
cd game
Scripts\deactivate.bat
"""

#import xmlrpclib
import xmlrpc.client
import random
import visualizer
import xml.etree.ElementTree as ET

class Agent(object):
    def __init__(self, filename):
        # TODO 1 - nacist data z configuracniho xml souboru (nazev v parametru
        # filename)
        self.filename = filename
        # TODO 2 - vytvorit instancni promenne (login, data, vizualizer, 
        # gameserver)
        self.root = ET.parse(self.filename)
        self.login = self.root.find("login").text
        self.data = []
        self.visualizer = visualizer.Visualizer()
        self.url = self.root.find("url").text
        self.gameserver = xmlrpc.client.ServerProxy(self.url)
        # login - naplnit daty prectenymi z XML
        # data - prazny list, kde budou ukladana data ze serveru
        # visualizer - instance tridy v visualizer.Visualizer
        # gameserver - pripojit se k XML-RPC serveru (url v XML souboru)
        # TODO 3 - na serveru zavolat metodu add_player s parametrem login
        # (v instancni promenne login)
        self.gameserver.add_player(self.login)
                                
    
    def action(self):
        # TODO 4 
        self.data = self.gameserver.make_action(self.login, "look", "")
        self.visualizer.visualize(self.data)

    
    def __str__(self):
        # TODO 5 - Vrati retezec, ktery bude hezkou reprezentaci ulozenych
        # dat ulozenych v instancni promenne data.
        s = ""
        for item in self.data:
            s += str(item)
            s += '\n'
        return s

    def save_data(self):
        # TODO 6 - ulozi data do souboru data.txt
        f = open("output.txt", "a")
        s = ""
        for item in self.data:
            s += str(item)
            s += '\n'
        f.write(s)
        f.close()

class AgentRandom(Agent):
    # TODO 7 - tento agent bude dedit z agenta predchoziho a
    # upravi funkci action tak, ze akci bude "move" a v parametru
    # preda jeden ze smeru "north", "west", "south", "east". Tyto
    # smery bude vybirat nahodne (najdete vhodnou metodu z balicku
    # random)
    def __init__(self, filename):
        super().__init__(filename)

    def action(self):
        self.data = self.gameserver.make_action(self.login, "move", "")
        self.visualizer.visualize(self.data)

class AgentLeftRight(Agent):
    # TODO 8 - tento agent bude chodit stale doleva, dokud nenarazi na prekazku.
    # V takovem pripade obrati svuj smer a pohybuje se stale doprava, nez take
    # narazi na prekazku.
    pass

def main():
    agent = None
    try:
        agent = Agent("config.xml")
        agent = AgentRandom("config.xml")
        #agent = AgentLeftRight("config.xml")
        while agent.visualizer.running:
            agent.action()
            print(agent)
        else:
            agent.gameserver.make_action(agent.login, "exit", "")

        agent.save_data()
    except KeyboardInterrupt:
        agent.gameserver.make_action(agent.login, "exit", "")


if __name__ == "__main__":
    main()
