from abc import ABC, abstractmethod
from collections import defaultdict
from correctDataUser import CORRECT_PASSWORD, REQUESTS_FAILED

class IRequestFilter(ABC):
  @abstractmethod
  def process_request(self, ip_address: str) -> bool:
    pass

class RequestFilter(IRequestFilter):
  MAX_ATTEMPTS = 3
  
  def process_request(self, data) -> bool:
    print(self.requests_failed)
    if self.is_allowed(data['client']['ip_address']):
      if data['client']['password'] == CORRECT_PASSWORD:
        self.reset_attempts(data['client']['ip_address'])
        return True
      else:
        print('Contraseña Incorrecta')
        return False
    else:
      self.sum_attempts(data['client']['ip_address'])
      print('Numero de intentos excedido')
      return False

  def __init__(self):
    self.requests_failed = REQUESTS_FAILED

  def is_allowed(self, ip_address: str) -> bool:
    return self.requests_failed[ip_address] < self.MAX_ATTEMPTS

  def reset_attempts(self, ip_address: str):
    self.requests_failed[ip_address] = 0

  def sum_attempts(self, ip_address: str):
    self.requests_failed[ip_address] += 1