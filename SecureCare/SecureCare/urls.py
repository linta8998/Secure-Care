from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('login/',views.login),
    path('adminHome/',views.adminHome),
    
    path('addResidents/',views.addResidents),
    path('viewResidents/',views.viewResidents),
    path('deleteResident/',views.deleteResident),
    path('updateResident/',views.updateResident),
    path('adminViewChart/',views.adminViewChart),
    
    path('addCareTaker/',views.addCareTaker),
    path('viewCareTaker/',views.viewCareTaker),
    path('updateCareTaker/',views.updateCareTaker),
    path('deleteCareTaker/',views.deleteCareTaker),
    
    path('addNurse/',views.addNurse),
    path('viewNurse/',views.viewNurse),
    path('updateNurse/',views.updateNurse),
    path('deleteNurse/',views.deleteNurse),
    
    path('addDoctor/',views.addDoctor),
    path('viewDoctor/',views.viewDoctor),
    path('updateDoctor/',views.updateDoctor),
    path('deleteDoctor/',views.deleteDoctor),
    
    path('adminViewCareplan/',views.adminViewCareplan),
    path('adminDeleteCareplan/',views.adminDeleteCareplan),
    
    
    #CareTaker
    path('careTakerHome/',views.careTakerHome),
    path('addFoodTt/',views.addFoodTt),
    path('ctViewResident/',views.ctViewResident),
    path('addWeightChart/',views.addWeightChart),
    path('viewWeightChart/',views.viewWeightChart),
    path('food_timetable_view/',views.food_timetable_view),
    
    #Nurse
    path('nurseHome/',views.nurseHome),
    path('nurseViewResidents/',views.nurseViewResidents),
    path('addMedicine/',views.addMedicine),
    path('viewMedicine/',views.viewMedicine),
    path('deleteMed/',views.deleteMed),
    path('addCarePlan/',views.addCarePlan),
    path('viewCarePlan/',views.viewCarePlan),
    path('deleteCarePlan/',views.deleteCarePlan),
    
    path('uploadEmergencySituation/',views.uploadEmergencySituation),
    path('nurseviewEmergencySituations/',views.nurseviewEmergencySituations),
    
    path('chat/',views.chat),
    
    #Docotr
    path('doctorHome/',views.doctorHome),
    
    path('viewEmergencySituations/',views.viewEmergencySituations),
    path('reply/',views.reply),
    
]
