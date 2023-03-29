from django.shortcuts import render
from .models import Operator, DroneShot, Booking, Location, Customer
from django.contrib import messages
import hashlib
from .settings import MESSAGE_STORAGE


# Create your views here.

def register(request):
    method = False
    if request.method == 'POST':
        method = True
    unm = False
    if method and not Operator.objects.filter(name=request.POST.get('username')):
        unm = True
    pas = True
    if method and request.POST.get('password1') != request.POST.get('password2'):
        pas = False
    if unm and pas:
        saverecord = Operator()
        saverecord.name = request.POST.get('username')
        passtr = request.POST.get('password1')
        saverecord.password = hashlib.sha256(passtr.encode()).hexdigest()
        saverecord.email = request.POST.get('email')
        saverecord.access = "NO"
        saverecord.save()
        return render(request, 'droame/homepage.html', {'username': saverecord.name})
    else:
        if not unm:
            messages.warning(request, 'Username already exists!')
        if not pas:
            messages.warning(request, 'Passwords don\'nt match!')
        return render(request, 'droame/register.html', {})


def login(request):
    method = False
    if request.method == 'POST':
        method = True
    unm = False
    if method and Operator.objects.filter(name=request.POST.get('username')):
        unm = True
    pas = False
    if method and unm:
        opr = Operator.objects.get(name=request.POST.get('username'))
        passtr = request.POST.get('password')
        if opr.password == hashlib.sha256(passtr.encode()).hexdigest():
            pas = True
    if method and unm and pas:
        return render(request, 'droame/homepage.html', {'username': request.POST.get('username')})
    else:
        if unm:
            messages.warning(request, 'Username doesn\'nt exist!')
        if unm and not pas:
            messages.warning(request, 'Please enter valid password!')
        return render(request, 'droame/login.html', {})


def homepage(request):
    return render(request, 'droame/homepage.html', {})


def forgotPassword(request):
    return render(request, "<h1> Hello </h1>", {})


def logout(request):
    return render(request, 'droame/login.html', {})


def customers(request):
    customers = Customer.objects.all()
    return render(request, 'droame/customers.html', {'customers': customers})


def editCustomer(request, customer_id):
    method = False
    if request.method == 'POST':
        method = True
        eml = True
        mobn = True
    if method and not Customer.objects.filter(email=request.POST.get('email')) and not len(Customer.objects.filter(email=request.POST.get('email'))) <= 1:
        eml = False
    if method and not Customer.objects.filter(mobileNo=request.POST.get('mobileNo')) and not len(Customer.objects.filter(mobileNo=request.POST.get('mobileNo'))) <= 1:
        mobn = False
    adno = True
    if method and not Customer.objects.filter(aadhaarNo=request.POST.get('aadhaarNo')) and not len(Customer.objects.filter(aadhaarNo=request.POST.get('aadhaarNo'))) <= 1:
        adno = False
    leng = True
    if method and adno and len(request.POST.get('aadhaarNo')) != 12:
        leng = False
    if method and eml and mobn and adno and leng:
        Customer.objects.filter(id=customer_id).update(name=request.POST.get('name'), email=request.POST.get('email'), mobileNo=request.POST.get('mobileNo'), address=request.POST.get('address'), pincode=request.POST.get('pincode'), aadhaarNo=request.POST.get('aadhaarNo'), addedBy=request.POST.get('addedBy'))
        customers = Customer.objects.all()
        return render(request, 'droame/customers.html', {'customers': customers})
    else:
        saverecord = Customer()
        if method:
            saverecord.name = request.POST.get('name')
            saverecord.email = request.POST.get('email')
            saverecord.mobileNo = request.POST.get('mobileNo')
            saverecord.address = request.POST.get('address')
            saverecord.pincode = request.POST.get('pincode')
            saverecord.aadhaarNo = request.POST.get('aadhaarNo')
            saverecord.addedBy = request.POST.get('addedBy')
            if not eml:
                messages.warning(request, 'Email already exists!')
            if not mobn:
                messages.warning(request, 'Mobile Number already exists!')
            if not adno:
                messages.warning(request, 'Aadhaar Number already exists!')
            if adno and not leng:
                messages.warning(request, 'Please enter a valid Aadhaar number!')
        else:
            saverecord = Customer.objects.get(id=customer_id)
        operators = Operator.objects.all()
        return render(request, 'droame/editCustomer.html', {'saverecord': saverecord, 'operators': operators})





def addCustomer(request):
    method = False
    if request.method == 'POST':
        method = True
    eml = False
    if method and not Customer.objects.filter(email=request.POST.get('email')):
        eml = True
    mobn = False
    if method and not Customer.objects.filter(mobileNo=request.POST.get('mobileNo')):
        mobn = True
    adno = False
    if method and not Customer.objects.filter(aadhaarNo=request.POST.get('aadhaarNo')):
        adno = True
    leng = False
    if adno and len(request.POST.get('aadhaarNo')) == 12:
        leng = True
    if method and eml and mobn and adno and leng:
        saverecord = Customer()
        saverecord.name = request.POST.get('name')
        saverecord.email = request.POST.get('email')
        saverecord.mobileNo = request.POST.get('mobileNo')
        saverecord.address = request.POST.get('address')
        saverecord.pincode = request.POST.get('pincode')
        saverecord.aadhaarNo = request.POST.get('aadhaarNo')
        saverecord.addedBy = request.POST.get('addedBy')
        saverecord.save()
        customers = Customer.objects.all()
        return render(request, 'droame/customers.html', {'customers': customers})
    else:
        saverecord = Customer()
        if method:
            saverecord.name = request.POST.get('name')
            saverecord.email = request.POST.get('email')
            saverecord.mobileNo = request.POST.get('mobileNo')
            saverecord.address = request.POST.get('address')
            saverecord.pincode = request.POST.get('pincode')
            saverecord.aadhaarNo = request.POST.get('aadhaarNo')
            saverecord.addedBy = request.POST.get('addedBy')
            if not eml:
                messages.warning(request, 'Email already exists!')
            if not mobn:
                messages.warning(request, 'Mobile Number already exists!')
            if not adno:
                messages.warning(request, 'Aadhaar Number already exists!')
            if adno and not leng:
                messages.warning(request, 'Please enter a valid Aadhaar number!')
        operators = Operator.objects.all()
        return render(request, 'droame/addCustomer.html', {'saverecord': saverecord, 'operators': operators})




def removeCustomer(request,customer_id):
    Customer.objects.get(id=customer_id).delete()
    customers = Customer.objects.all()
    return render(request, 'droame/customers.html', {'customers': customers})



def droneshots(request):
    droneshots = DroneShot.objects.all()
    return render(request, 'droame/droneshots.html', {'droneshots': droneshots})


def addDroneShot(request):
    method = False
    if request.method == 'POST':
        method = True
    if method and request.POST.get('type') and request.POST.get('addedBy'):
        saverecord = DroneShot()
        saverecord.type = request.POST.get('type')
        saverecord.addedBy = request.POST.get('addedBy')
        saverecord.save()
        droneshots = DroneShot.objects.all()
        return render(request, 'droame/droneshots.html', {'droneshots': droneshots})
    else:
        operators = Operator.objects.all()
        return render(request, 'droame/addDroneShot.html', {'operators': operators})


def editDroneShot(request, drone_shot_id):
    method = False
    if request.method == 'POST':
        method = True
    if method and request.POST.get('type') and request.POST.get('addedBy'):
        DroneShot.objects.filter(id=drone_shot_id).update(type=request.POST.get('type'), addedBy=request.POST.get('addedBy'))
        droneshots = DroneShot.objects.all()
        return render(request, 'droame/droneshots.html', {'droneshots': droneshots})
    else:
        droneshot = DroneShot.objects.get(id=drone_shot_id)
        operators = Operator.objects.all()
        return render(request, 'droame/editDroneShot.html', {'droneshot': droneshot, 'operators': operators})


def removeDroneShot(request, drone_shot_id):
    DroneShot.objects.get(id=drone_shot_id).delete()
    droneshots = DroneShot.objects.all()
    return render(request, 'droame/droneshots.html', {'droneshots':droneshots})



def locations(request):
    locations = Location.objects.all()
    return render(request, 'droame/locations.html', {'locations': locations})


def addLocation(request):
    method = False
    if request.method == 'POST':
        method = True
    if method and request.POST.get('name') and request.POST.get('state') and request.POST.get('country') and request.POST.get('pincode') and request.POST.get('addedBy'):
        saverecord = Location()
        saverecord.name = request.POST.get('name')
        saverecord.state = request.POST.get('state')
        saverecord.country = request.POST.get('country')
        saverecord.pincode = request.POST.get('pincode')
        saverecord.addedBy = request.POST.get('addedBy')
        saverecord.save()
        locations = Location.objects.all()
        return render(request, 'droame/locations.html', {'locations': locations})
    else:
        operators = Operator.objects.all()
        return render(request, 'droame/addLocation.html', {'operators': operators})


def editLocation(request, location_id):
    method = False
    if request.method == 'POST':
        method = True
    if method and request.POST.get('name') and request.POST.get('state') and request.POST.get('country') and request.POST.get('pincode') and request.POST.get('addedBy'):
        Location.objects.filter(id=location_id).update(name=request.POST.get('name'), state=request.POST.get('state'), country=request.POST.get('country'), pincode=request.POST.get('pincode'), addedBy=request.POST.get('addedBy'))
        locations = Location.objects.all()
        return render(request, 'droame/locations.html', {'locations': locations})
    else:
        saverecord = Location.objects.get(id=location_id)
        operators = Operator.objects.all()
        return render(request, 'droame/editLocation.html', {'saverecord': saverecord, 'operators': operators})


def removeLocation(request, location_id):
    Location.objects.get(id=location_id).delete()
    locations = Location.objects.all()
    return render(request, 'droame/locations.html', {'locations': locations})



def bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'droame/bookings.html', {'bookings': bookings})


def addBooking(request):
    method = False
    if request.method == 'POST':
        method = True
    if method and request.POST.get('custid') and request.POST.get('locid') and request.POST.get('dsid') and request.POST.get('datetime') and request.POST.get('totalRent') and request.POST.get('duration') and request.POST.get('addedBy'):
        saverecord = Booking()
        cus = Customer.objects.get(name=request.POST.get('custid'))
        saverecord.location_id = cus.id
        loc = Location.objects.get(name = request.POST.get('locid'))
        saverecord.location_id = loc.id
        ds = DroneShot.objects.get(type=request.POST.get('dsid'))
        saverecord.drone_shot_id = ds.id
        saverecord.datetime = request.POST.get('datetime')
        saverecord.totalRent = request.POST.get('totalRent')
        saverecord.duration = request.POST.get('duration')
        saverecord.addedBy = request.POST.get('addedBy')
        saverecord.save()
        bookings = Booking.objects.all()
        return render(request, 'droame/bookings.html', {'bookings': bookings})
    else:
        operators = Operator.objects.all()
        customers = Customer.objects.all()
        locations = Location.objects.all()
        return render(request, 'droame/addBooking.html', {'operators': operators, 'customers': customers, 'locations': locations})


def editBooking(request, booking_id):
    method = False
    if request.method == 'POST':
        method = True
    if method and request.POST.get('custid') and request.POST.get('locid') and request.POST.get('dsid') and request.POST.get('datetime') and request.POST.get('totalRent') and request.POST.get('duration') and request.POST.get('addedBy'):
        cus = Customer.objects.get(name=request.POST.get('custid'))
        loc = Location.objects.get(name=request.POST.get('locid'))
        ds = DroneShot.objects.get(type=request.POST.get('dsid'))
        Booking.objects.filter(id=booking_id).update(customer_id=cus.id, location_id=loc.id, drone_shot_id=ds.id, datetime=request.POST.get('datetime'), totalRent=request.POST.get('totalRent'), duration=request.POST.get('duration'), addedBy=request.POST.get('addedBy'))
        bookings = Booking.objects.all()
        return render(request, 'droame/bookings.html', {'bookings': bookings})
    else:
        saverecord = Booking.objects.get(id=booking_id)
        operators = Operator.objects.all()
        return render(request, 'droame/editBooking.html', {'saverecord': saverecord, 'operators': operators})


def removeBooking(request, booking_id):
    Booking.objects.get(id=booking_id).delete()
    bookings = Booking.objects.all()
    return render(request, 'droame/bookings.html', {'bookings': bookings})







