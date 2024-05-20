from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate
from datetime import date, datetime
from django.db.models import Q
from datetime import date as d, datetime as dt
from django.db.models import Max, Case, When, IntegerField
import json


def index(request):
    return render(request, "index.html")


def login(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        print(email, password, "email,password")
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.user_type == 'admin':
                print('admin#####')
                messages.info(request, 'Welcome to Secure Care')
                return redirect('/adminHome')

            elif user.user_type == 'CareTaker':
                request.session['uid'] = user.id
                print('==============================-----------careTakerHome#####')
                messages.info(request, 'Welcome to Secure Care')
                return redirect('/careTakerHome')

            elif user.user_type == 'Nurse':
                request.session['uid'] = user.id
                messages.info(request, 'Welcome to Secure Care')
                return redirect('/nurseHome')

            elif user.user_type == 'Doctor':
                request.session['uid'] = user.id
                print('Treasurer#####')
                messages.info(request, 'Welcome to Secure Care')
                return redirect('/doctorHome')

            else:
                messages.info(request, 'Invalid')
        else:
            messages.info(request, 'Invalid')
    return render(request, "login.html")


def adminHome(request):
    return render(request, "ADMIN/adminHome.html")


def addResidents(request):
    if request.POST:
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        image = request.FILES['image']

        reguser = Residents.objects.create(
            name=name,
            age=age,
            address=address,
            email=email,
            phone=phone,
            gender=gender,
            image=image)

        reguser.save()

        messages.success(request, "Resident Added Successfully")
        return redirect('/viewResidents')
    return render(request, "ADMIN/addResidents.html")


def viewResidents(request):
    data = Residents.objects.all()
    return render(request, "ADMIN/viewResidents.html", {'data': data})


def deleteResident(request):

    id = request.GET.get('id')
    Residents.objects.filter(id=id).delete()
    messages.success(request, "Resident deleted Successfully")

    return redirect("/viewResidents")


def addCareTaker(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        password = request.POST['password']
        image = request.FILES['image']
        logUser = Login.objects.create_user(
            username=email,
            user_type='CareTaker',
            password=password,
            view_password=password)
        logUser.save()
        reguser = CareTaker.objects.create(
            login=logUser,
            name=name,
            address=address,
            email=email,
            phone=phone,
            image=image)
        reguser.save()

        messages.success(request, "CareTaker Added Successfully")
        return redirect('/viewCareTaker')
    return render(request, "ADMIN/addCareTaker.html")


def adminViewCareplan(request):
    id = request.GET.get('id')
    data = CarePlan.objects.filter(resident=id)
    return render(request, "ADMIN/adminViewCareplan.html", {'data': data})


def viewCareTaker(request):
    data = CareTaker.objects.all()
    return render(request, "ADMIN/viewCareTaker.html", {'data': data})


def deleteCareTaker(request):
    id = request.GET.get('id')
    Login.objects.filter(id=id).delete()
    messages.success(request, "CareTaker deleted Successfully")
    return redirect("/viewCareTaker")


def adminDeleteCareplan(request):
    id = request.GET.get('id')
    d = CarePlan.objects.filter(id=id).delete()
    print("delete", d)
    return redirect("/viewResidents")


def updateCareTaker(request):
    id = request.GET.get('id')
    data = CareTaker.objects.filter(id=id)

    img = CareTaker.objects.get(id=id)

    print('-------------------->>>data', data)
    if request.POST:
        name = request.POST['name']
        # email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        if "image" in request.FILES:
            image = request.FILES['image']
            img.image = image
            img.save()
        else:
            image = data[0].image
        print("------------------>>>ID", id)
        reguser = CareTaker.objects.filter(id=id).update(
            name=name,
            address=address,
            # email=email,
            phone=phone,
        )
        # reguser.save()
        print('------------->>>', reguser)

        messages.success(request, "Care Taker Successfully")
        return redirect('/viewCareTaker')

    return render(request, "ADMIN/updateCareTaker.html", {'data': data})


def addNurse(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        password = request.POST['password']
        image = request.FILES['image']
        logUser = Login.objects.create_user(
            username=email,
            user_type='Nurse',
            password=password,
            view_password=password)
        logUser.save()
        reguser = Nurse.objects.create(
            login=logUser,
            name=name,
            address=address,
            email=email,
            phone=phone,
            image=image)
        reguser.save()

        messages.success(request, "Nurse Added Successfully")
        return redirect('/viewNurse')
    return render(request, "ADMIN/addNurse.html")


def viewNurse(request):
    data = Nurse.objects.all()
    return render(request, "ADMIN/viewNurse.html", {'data': data})


def deleteNurse(request):
    id = request.GET.get('id')
    Login.objects.filter(id=id).delete()
    Login.objects.all().delete()
    messages.success(request, "Nurse deleted Successfully")
    return redirect("/viewNurse")


def updateNurse(request):
    id = request.GET.get('id')
    data = Nurse.objects.filter(id=id)
    img = Nurse.objects.get(id=id)
    print('-------------------->>>data', data)
    if request.POST:
        name = request.POST['name']
        # email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        if "image" in request.FILES:
            image = request.FILES['image']
            img.image = image
            img.save()
        else:
            image = data[0].image
        print("------------------>>>ID", id)
        reguser = Nurse.objects.filter(id=id).update(
            name=name,
            address=address,
            # email=email,
            phone=phone,
        )
        # reguser.save()
        print('------------->>>', reguser)

        messages.success(request, "Nurse Details Updated Successfully")
        return redirect('/viewNurse')

    return render(request, "ADMIN/updateNurse.html", {'data': data})


def addDoctor(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        password = request.POST['password']
        image = request.FILES['image']
        logUser = Login.objects.create_user(
            username=email,
            user_type='Doctor',
            password=password,
            view_password=password)
        logUser.save()
        reguser = Doctor.objects.create(
            login=logUser,
            name=name,
            address=address,
            email=email,
            phone=phone,
            image=image)
        reguser.save()

        messages.success(request, "Doctor Added Successfully")
        return redirect('/viewDoctor')
    return render(request, "ADMIN/addDoctor.html")


def viewDoctor(request):
    data = Doctor.objects.all()
    return render(request, "ADMIN/viewDoctor.html", {'data': data})


def updateDoctor(request):
    id = request.GET.get('id')
    data = Doctor.objects.filter(id=id)
    img = Doctor.objects.get(id=id)
    print('-------------------->>>data', data)
    if request.POST:
        name = request.POST['name']
        # email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        if "image" in request.FILES:
            image = request.FILES['image']
            img.image = image
            img.save()
        else:
            image = data[0].image
        print("------------------>>>ID", id)
        reguser = Doctor.objects.filter(id=id).update(
            name=name,
            address=address,
            # email=email,
            phone=phone,
        )
        # reguser.save()
        print('------------->>>', reguser)

        messages.success(request, "Doctor Updated Successfully")
        return redirect('/viewDoctor')

    return render(request, "ADMIN/updateDoctor.html", {'data': data})


def deleteDoctor(request):
    id = request.GET.get('id')
    Login.objects.filter(id=id).delete()
    messages.success(request, "Doctor deleted Successfully")
    return redirect("/viewDoctor")


def updateResident(request):
    id = request.GET.get('id')
    data = Residents.objects.filter(id=id)

    img = Residents.objects.get(id=id)

    if request.POST:
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        if "image" in request.FILES:
            image = request.FILES['image']
            img.image = image
            img.save()
        else:
            image = data[0].image
        print("------------------>>>ID", id)
        reguser = Residents.objects.filter(id=id).update(
            name=name,
            age=age,
            address=address,
            email=email,
            phone=phone,
            gender=gender,
        )

        # reguser.save()
        print('------------->>>', reguser)

        messages.success(request, "Resident Updated Successfully")
        return redirect('/viewResidents')

    return render(request, "ADMIN/updateResident.html", {'data': data})


# ======================Caretaker

def careTakerHome(request):
    return render(request, "CareTaker/careTakerHome.html")


def addFoodTt(request):
    id = request.GET.get('id')
    id = Residents.objects.get(id=id)
    print('--------------------------/////////////////////////////////////////////////////////////////////////////////////>', id)
    if request.POST:
        print("-------------------------------------------------------------posttttttttttttttttttttttttttttttttttttttttt")
        day = request.POST['day']
        meal = request.POST['meal']
        menu = request.POST['menu']
        if FoodTimeTable.objects.filter(resident=id, day=day, meal=meal).exists():
            messages.success(request, "Meal already entered for this day!!!")
            return redirect('/ctViewResident')
        else:
            tt = FoodTimeTable.objects.create(
                resident=id, day=day, meal=meal, menu=menu)
            tt.save()
        print('--------------------------day>', day)
        print('--------------------------meal>', meal)
        print('--------------------------menu>', menu)

        messages.success(request, "Data Entered Successfully")
    return render(request, "CareTaker/addFoodTt.html")


def adminViewChart(request):
    resident_id = request.GET.get('id')

    # Define a dictionary to map month names to their numerical representation
    month_order_map = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12,
    }

    # Define a custom ordering based on the numerical representation of months
    month_order = Case(
        *[When(month=month_name, then=month_number)
          for month_name, month_number in month_order_map.items()],
        default=0,
        output_field=IntegerField()
    )

    data = WeightChart.objects.filter(resident=resident_id).values(
        'month', 'year', 'weight').annotate(month_order=month_order).order_by('year', 'month_order')
    chart_data = [{'month': entry['month'], 'year': entry['year'],
                   'weight': entry['weight']} for entry in data]
    chart_data_json = json.dumps(chart_data)  # Convert data to JSON format
    return render(request, "ADMIN/adminViewChart.html", {'chart_data': chart_data_json})


def addWeightChart(request):
    id = request.GET.get('id')
    id = Residents.objects.get(id=id)
    print('-------------------------->', id)
    if request.POST:
        year = request.POST['year']
        month = request.POST['month']
        weight = request.POST['weight']
        if WeightChart.objects.filter(resident=id, year=year, month=month).exists():
            messages.success(request, "Weight Already added for this month!!!")
            return redirect('/ctViewResident')
        else:
            weightChart = WeightChart.objects.create(
                resident=id, year=year, month=month, weight=weight)
            weightChart.save()
            print('--------------------------weightChart>', weightChart)

            messages.success(request, "Weight Added Successfully")

    return render(request, "CareTaker/addWeightChart.html")


def ctViewResident(request):
    data = Residents.objects.all()
    return render(request, "CareTaker/ctViewResident.html", {'data': data})


def food_timetable_view(request):
    id = request.GET.get('id')
    data = FoodTimeTable.objects.filter(resident=id)
    print(data)
    return render(request, 'CareTaker/food_timetable_view.html', {'data': data, 'id': id})


def viewWeightChart(request):
    resident_id = request.GET.get('id')

    # Define a dictionary to map month names to their numerical representation
    month_order_map = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12,
    }

    # Define a custom ordering based on the numerical representation of months
    month_order = Case(
        *[When(month=month_name, then=month_number)
          for month_name, month_number in month_order_map.items()],
        default=0,
        output_field=IntegerField()
    )

    data = WeightChart.objects.filter(resident=resident_id).values(
        'month', 'year', 'weight').annotate(month_order=month_order).order_by('year', 'month_order')
    chart_data = [{'month': entry['month'], 'year': entry['year'],
                   'weight': entry['weight']} for entry in data]
    chart_data_json = json.dumps(chart_data)  # Convert data to JSON format
    return render(request, "CareTaker/ctViewWeightChart.html", {'chart_data': chart_data_json})
# =========================NURSE


def nurseHome(request):
    return render(request, "NURSE/nurseHome.html")


def nurseViewResidents(request):
    data = Residents.objects.all()
    return render(request, "NURSE/nurseViewResidents.html", {'data': data})


def addMedicine(request):
    id = request.GET.get('id')
    id = Residents.objects.get(id=id)

    print(id, '--------------------------------')
    if request.POST:
        name = request.POST['name']
        dosage = request.POST['dosage']
        frequency = request.POST['frequency']
        bf_af = request.POST['bf_af']
        notes = request.POST['notes']
        if Medicine.objects.filter(resident=id, name=name, dosage=dosage, frequency=frequency, bf_af=bf_af).exists():
            messages.success(request, "This prescription already exists!!!")
            return redirect('/nurseViewResidents')
        else:
            medicine = Medicine.objects.create(
                resident=id, name=name, dosage=dosage, frequency=frequency, bf_af=bf_af, notes=notes)
            medicine.save()
            print('--------------------------medicine>', medicine)

            messages.success(request, "Prescription Added Successfully")

        # print(name,dosage,frequency,bf_af,notes,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    # data = Residents.objects.all()
    return render(request, "NURSE/addMedicine.html")


def addCarePlan(request):
    id = request.GET.get('id')
    id = Residents.objects.get(id=id)

    print(id, '--------------------------------')
    if request.POST:
        likeOrdislike = request.POST['likeOrdislike']
        notes = request.POST['notes']
        if CarePlan.objects.filter(resident=id, note=notes).exists():
            messages.success(request, "Already exists!!!")
            return redirect('/nurseViewResidents')
        else:
            carePlan = CarePlan.objects.create(
                resident=id, note=notes, likeOrdislike=likeOrdislike)
            carePlan.save()
            # print('--------------------------medicine>', medicine)

            messages.success(request, "Care Plan Added Successfully")

    return render(request, "NURSE/addCarePlan.html")


def viewMedicine(request):
    id = request.GET.get('id')
    data = Medicine.objects.filter(resident=id)
    return render(request, "NURSE/viewMedicine.html", {'data': data})


def viewCarePlan(request):
    id = request.GET.get('id')
    data = CarePlan.objects.filter(resident=id)
    return render(request, "NURSE/viewCarePlan.html", {'data': data})


def deleteMed(request):
    id = request.GET.get('id')
    Medicine.objects.filter(id=id).delete()


def deleteCarePlan(request):
    id = request.GET.get('id')
    CarePlan.objects.filter(id=id).delete()

    return redirect('/nurseViewResidents')


def uploadEmergencySituation(request):
    residents = Residents.objects.all()
    if request.POST:
        resident=request.POST['resident']
        res=Residents.objects.get(id=resident)
        situation = request.POST['situation']
        print(res,situation)
        emSit=EmergencySituation.objects.create(resident=res,situation=situation,status='sent')
        emSit.save()
        messages.success(request, "Emergency Situation Sent!!!")    
        return redirect('/nurseviewEmergencySituations')
    return render(request, 'NURSE/uploadEmergencySituation.html', {'residents': residents})

def nurseviewEmergencySituations(request):
    data = EmergencySituation.objects.all()
    return render(request, 'NURSE/nurseviewEmergencySituations.html',{'data': data})
# ======================== DOCTOR


def doctorHome(request):
    emergencySituation=EmergencySituation.objects.filter(status='sent')
    print(emergencySituation,"<<<<<<<<<<<----------------------------------------------------------------EMSituationSituation")
    return render(request, "DOCTOR/doctorHome.html",{'emergencySituation': emergencySituation})


def viewEmergencySituations(request):
    data = EmergencySituation.objects.all()

    if request.POST:
        id = request.POST['id']
        print(id,"________________________________________________________________")
        reply=request.POST['reply']
        img = EmergencySituation.objects.get(id=id)
        if "file" in request.FILES:
            file = request.FILES['file']
            img.file = file
            img.save()
        else:
            return HttpResponse("<script>alert('Upload an image');window.location.href='/viewEmergencySituations'</script>")
        da = EmergencySituation.objects.filter(id=id).update(reply=reply,status='replied')
        messages.success(request, "Reply Sent!!!")    
        return redirect('/viewEmergencySituations')
    return render(request, "DOCTOR/viewEmergencySituations.html",{'data': data})




########################################### Chat Section###########################################

def chat(request):
    uid = request.session["uid"]
    # Artists
    name=""
    # print(uid,"uid<<<----------")
    artistData = Doctor.objects.all()
    id = request.GET.get("id")
    # print("--------------------->>>",id)
    getChatData = Chat.objects.filter(Q(uid__login=uid) & Q(artistid=id))
    print(getChatData, "<<<getChatData----------------------------------------------------------------")
    
    current_time = datetime.now().time()
    formatted_time = current_time.strftime("%H:%M")
    userid = Nurse.objects.get(login__id=uid)
    if id:
        artistid = Doctor.objects.get(id=id)
        name=artistid.name
        print(name,"<<<userid----------------------------------------------------------------")
    if request.POST:
        message = request.POST["message"]
        sendMsg = Chat.objects.create(uid=userid,message=message,artistid=artistid,time=formatted_time,utype="Nurse")
        sendMsg.save()
    return render(request,"NURSE/chat.html"
                  ,{"artistData": artistData, "getChatData": getChatData,"artistid":name}
                  )


def reply(request):
    uid = request.session["uid"]
    name=""
    userData = Nurse.objects.all()
    id = request.GET.get("id")
    getChatData = Chat.objects.filter(Q(artistid__login=uid) & Q(uid=id))
    print(getChatData, "<<<getChatData----------------------------------------------------------------")
    current_time = datetime.now().time()
    formatted_time = current_time.strftime("%H:%M")
    artistid = Doctor.objects.get(login__id=uid)
    if id:
        userid = Nurse.objects.get(id=id)
        name=userid.name
    if request.POST:
        message = request.POST["message"]
        sendMsg = Chat.objects.create(uid=userid,message=message,artistid=artistid,time=formatted_time,utype="Doctor")
        sendMsg.save()
    return render(request,"DOCTOR/chat.html"
                  ,{"userData": userData, "getChatData": getChatData,"userid":name}
                  )


#########################################################################################
def udp(request):
    Chat.objects.all().delete()
    return HttpResponse("Done==========🏆")
#########################################################################################
