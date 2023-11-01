from .DataCleaner import IDataValidator
import re

class UserDataValidator(IDataValidator):
  def validate(self, data):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(email_pattern, data['client']['user']):
      return True
    else:
      raise ValueError("El formato del correo electrónico no es válido.")
  
class PasswordDataValidator(IDataValidator):
  def validate(self, data):
    if len(data['client']['password']) >= 8 and any(char.isupper() for char in data['client']['password']):
      return True
    else:
      raise ValueError("La contraseña debe tener al menos 8 caracteres y al menos una letra mayúscula.")