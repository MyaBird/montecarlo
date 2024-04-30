import numpy as np

class BitString:
    """
    Simple class to implement a config of bits
    """
    def __init__(self, N):
        self.N = N
        self.config = np.zeros(N, dtype=int) 

    def __repr__(self):
        return "%s"%(self.config)

    def __eq__(self, other):        
        return self.config == other.config

    def __str__(self):
        return "%s"%(self.config)
    
    def __len__(self):
        return len(self.config)

    def on(self):
        on = 0
        for i in range(len(self.config)):
            if self.config[i] == 1:
                on += 1
        return on
    
    def off(self):
        off = 0
        for i in range(len(self.config)):
            if self.config[i] == 0:
                off += 1
        return off
    
    def flip_site(self,i):
        if self.config[i] == 1:
            self.config[i] = 0
        else:
            self.config[i] = 1
    
    def int(self):
        integer = 0
        for i in range(0, self.N):
            integer *= 2
            integer += self.config[i]
        return integer
 
    def set_config(self, s:list):
        self.config = np.array(s)
        
    def set_int_config(self, dec:int):
        n = dec
        if dec >= 0:
            for i in range(self.N-1, -1,-1):
                self.config[i] = n % 2
                n = n // 2