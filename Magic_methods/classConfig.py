# Implement a Config class that follows the singleton pattern and describes a configuration 
# object with fixed parameters. The class should not accept any arguments when it is instantiated.

#  When the Config class is first called, an instance of the class should be created and returned, 
#  and subsequent calls should return the instance created on the first call.

#  The Config class instance should have four attributes:

# program_name — attribute with string value GenerationPy
# environment — attribute with string value release
# loglevel — attribute with string value verbose
# version — attribute with string value 1.0.0


class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance
                          
    def __init__(self):
        self.program_name = 'GenerationPy'
        self.environment = 'release'
        self.loglevel = 'verbose'
        self.version = '1.0.0'


# Sample Input 1:

config = Config()

print(config.program_name)
print(config.environment)
print(config.loglevel)
print(config.version)

# Sample Output 1:

# GenerationPy
# release
# verbose
# 1.0.0