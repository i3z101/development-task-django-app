import re
from django.forms import ValidationError

class Validation:
    value: str
    def __init__(self, value):
        self.value = value

    def validateString(self, name: str, isRequired: bool, min: int, max: int, containSpace:bool, containNumeric:bool):
        trimmedValue: str = self.value.strip()
        if(isRequired):
            if(trimmedValue == ""):
                return ValidationError(name + " is required")
            elif(containSpace and containNumeric):
                if(not re.match('^[A-Za-z\s0-9]+$', trimmedValue)):
                    return ValidationError(name + " should contain english characters or numbers", 422)
                elif(len(trimmedValue) < min or len(trimmedValue) > max):
                    return ValidationError(name + " should be between " + min + " and " + max, 422)
                else:
                    return ValidationError(" ", 200)
            elif(not containSpace and containNumeric):
                if(not re.match('^[A-Za-z0-9]+$', trimmedValue)):
                    return ValidationError(name + " should contain english characters and numbers withut spaces", 422)
                elif(len(trimmedValue) < min or len(trimmedValue) > max):
                    return ValidationError(name + " should be between " + min + " and " + max, 422)
                else:
                    return ValidationError(" ", 200)
            elif(containSpace and not containNumeric):
                if(not re.match('^[A-Za-z\s]+$', trimmedValue)):
                    return ValidationError(name + " should contain english characters only", 422)
                elif(len(trimmedValue) < min or len(trimmedValue) > max):
                    return ValidationError(name + " should be between " + min + " and " + max, 422)
                else:
                    return ValidationError("", 200)
        else:
            if(trimmedValue == ""):
                return ValidationError(" ", 200)
            elif(containSpace and containNumeric):
                if(not re.match('^[A-Za-z\s0-9]+$', trimmedValue)):
                    return ValidationError(name + " should contain english characters or numbers or", 422)
                elif(len(trimmedValue) < min or len(trimmedValue) > max):
                    return ValidationError(name + " should be between " + min + " and " + max, 422)
                else:
                    return ValidationError(" ", 200)
            elif(not containSpace and containNumeric):
                if(not re.match('^[A-Za-z0-9]+$', trimmedValue)):
                    return ValidationError(name + " should contain english characters and numbers withut spaces", 422)
                elif(len(trimmedValue) < min or len(trimmedValue) > max):
                    return ValidationError(name + " should be between " + min + " and " + max, 422)
                else:
                    return ValidationError(" ", 200)
            elif(containSpace and not containNumeric):
                if(not re.match('^[A-Za-z\s]+$', trimmedValue)):
                    return ValidationError(name + " should contain english characters only", 422)
                elif(len(trimmedValue) < min or len(trimmedValue) > max):
                    return ValidationError(name + " should be between " + min + " and " + max, 422)
                else:
                    return ValidationError("", 200)
    
    def validateEmail(self) -> ValidationError:
        trimmedValue: str = self.value.strip()
        if(trimmedValue == ""):
            return ValidationError("Email is required", 422)
        elif(not re.match('^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$', trimmedValue)):
            return ValidationError("Email format is not valid", 422)
        else:
            return ValidationError("", 200)

    def validatePassword(self, min:int, max:int) -> ValidationError:
        trimmedValue: str = self.value.strip()
        if(trimmedValue == ""):
            return ValidationError("Password is required", 422)
        elif(not re.match('^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@$!%*?&#])([a-zA-Z0-9@$!%*?&#])+$', trimmedValue)):
             return ValidationError("Password should contain at least one uppercase, lowercase, number, and special characters", 422)
        elif(len(trimmedValue) < min or len(trimmedValue) > max):
            return ValidationError("Password should be " + str(min) + " and " + str(max), 422)
        else:
            return ValidationError("", 200)
    
    def validateNumeric(self, name: str, isRequired: str):
        trimmedValue: str = self.value.strip()
        if(isRequired):
            if(trimmedValue == ""):
                return ValidationError(name + " is required", 422)
            elif(not re.match('^[0-9]+$', trimmedValue)):
                return ValidationError(name + " should contain only numeric values", 422)
            else:
                return ValidationError("", 200)
        else:
            if(not re.match('^[0-9]+$', trimmedValue)):
                return ValidationError(name + " should contain only numeric values", 422)
            else:
                return ValidationError("", 200)
