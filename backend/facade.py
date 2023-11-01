from abc import ABC, abstractmethod
from restrictions.DataCleaner.DataCleaner import DataCleaner
from restrictions.Access.Access import CreateAccess
from restrictions.DataCleaner.Validators import UserDataValidator, PasswordDataValidator
from restrictions.RequestFilter.RequestFilter import RequestFilter

class IFacade(ABC):
    @abstractmethod
    def send_request(self, data):
        pass

class Facade:
    def __init__(self):
      self.data_cleaner = DataCleaner()
      self.request_filter = RequestFilter()
      self.access = CreateAccess()

      self.data_cleaner.add_validator(UserDataValidator())
      self.data_cleaner.add_validator(PasswordDataValidator())

    def send_request(self, data):
      passedCleanData = True
      requestIsAllowed = True
      
      if not self.request_filter.process_request(data):
        requestIsAllowed = False
        return {"message": "Solicitud bloqueada."}

      if not self.data_cleaner.clean_data(data):
        passedCleanData = False
        return {"message": "La data no ha cumplido con los validadores."}
      
      # # ---------------------------------- ACCESOS --------------------------------- #
      # control_access = self.access.create(data['client']['role'])
      # InsSystem = control_access.authenticate()
      # control_access.login()
      
      
      # # --------------------------------- PERMISOS --------------------------------- #
      # InsSystem.create_order()
      # InsSystem.delete_order_order()

      msg = {F"requestIsAllowed": {requestIsAllowed}, "passedCleanData": {passedCleanData}}
      return msg