from django.db import models


# from django.contrib.auth.models import User


class BankName(models.Model):
    Name = models.CharField(max_length=20)


class BankAccount(models.Model):
    AccountNumber = models.CharField(max_length=32)
    BankName = models.ForeignKey(BankName)
    BranchName = models.CharField(max_length=20)


class CustomerGroup(models.Model):
    Name = models.CharField(max_length=20)


class ActualCounterparty(models.Model):  # moshtari haghighi
    Name = models.CharField(max_length=100)
    Family = models.CharField(max_length=100)
    Job = models.CharField(max_length=30)
    IdNumber = models.IntegerField()  # shomare shenasname
    FatherName = models.CharField(max_length=100)
    NationalCode = models.CharField(max_length=10)


class LegalCounterparty(models.Model):
    Name = models.CharField(max_length=100)
    ToBeRegistered = models.BooleanField(default=False)  # dar shorofe taasis
    EconomicCode = models.CharField(max_length=8)  # code eghtesadi
    NationalId = models.CharField(max_length=10)  # shenase melli
    RegisterNumber = models.IntegerField()  # shomare sabt


class PurchaserCredit(models.Model):
    MaxInvoiceAmount = models.BigIntegerField()  # max mablaghe har factor
    MaxDebtAmount = models.BigIntegerField()
    MaxProformaPlusDebtAmount = models.BigIntegerField()
    MaxChequeAmount = models.BigIntegerField()
    MaxVolume = models.IntegerField()
    MaxWeight = models.IntegerField()
    MaxOutstandingInvoicesAmount = models.BigIntegerField()
    MaxOutstandingInvoicesNumber = models.IntegerField()
    MaxProformaNumber = models.IntegerField()
    MaxChequeDeadlineGapDays = models.IntegerField()
    MinInvoiceAmount = models.IntegerField()


class PurchaserCreditType(models.Model):
    TypeName = models.CharField(max_length=15)


class State(models.Model):
    StateName = models.CharField(max_length=20)


class City(models.Model):
    CityName = models.CharField(max_length=20)
    State = models.ForeignKey(State)


class Region(models.Model):
    RegionName = models.CharField(max_length=20)
    City = models.ForeignKey(City)


class Path(models.Model):
    PathName = models.CharField(max_length=20)
    Region = models.ForeignKey(Region)


class CounterpartyBaseInformation(models.Model):  # tarafe hesab
    ManualCode = models.CharField(max_length=10, unique=True)  # code dasti
    DateCreated = models.DateField()
    TimeCreated = models.TimeField()
    IsCounterpartyTypeActual = models.BooleanField(null=False, default=False)
    ActualCounterparty = models.ForeignKey(ActualCounterparty, null=True)
    LegalCounterparty = models.ForeignKey(LegalCounterparty, null=True)
    DeliveryStartTime = models.TimeField()
    DeliveryStopTime = models.TimeField()
    IsOwnershipTypeOwner = models.BooleanField(null=False, default=False)
    IsCounterpartySeller = models.BooleanField(default=False)
    IsCounterpartyPurchaser = models.BooleanField(default=False)
    PurchaserCreditType = models.ForeignKey(PurchaserCreditType)
    PurchaserCredit = models.ForeignKey(PurchaserCredit, null=True)
    Path = models.ForeignKey(Path)
    Address = models.CharField(max_length=200)

# OWNERSHIPTYPES = (
#     (3, 'IEC62056'),
#     (4, 'CORUS'),
#     (5, 'MODBUS')
# )
# OwnershipType = models.SmallIntegerField(choices=)
