from datetime import datetime

class date:
    def __init__(self,date):
        self.date = date
        
    def validate(date_input):
        today = datetime.today()

        try:
            if date_input != datetime.strptime(date_input, "%Y/%m/%d").strftime('%Y/%m/%d'):
                return 'WRONG'  
            date_text = datetime.strptime(date_input, "%Y/%m/%d")
            born_date = today.year - date_text.year - ((today.month, today.day) < (date_text.month, date_text.day))
            return born_date
        except:
            return 'WRONG'
date_input = date.validate(input())
print(date_input)