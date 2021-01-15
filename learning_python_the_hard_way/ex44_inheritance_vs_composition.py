class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

    def override(self):
        print "PARENT override()"
    
    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

    def override(self):
        print "CHILD override()"


dad = Parent()
son = Child()

dad.implicit()
son.implicit()
print("")

dad.override()
son.override()
print("")

dad.altered()
son.altered()
print("")


# Composition
class Other(object):
    
    def override(self):
        print "OTHER override()"
    
    def implicit(self):
        print "OTHER implicit()"
    
    def altered(self):
        print "OTHER altered()"
    

class Child2(object):
    def __init__(self):
        self.other = Other()
    
    def implicit(self):
        self.other.implicit()
    
    def override(self):
        print "CHILD override()"
    
    def altered(self):
        print "CHILD BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD AFTER OTHER altered()"

son = Child2()
son.implicit()
son.override()
son.altered()