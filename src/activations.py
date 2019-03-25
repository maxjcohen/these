class Activation:
    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)