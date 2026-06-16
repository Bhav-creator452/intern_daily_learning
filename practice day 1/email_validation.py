#email validation
def is_valid_email(email: str) -> bool:
    if email.count("@")!=1:
        return False
    username, domain = email.split("@")

    if username=="" or domain=="":
        return False
    
    if "." not in domain:
        return False
    
    name, extension = domain.rsplit(".", 1) 

    if name=="" or extension=="":
        return False
    return True

print(is_valid_email("anna@shop.com"))      # True
print(is_valid_email("anna.shop.com"))      # False
print(is_valid_email("@shop.com"))          # False

print(is_valid_email("anna@.com"))         # False
print(is_valid_email("anna@shopcom"))      # False
print(is_valid_email("anna@shop."))        # False
print(is_valid_email("anna@@shop.com"))     # False
