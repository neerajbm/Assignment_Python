class student():
    def register(self, regno, name, standard, section):
        self.regno = regno
        self.name = name
        self.standard = standard
        self.section = section
        
    def info(self):
        print('Regno', self.regno, 'Name', self.name, 'Standard', self.standard, 'Section', self.section)
        
        
pratham = student()
pratham.register(101, 'Pratham', '9', 'A')
pratham.info()

mad = student()
mad.register(102, 'Mad', '9', 'C')
mad.info()

