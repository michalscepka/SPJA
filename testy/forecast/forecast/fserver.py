from xmlrpc.server import SimpleXMLRPCServer

class Forecast(object):
    #Reprezentuje predpoved. V instancnich promennych jsou reprezentovany hodnoty predpovedi.

    def __init__(self, description, wind_force, temperature):
        #Konstuktor predpovedi. Instancni promenne reprezentuji predana data.
        self.description = description
        self.wind_force = wind_force
        self.temperature = temperature

    def get_list(self):
        #Vraci trojici reprezentujici predpoved.
        return (self.description, self.wind_force, self.temperature)

class ForecastCalendar(object):
    """
    Reprezentuje predpovedi pro nekolik dni. Data predpovedi jsou ulozena ve
    slovniku. Klicem je datum, hodnotou pak instance tridy Forecast. Vkladani
    predpovedi metodou update_forecast je chraneno heslem, ktere je predano v
    konstruktoru. Startovaci data jsou tezz predana v konstruktoru.
    """
    
    def __init__(self, initial_values, password):
        #Konstruktor kalendare predpovedi. Instancni promenne reprezentuji predana data.
        self.initial_values = initial_values
        self.password = password

    def get_forecast(self, date):
        #Vrati predpoved pro zadane datum jako retezec. V pripade, ze pro dane
        #datum neexistuje predpoved. Vrati se retezec "No focecast".
        for item in self.initial_values:
            if(item == date):
                return (
                    str(self.initial_values[item].description) + " " + 
                    str(self.initial_values[item].wind_force) + " m/s " + 
                    str(self.initial_values[item].temperature) + "°C")
        return "No forecast"

    def update_forecast(self, password, date, description, wind_force, temperature):
        """
        Aktualizuje predpoved pro zadane datum. Akce je chranena heslem. Pokud
        heslo nesouhlasi s heslem, ktere je zadano v konstruktoru, neni mozno
        aktualizovat predpoved. v takovm priapde metoda vrati retezec "No
        update". Metoda muze aktualizovat stavajici predpoved nebo pridat novou.
        """
        if(self.password != password):
            return "No update"
        
        self.initial_values.update({ date : Forecast(description, wind_force, temperature)})

        return "Updated"

        
def main():

    # TODO Pridat do initial_state data predpovedi tak, aby je mohl klient precist.
    initial_state = { 
        "2012-11-05" : Forecast("rainy", 10.0, 25.0),
        "2012-11-06" : Forecast("sunny", 15.0, 26.0),
        "2012-11-07" : Forecast("windy", 11.0, 20.0),
        "2012-11-08" : Forecast("rainy", 10.0, 25.0) 
        }

    fcalendar = ForecastCalendar(initial_state, password = "master-of-weather")

    server_address = ('localhost', 10001)
    server = SimpleXMLRPCServer(server_address)
    server.register_instance(fcalendar)
    server.register_introspection_functions()
    print("Starting Weather XML-RPC server, use <Ctrl-C> to stop")
    server.serve_forever()

if __name__ == "__main__":
    main()
