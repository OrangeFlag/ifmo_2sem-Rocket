from math import floor, ceil, exp
#selfig сюда мы вносим переменные в разных форматах числовое константное значения или функция или массив данных,
# после чего все это преобразуется в массив заданной длинны(в зависимости от delta_t) с точностью до 0,5 сек
#Time
class Config:
    t_mas = []
    Accuracy = []
    G = []
    #Rocket
    m_rocket = [] #in kg
    S_rocket = []
    Coefficient_resistance = []  # Коэффицент лобового сопротивления
    #Calculated
    distance = []
    a_rocket = []
    u_rocket = []
    #~Rocket

    #Fuel
    m_fuel = []
    u_fuel = []
    c_fuel = []
    #~Fuel

    #Planet
    M_planet = []
    R_planet = []
    Mol_gas = []
    #Calculated
    Temperature = [] #one string in mas (func (h))
    Atmospher_density = [] #Плотность атмосферы
    #~Planet
    R = 8.31445984848488


    #def
    def Normalization_config(self):
        t = self.t_mas[len(self.t_mas)-1]
        self.t_mas = [0]
        step = 1/self.Accuracy[0]
        i = 0
        while i < t * self.Accuracy[0]:
            self.t_mas.append(self.t_mas[i] + step)
            i += 1


        Var = [self.t_mas, self.m_rocket, self.a_rocket, self.u_rocket, self.S_rocket,
               self.u_fuel, self.m_fuel, self.c_fuel,
               self.distance,self.Atmospher_density, self.Mol_gas,
               self.Coefficient_resistance, self.Temperature]
        for x in Var:
            Temp = x[:]
            Repeat = [int(floor((t * self.Accuracy[0]) / len(x))), int(ceil((t * self.Accuracy[0]) / len(x)))]
            if Repeat[0] == 0:
                Repeat[0] = 1
            if Repeat[1] == 0:
                Repeat[1] = 1
            x.clear()
            for i in range(len(Temp)):
                for count in range(Repeat[i%2]):
                    if len(x) < t*self.Accuracy[0]:
                        x.append(Temp[i])


    def Calculate(self):
        delta_t = 1 / self.Accuracy[0]
        t = self.t_mas[len(self.t_mas) - 1] + self.Accuracy[0]
        F = self.G[0] * (self.m_fuel[0] + self.m_rocket[0]) * self.M_planet[0] \
            / ((self.R_planet[0] + self.distance[0]) ** 2)
        self.a_rocket[0] = (self.u_fuel[0] * self.c_fuel[0] * (self.m_fuel[0] != 0) - F) / (
        self.m_fuel[0] + self.m_rocket[0])
        self.Temperature[0] = max(1, self.Parse_Temperature(0))
        for i in range(1, int(self.Accuracy[0] * t)):
            F = 0
            self.distance[i] = self.distance[i - 1] + self.u_rocket[i - 1] * delta_t \
                               + self.a_rocket[i - 1] * delta_t ** 2 / 2
            self.u_rocket[i] = self.u_rocket[i - 1] + self.a_rocket[i - 1] * delta_t
            if (self.distance[i] < 0):
                self.distance[i] = 0
                self.u_rocket[i] = 0
            self.m_fuel[i] = self.m_fuel[i - 1] - self.c_fuel[i - 1] * delta_t
            if (self.m_fuel[i] < 0):
                self.m_fuel[i] = 0
            # Atmospher
            g = self.G[0]*self.M_planet[0]/(self.distance[i]+self.R_planet[0])**2
            #fixme
            self.Temperature[i] = max(1, self.Parse_Temperature(i))

            self.Atmospher_density[i] = self.Atmospher_density[i-1]* exp(-self.Mol_gas[i]*g*(self.distance[i] - self.distance[i-1])/(self.R*self.Temperature[i]))
            F += self.Coefficient_resistance[i] / 2 * self.Atmospher_density[i] * self.u_rocket[i] ** 2 * self.S_rocket[i]
            # ~Atmospher

            F = self.G[0] * (self.m_fuel[i] + self.m_rocket[i]) * self.M_planet[0] / (
            (self.R_planet[0] + self.distance[i]) ** 2)

            self.a_rocket[i] = (self.u_fuel[i] * self.c_fuel[i] * (self.m_fuel[i] != 0) - F) / (
            self.m_fuel[i] + self.m_rocket[i])
    def Parse_Temperature(self, i):
        from Parsers import eval_
        string = self.Temperature[i]
        string = string.replace('h', str(self.distance[i]))
        string = string.replace('H', str(self.distance[i]))
        string = eval_(string)
        return string

