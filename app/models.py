from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

year_choice=[
    ('First','First'),
    ('Second','Second'),
    ('Third','Third'),
    ('Four','Four'),
    ]

Department_choice=[
    ('CSE','CSE'),
    ('EEE','EEE'),
    ('ECE','ECE'),
    ('MECH','MECH'),
    ('CIVIL','CIVIL'),
    ]


class feesdetails(models.Model):
    Name = models.CharField(max_length=50,null=True)
    Register_No = models.IntegerField(null=True)
    Year = models.CharField(max_length=50,null=True,choices=year_choice)
    Department = models.CharField(max_length=50,null=True,choices=Department_choice)
    Previous_year_balance = models.IntegerField(null=True)
    Admission_fees = models.IntegerField(null=True)
    Tuition_fees = models.IntegerField(null=True)
    Bus_fees = models.IntegerField(null=True)
    Hostel_fees = models.IntegerField(null=True)
    FGG = models.IntegerField(null=True)
    PMSS = models.IntegerField(null=True)
    Gover_quota = models.IntegerField(null=True)
    Other_scholarships = models.IntegerField(null=True)    
    KET_scholarships = models.IntegerField(null=True)
    Students_to_pay = models.IntegerField(null=True)
    Total = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.Name
    
@receiver(pre_save,sender=feesdetails)
def update_Total(sender,instance,**kwargs):
    instance.Total= instance.Previous_year_balance + instance.Admission_fees + instance.Tuition_fees + instance.Bus_fees + instance.Hostel_fees + instance.FGG + instance.PMSS + instance.Gover_quota + instance.Other_scholarships + instance.KET_scholarships + instance.Students_to_pay
    '''@property
    def Total(self):
        return self.FGG+self.PMSS
    '''
    '''def total(self, *args, **kwargs):
        self.Total = self.FGG + self.PMSS 
        super(feesdetails, self).total(*args,**kwargs)'''
   
