class ValidationError(Exception):
 def __init__(self, message, field, error_code):
     super().__init__(message)
     self.field = field
     self.error_code = error_code
 def __str__(self):
     return f"{self.args[0]} (Field: {self.field}, Error Code: {self.error_code})"
# Usage
def validate_input(data):
 if not data.get('name'):
     raise ValidationError("Name is required", 'name', 400)
try:
 validate_input({})
except ValidationError as e:
 print(f"Validation failed: {e}")
