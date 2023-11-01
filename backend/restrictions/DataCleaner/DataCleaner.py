from abc import ABC, abstractmethod

class IDataValidator(ABC):
    @abstractmethod
    def validate(self, data):
        pass
      
class DataCleaner:
    def __init__(self):
        self.validators = []

    def add_validator(self, validator):
        if isinstance(validator, IDataValidator):
            self.validators.append(validator)
        else:
            raise ValueError("El validador debe implementar la interfaz IDataValidator")

    def clean_data(self, data):
      try:
        for validator in self.validators:
          if not validator.validate(data):
            return False
        return True
      except Exception as e:
        print(F"error: {e}")
        return False