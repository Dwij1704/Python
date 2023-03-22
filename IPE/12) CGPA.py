class sgpa:
    def __init__(self,no_subject,total_credit,sem):
        self.no_subject=no_subject
        self.total_credit=total_credit
        self.sem=sem
    def sgpa(self,current_sem):
        self.temp_sum=0
        for i in range(self.no_subject):
            self.temp_sum+=int(input(f"Enter Grade out of {self.total_credit} For {i+1} Subject for {current_sem} sem: "))
        self.final_sgpa=(self.temp_sum*self.total_credit)/(self.total_credit*self.no_subject)
class cgpa(sgpa):
    def cgpa(self):
        self.total_sgpa=0
        for i in range(self.sem):
            super().sgpa(i+1)
            self.total_sgpa+=self.final_sgpa
        print(self.total_sgpa/self.sem)
cgpa=cgpa(3,10,2)
cgpa.cgpa()