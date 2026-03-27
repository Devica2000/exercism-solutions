import re

class PhoneNumber:
    
    def __init__(self, number):
        self.number = self.clean_up(number)
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        self.subscriber_number = self.number[6:]
        
    def clean_up(self, number):
        valid_num = re.sub(r'[\D]', '', number)
        
        if re.search(r'[a-zA-Z]', number):
            raise ValueError("letters not permitted")
        if re.search(r'[^0-9()\s.+\-]', number):
            raise ValueError("punctuations not permitted")
        
        if len(valid_num) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(valid_num) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(valid_num) == 11 and valid_num[0] != '1':
            raise ValueError("11 digits must start with 1")

        if len(valid_num) == 11:
            valid_num = valid_num[1:]
            
        if valid_num[3] == '1':
            raise ValueError("exchange code cannot start with one")
        if valid_num[3] == '0':
            raise ValueError("exchange code cannot start with zero")
        if valid_num[0] == '0':
            raise ValueError("area code cannot start with zero")
        if valid_num[0] == '1':
            raise ValueError("area code cannot start with one")

        return valid_num

    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"


            
        

            
        
            
            
            
 
        
