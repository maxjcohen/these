class Layer:
    def __init__(self):
        self.X = None
        self.A = None
        
        self.activation = None
        
    def d_activation(self):
        if self.A is None:
            raise RuntimeError("This layer needs a forward pass before computing a gradient")
        return self.activation.d(self.A)
    
    def __call__(self, X):
        return self.forward(X)
    
    def __sizeof__(self):
        return sys.getsizeof(self.W) + sys.getsizeof(self.b)