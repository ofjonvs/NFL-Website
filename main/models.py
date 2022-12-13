from django.db import models

class Prospect(models.Model):
    name = models.CharField(max_length=30)
    name_link = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    school_link = models.CharField(max_length=30)
    grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    position = models.CharField(max_length=4)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}, {self.school}"

class Quarterback(models.Model):
    prospect = models.ForeignKey(Prospect, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    arm_strength = models.DecimalField(max_digits=2, decimal_places=1)
    size = models.DecimalField(max_digits=2, decimal_places=1)
    short_acc = models.DecimalField(max_digits=2, decimal_places=1)	
    deep_acc = models.DecimalField(max_digits=2, decimal_places=1)
    mobility = models.DecimalField(max_digits=2, decimal_places=1)
    process = models.DecimalField(max_digits=2, decimal_places=1)
    decision = models.DecimalField(max_digits=2, decimal_places=1)
    athleticism	 = models.DecimalField(max_digits=2, decimal_places=1)
    mechanics = models.DecimalField(max_digits=2, decimal_places=1)
    anticipation = models.DecimalField(max_digits=2, decimal_places=1)
    ball_carry = models.DecimalField(max_digits=2, decimal_places=1)	
    intangebles	= models.IntegerField(blank=True, default=0)
    grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        self.grade = round(((
            self.arm_strength*10 + 
            self.size*4 + 
            self.short_acc*9 +
            self.deep_acc*14 +
            self.mobility*17 +
            self.process*8 +
            self.decision*9 +
            self.athleticism*7 +
            self.mechanics*7 +
            self.anticipation*9 +
            self.ball_carry*5
            )/100)*20, 2)
        super(Quarterback, self).save(*args, **kwargs) # Call the "real" save() method.

    def __str__(self):
        return f"{self.name}, {self.school}"

class Runningback(models.Model):
    prospect = models.ForeignKey(Prospect, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    size = models.DecimalField(max_digits=2, decimal_places=1)
    vision = models.DecimalField(max_digits=2, decimal_places=1)
    balance = models.DecimalField(max_digits=2, decimal_places=1)
    elusiveness = models.DecimalField(max_digits=2, decimal_places=1)
    speed = models.DecimalField(max_digits=2, decimal_places=1)
    burst = models.DecimalField(max_digits=2, decimal_places=1)
    pass_block = models.DecimalField(max_digits=2, decimal_places=1)
    fumble = models.DecimalField(max_digits=2, decimal_places=1)
    cod = models.DecimalField(max_digits=2, decimal_places=1)
    grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.name}, {self.school}"

class Widereceiver(models.Model):
    prospect = models.ForeignKey(Prospect, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    size = models.DecimalField(max_digits=2, decimal_places=1)
    speed = models.DecimalField(max_digits=2, decimal_places=1)
    cod = models.DecimalField(max_digits=2, decimal_places=1)
    release = models.DecimalField(max_digits=2, decimal_places=1)
    short_routes = models.DecimalField(max_digits=2, decimal_places=1)
    deep_routes = models.DecimalField(max_digits=2, decimal_places=1)
    hands = models.DecimalField(max_digits=2, decimal_places=1)
    ball_skills = models.DecimalField(max_digits=2, decimal_places=1)
    rac = models.DecimalField(max_digits=2, decimal_places=1)
    block = models.DecimalField(max_digits=2, decimal_places=1)
    cit = models.DecimalField(max_digits=2, decimal_places=1)
    grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.name}, {self.school}"

class IOL(models.Model):
    prospect = models.ForeignKey(Prospect, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    size = models.DecimalField(max_digits=2, decimal_places=1)
    pass_set = models.DecimalField(max_digits=2, decimal_places=1)
    run_block = models.DecimalField(max_digits=2, decimal_places=1)
    impact = models.DecimalField(max_digits=2, decimal_places=1)
    move = models.DecimalField(max_digits=2, decimal_places=1)
    strength = models.DecimalField(max_digits=2, decimal_places=1)
    athleticism = models.DecimalField(max_digits=2, decimal_places=1)
    hands = models.DecimalField(max_digits=2, decimal_places=1)
    anchor = models.DecimalField(max_digits=2, decimal_places=1)
    lean = models.DecimalField(max_digits=2, decimal_places=1)
    grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.name}, {self.school}"

class Tightend(models.Model):
    prospect = models.ForeignKey(Prospect, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    size = models.DecimalField(max_digits=2, decimal_places=1)
    speed = models.DecimalField(max_digits=2, decimal_places=1)
    cod = models.DecimalField(max_digits=2, decimal_places=1)
    release = models.DecimalField(max_digits=2, decimal_places=1)
    short_routes = models.DecimalField(max_digits=2, decimal_places=1)
    deep_routes = models.DecimalField(max_digits=2, decimal_places=1)
    hands = models.DecimalField(max_digits=2, decimal_places=1)
    ball_skills = models.DecimalField(max_digits=2, decimal_places=1)
    rac = models.DecimalField(max_digits=2, decimal_places=1)
    run_block = models.DecimalField(max_digits=2, decimal_places=1)
    pass_block = models.DecimalField(max_digits=2, decimal_places=1)
    cit = models.DecimalField(max_digits=2, decimal_places=1)
    grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.name}, {self.school}"

class Tackle(models.Model):
    prospect = models.ForeignKey(Prospect, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    size = models.DecimalField(max_digits=2, decimal_places=1)
    pass_set = models.DecimalField(max_digits=2, decimal_places=1)
    run_block = models.DecimalField(max_digits=2, decimal_places=1)
    impact = models.DecimalField(max_digits=2, decimal_places=1)
    move = models.DecimalField(max_digits=2, decimal_places=1)
    strength = models.DecimalField(max_digits=2, decimal_places=1)
    athleticism = models.DecimalField(max_digits=2, decimal_places=1)
    hands = models.DecimalField(max_digits=2, decimal_places=1)
    anchor = models.DecimalField(max_digits=2, decimal_places=1)
    kick = models.DecimalField(max_digits=2, decimal_places=1)
    lean = models.DecimalField(max_digits=2, decimal_places=1)
    grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.name}, {self.school}"

class IDL(models.Model):
    prospect = models.ForeignKey(Prospect, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    size = models.DecimalField(max_digits=2, decimal_places=1)
    poa = models.DecimalField(max_digits=2, decimal_places=1)
    shed = models.DecimalField(max_digits=2, decimal_places=1)
    strength = models.DecimalField(max_digits=2, decimal_places=1)
    power_rush = models.DecimalField(max_digits=2, decimal_places=1)
    finesse_rush = models.DecimalField(max_digits=2, decimal_places=1)
    getoff = models.DecimalField(max_digits=2, decimal_places=1)
    bend = models.DecimalField(max_digits=2, decimal_places=1)
    athleticism = models.DecimalField(max_digits=2, decimal_places=1)
    hands = models.DecimalField(max_digits=2, decimal_places=1)
    motor = models.DecimalField(max_digits=2, decimal_places=1)
    grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.name}, {self.school}"

class Edge(models.Model):
    prospect = models.ForeignKey(Prospect, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    size = models.DecimalField(max_digits=2, decimal_places=1)
    poa = models.DecimalField(max_digits=2, decimal_places=1)
    shed = models.DecimalField(max_digits=2, decimal_places=1)
    speed_rush = models.DecimalField(max_digits=2, decimal_places=1)
    power_rush = models.DecimalField(max_digits=2, decimal_places=1)
    finesse_rush = models.DecimalField(max_digits=2, decimal_places=1)
    getoff = models.DecimalField(max_digits=2, decimal_places=1)
    bend = models.DecimalField(max_digits=2, decimal_places=1)
    athleticism = models.DecimalField(max_digits=2, decimal_places=1)
    hands = models.DecimalField(max_digits=2, decimal_places=1)
    tackle = models.DecimalField(max_digits=2, decimal_places=1)
    motor = models.DecimalField(max_digits=2, decimal_places=1)
    strength = models.DecimalField(max_digits=2, decimal_places=1)
    grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.name}, {self.school}"

class Linebacker(models.Model):
    prospect = models.ForeignKey(Prospect, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    size = models.DecimalField(max_digits=2, decimal_places=1)
    speed = models.DecimalField(max_digits=2, decimal_places=1)
    cod = models.DecimalField(max_digits=2, decimal_places=1)
    man = models.DecimalField(max_digits=2, decimal_places=1)
    zone = models.DecimalField(max_digits=2, decimal_places=1)
    poa = models.DecimalField(max_digits=2, decimal_places=1)
    shed = models.DecimalField(max_digits=2, decimal_places=1)
    strength = models.DecimalField(max_digits=2, decimal_places=1)
    process = models.DecimalField(max_digits=2, decimal_places=1)
    tackle = models.DecimalField(max_digits=2, decimal_places=1)
    blitz = models.DecimalField(max_digits=2, decimal_places=1)
    grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.name}, {self.school}"

class Cornerback(models.Model):
    prospect = models.ForeignKey(Prospect, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    size = models.DecimalField(max_digits=2, decimal_places=1)
    speed = models.DecimalField(max_digits=2, decimal_places=1)
    cod = models.DecimalField(max_digits=2, decimal_places=1)
    man = models.DecimalField(max_digits=2, decimal_places=1)
    zone = models.DecimalField(max_digits=2, decimal_places=1)
    press = models.DecimalField(max_digits=2, decimal_places=1)
    ball_skills = models.DecimalField(max_digits=2, decimal_places=1)
    transitions = models.DecimalField(max_digits=2, decimal_places=1)
    rund = models.DecimalField(max_digits=2, decimal_places=1)
    tackle = models.DecimalField(max_digits=2, decimal_places=1)
    grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.name}, {self.school}"

class Safety(models.Model):
    prospect = models.ForeignKey(Prospect, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    size = models.DecimalField(max_digits=2, decimal_places=1)
    speed = models.DecimalField(max_digits=2, decimal_places=1)
    cod = models.DecimalField(max_digits=2, decimal_places=1)
    man = models.DecimalField(max_digits=2, decimal_places=1)
    zone = models.DecimalField(max_digits=2, decimal_places=1)
    press = models.DecimalField(max_digits=2, decimal_places=1)
    ball_skills = models.DecimalField(max_digits=2, decimal_places=1)
    strength = models.DecimalField(max_digits=2, decimal_places=1)
    rund = models.DecimalField(max_digits=2, decimal_places=1)
    tackle = models.DecimalField(max_digits=2, decimal_places=1)
    range = models.DecimalField(max_digits=2, decimal_places=1)
    grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True)

    # def save(self, *args, **kwargs):
    #     self.grade = self.arm_strength + self.size
    #     super(Quarterback, self).save(*args, **kwargs) # Call the "real" save() method.
    def __str__(self):
        return f"{self.name}, {self.school}"

class GradeDescriptions(models.Model):
    position = models.CharField(max_length=20)
    description = models.TextField()

    