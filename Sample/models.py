from django.db import models, transaction
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import threading

class stuform(models.Model):
    Name= models.CharField(max_length=40,null=True)


@receiver(pre_save,sender=stuform)
def userform(sender, instance,*args,**kwargs):
    print("User Filling the form")

@receiver(post_save,sender=stuform)
def usersave(sender,instance, created, *args,**kwargs):
    try:
        with transaction.atomic():
        
            if created:
                print(f"Signal Received, Thread:{threading.current_thread().name}")
                print(f"{instance.Name} has filled the form")
                print("action completed inside the transaction")
    except:
        print("transcation failed, user creation failed")


