class Signal(type):
    _instances = {}
    def __call__(self, name, *args, **kwds):
        inst = super().__call__(name, *args, **kwds)
        Signal._instances[name] = inst 
        return inst

class BaseSignal(metaclass=Signal):
    def __init__(self, name):
        self.name = name
        self.callbacks = []

    @classmethod
    def get_instance(cls, name):
        return BaseSignal._instances.get(name)

    def connect(self, callback):
        self.callbacks.append(callback)

    def emit(self, *args, **kwds):
        for callback in self.callbacks:
            callback(*args, **kwds)

def register_callback(signal_name, callback):
    signal = BaseSignal.get_instance(signal_name)
    if signal:
        signal.connect(callback)
    else:
        ValueError(f"Signal '{signal_name}' not found.")
