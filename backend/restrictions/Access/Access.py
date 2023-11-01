from abc import ABC, abstractmethod
from system import InsSystem

class IAccess(ABC):
    @abstractmethod
    def authenticate(self) -> InsSystem:
        pass

    @abstractmethod
    def login(self, client):
        pass

class CreateAccess:
    def create(self, client):
        if client == 'admin':
            return AccessAdmin()
        elif client == 'user':
            return AccessUser()
          
class AccessAdmin(IAccess):
    def authenticate(self) -> InsSystem:
        return InsSystem('Admin')

    def login(self, client):
        return self.authenticate()
      
class AccessUser(IAccess):
    def authenticate(self) -> InsSystem:
        return InsSystem('User')

    def login(self, client):
        return self.authenticate()
