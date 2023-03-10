"""BTL_nghia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App import views, AdminViews, StaffViews
urlpatterns = [
    path('', views.ShowLoginPage, name="show_login"),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user, name="logout"),
    path('doLogin', views.doLogin, name="do_login"),
   
    path('admin_home', AdminViews.admin_home, name="admin_home"),
    path('admin_profile', AdminViews.admin_profile, name="admin_profile"),
    path('admin_profile_save', AdminViews.admin_profile_save, name="admin_profile_save"),
    path('add_staff',AdminViews.add_staff,name="add_staff"),
    path('add_staff_save', AdminViews.add_staff_save,name="add_staff_save"),
    path('check_email_exist', AdminViews.check_email_exist, name="check_email_exist"),
    path('check_username_exist', AdminViews.check_username_exist, name="check_username_exist"),
    path('manage_staff', AdminViews.manage_staff, name="manage_staff"),
    path('edit_staff/<str:staff_id>', AdminViews.edit_staff, name="edit_staff"),
    path('edit_staff_save', AdminViews.edit_staff_save, name="edit_staff_save"),
    path('Quan_ly_to_chuc_cap_phep', AdminViews.QuanLyToChucCapPhep, name="Quan_ly_to_chuc_cap_phep"),
    path('Luu_to_chuc_cap_phep', AdminViews.LuuToChucCapPhep, name="Luu_to_chuc_cap_phep"),
    path('Quan_ly_giay_phep', AdminViews.QuanLyGiayPhep, name="Quan_ly_giay_phep"),
    path('Luu_giay_phep', AdminViews.LuuGiayPhep, name="Luu_giay_phep"),
    path('Quan_ly_vung_chan_nuoi_1', AdminViews.QuanLyVungChanNuoi, name="Quan_vung_chan_nuoi_1"),


    path('staff_home', StaffViews.staff_home, name="staff_home"),
    path('staff_profile', StaffViews.staff_profile, name="staff_profile"),
    path('staff_profile_save', StaffViews.staff_profile_save, name="staff_profile_save"),
    path('Them_loai_co_so', StaffViews.Them_loai_co_so, name="Them_loai_co_so"),
    path('Luu_loai_co_so', StaffViews.Luu_them_thong_tin_loai_co_so, name="Luu_loai_co_so"),
    path('Them_co_so/', StaffViews.Them_co_so, name="Them_co_so"),
    path('luu_co_so/', StaffViews.Luu_co_so,name="Luu_co_so"),
    path('Quan_ly_co_so', StaffViews.QuanLyCoSo, name="Quan_ly_co_so"),
    path('Sua_co_so/<str:coso_id>', StaffViews.Sua_co_so, name="Sua_co_so"),
    path('Luu_sua_co_so', StaffViews.Luu_sua_co_so, name="Luu_sua_co_so"),
    path('Addthongtincosothuy',StaffViews.Addthongtincosothuy, name="Addthongtincosothuy"),
    path('Luuthongtincosothuy',StaffViews.Luuthongtincosothuy, name="Luuthongtincosothuy"),

    path('Quanlychicucthuy', StaffViews.Quanlychicucthuy, name="Quanlychicucthuy"),
    path('suathongtinchicucthuy/<str:thuy_id>', StaffViews.suathongtinchicucthuy, name="suathongtinchicucthuy"),
    path('luusuathongtinchicucthuy', StaffViews.luusuathongtinchicucthuy, name="luusuathongtinchicucthuy"),

    path('adddailybanthuoc',StaffViews.adddailybanthuoc, name="adddailybanthuoc"),
    path('luuthongtindailybanthuoc',StaffViews.luuthongtindailybanthuoc, name="luuthongtindailybanthuoc"),
    path('Quanlydailybanthuoc', StaffViews.Quanlydailybanthuoc, name="Quanlydailybanthuoc"),
    path('suathongtindailybanthuoc/<str:thuoc_id>', StaffViews.suathongtindailybanthuoc, name="suathongtindailybanthuoc"),
    path('luusuathongtindailybanthuoc', StaffViews.luusuathongtindailybanthuoc, name="luusuathongtindailybanthuoc"),

    path('Them_vung_chan_nuoi', StaffViews.ThemVungChanNuoi, name="Them_vung_chan_nuoi"),
    path('Luu_vung_chan_nuoi', StaffViews.LuuVungChanNuoi, name="Luu_vung_chan_nuoi"),
    path('Quan_ly_vung_chan_nuoi', StaffViews.QuanLyVungChanNuoi, name="Quan_vung_chan_nuoi"),
    path('Sua_vung_chan_nuoi/<str:vung_id>', StaffViews.SuaVungChanNuoi, name="Sua_vung_chan_nuoi"),
    path('Luu_sua_vung_chan_nuoi', StaffViews.Luu_Sua_Vung_Chan_Chan_Nuoi, name="Luu_sua_vung_chan_nuoi"),

]
