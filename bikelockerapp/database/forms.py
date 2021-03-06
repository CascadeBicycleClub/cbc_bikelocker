from django import forms
from database.models import Customer, Location, Status, Cust_Locker
from datetime import date, datetime


class SendEmailForm(forms.Form):
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': ('Subject')}), initial="Leased Locker Renewal with King County Metro", required=False)
    message = forms.CharField(widget=forms.Textarea, initial="Dear Leased Locker Renter, \n\nThank you for renting a bike locker from King County Metro! Please follow the link below to a Google Form. This form will be used to process your locker renewal for {}. It is important that you fill out this form, whether you wish to keep your locker or not, within 2 weeks of receiving this notice.\n\nIf your response is not received within 2 weeks, then your locker may be forfeited. Your locker deposit will be forfeited and your locker given up to the next person on the waitlist if you do not respond.\n\nPlease respond to this email if you have any questions.\n\n[Insert Renewal Form Link Here!]\n\nThank you, \n\nStephen Rowley\nFleet Manager\nCascade Bicycle Club".format(datetime.now().year), required=False)

class SendEmailFormAfter2Weeks(forms.Form):
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': ('Subject')}), initial="Reminder: Leased Locker Renewal with King County Metro", required=False)
    message = forms.CharField(widget=forms.Textarea, initial="Dear Leased Locker Renter,\n\nThank you for renting a bike locker from King County Metro! This is a reminder to please follow the link below to a Google Form. This form will be used to process your locker renewal for {}.\n\nYour locker deposit will be forfeited and your locker given up to the next person on the waitlist if you do not respond within one week of this message.\n\nPlease respond to this email if you have any questions.\n\n[Insert Renewal Form Link Here!]".format(datetime.now().year), required=False)
