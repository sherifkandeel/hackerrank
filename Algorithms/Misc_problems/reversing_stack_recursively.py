class stack(list):
    def push(self, item):
        self.append(item)
    def isEmpty(self):
        return not self
    def top(self):
        if self:
            return s[len(s)-1]



#adding list items:
s = stack()
s.push(30)
s.push(-5)
s.push(18)
s.push(14)
s.push(-3)

print s.top()
