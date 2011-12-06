from django.db import models


class Client(models.Model):
    """
    Client who advertises with us.  
    """
    name = models.CharField(max_length=50)
    telephone_no =  models.CharField(max_length=25)
    
    def __unicode__(self):
        return "%s" %(self.name)


class Ad(models.Model):
    """
    Ad that is published in our message board.
    """
    title = models.CharField(max_length=50)
    body = models.TextField()
    client = models.ForeignKey(Client)
    STATUS_CHOICES = ((0, 'Inactive'), 
                      (1, 'Active'), 
                      (2, 'Expired'))
    status = models.PositiveIntegerField(choices=STATUS_CHOICES)
    
    def __unicode__(self):
        return "%s: %s" %(self.title, self.get_status_display())


class Transaction(models.Model):
    """
    Each ad appears in our message board based on transaction
    """
    client = models.ForeignKey(Client)
    ad = models.ForeignKey(Ad)
    start_at = models.DateTimeField(auto_now=True) 
    expire_at = models.DateTimeField()
    is_paid = models.BooleanField(default=False)
    
    def __unicode__(self):
        return "Transaction for ad %s expires: %s" %(self.ad, self.expire_at)
