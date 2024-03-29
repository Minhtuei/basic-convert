from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter, math , datetime, pytz , requests
def open_application(Return=None):
    
    username=name_typing.get()
    password=password_typing.get()
    
    if len(username) <=14 and password=='minhtueit123':
        if save.get()==1:
            auto_fill_password='1'
        if save.get()==0:
            auto_fill_password='0'
        with open('login.txt','w',encoding='utf8') as save_login:
            save_login.write(f'User: {username}\nPassword: {password}\nSavepass: {auto_fill_password}')
        def open_setting():
            global choice_colour,choice_font,tp_number,pc_symbol,choice_dv
            with open('setting.txt','r') as fr:
                setting=fr.readlines()
            for i in setting:
                if 'Font' in i:
                    choice_font=i[6:None].replace('\n','')
                if 'BG' in i:
                    choice_colour=i[4:None].replace('\n','')
                if 'DV' in i:
                    choice_dv=i[4:5].replace('\n','')
                if 'TP' in i:
                    tp_number=i[4:5].replace('\n','')
                if 'PC' in i:
                    pc_symbol=i[4:5]
                
            return choice_colour,choice_font,tp_number,pc_symbol,choice_dv
        def save_setting():
            global choice_colour,choice_font,tp_number,pc_symbol,choice_dv
            with open('setting.txt','w') as fw:
                fw.write(f'Font: {basic_font}\nBG: {basic_colour}\nDV: {dv_choice}\nTP: {tp_choice}\nPC: {pc_choice}')


        login.destroy()
        root=Tk()
        root.title('Convert Generator')
        root.geometry('800x600+250+0')

        root.iconbitmap('img\icon.ico')
        root.resizable(0,0)



        ###########Hàm standard ############
        # def :
        #     Chb_1.grid_forget()
        def get_API_currency():
            url='https://api.exchangerate-api.com/v4/latest/USD'
            data=requests.get(url).json()
            global currencies
            currencies=data['rates']
            return currencies
        def mg_to_standard():
            root.bind('<Return>',convert)
            btn_n.configure(command=convert)
            tb.delete(0,END)
            return

        def set_bg():
            root['background']=basic_colour
            lbl_2.configure(bg=basic_colour)
            lbl_3.configure(bg=basic_colour)
            lb.configure(bg=basic_colour)
        def set_font():
            lbl_2.configure(font=(basic_font,24,'bold'))
            lbl_3.configure(font=(basic_font,24))
            lb.configure(font=(basic_font,25,'bold'))
            btn_1.configure(font=(basic_font,18))
            btn_2.configure(font=(basic_font,18))
            btn_3.configure(font=(basic_font,18))
            btn_4.configure(font=(basic_font,18))
            btn_5.configure(font=(basic_font,18))
            btn_6.configure(font=(basic_font,18))
            btn_7.configure(font=(basic_font,18))
            btn_8.configure(font=(basic_font,18))
            btn_9.configure(font=(basic_font,18))
            btn_10.configure(font=(basic_font,18))
            btn_11.configure(font=(basic_font,18))
            btn_12.configure(font=(basic_font,18))
            btn_13.configure(font=(basic_font,18))
            btn_14.configure(font=(basic_font,18))
            btn_15.configure(font=(basic_font,18))
            btn_n.configure(font=(basic_font,20,'bold'))
            btn_e.configure(font=(basic_font,20,'bold'))
            if basic_font=='Helvetica' or basic_font=='Arial':
                btn_1.configure(font=(basic_font,17))
                btn_9.configure(font=(basic_font,16))
                btn_10.configure(font=(basic_font,17))
        def main_default():
            global basic_font
            global basic_colour
            global process
            global tp_choice,pc_choice,tp_number,pc_symbol,dv_choice,choice_dv
            open_setting()
            basic_colour=choice_colour
            root['background']=basic_colour
            basic_font=choice_font
            process=''
            tp_choice=tp_number
            pc_choice=int(pc_symbol)
            dv_choice=int(choice_dv)
            return


        main_default()
        def round_process():
            global process
            process=round(process,int(tp_choice))
            return process
        def comma_selected():
            global pc_choice, process
            if pc_choice==1:
                process="{:,}".format(process)

            if pc_choice==2:
                process="{:,}".format(process).replace(',',' ')

            if pc_choice==3:
                process=str(process)
            
                

        ###############Hàm button##############




        def kl():
            lb.configure(text='Bạn ơi cho mình đổi đơn vị khối lượng')
            cb_1['values']=('tấn','tấn (UK)','tấn (US)','kg','g','mg','lb','ct','oz','gr')
            cb_1.current(0)
            if dv_choice==1:
                cb_2['values']=('kg')
            if dv_choice==2:
                cb_2['values']=('tấn (UK)','lb','oz','gr')
            if dv_choice==3:
                cb_2['values']=('tấn (US)','lb','oz','gr')
            if dv_choice==4:
                cb_2['values']=('tấn','tấn (UK)','tấn (US)','kg','g','mg','lb','ct','oz','gr')
            cb_2.current(0)
            mg_to_standard()
            return
        def nđ():
            lb.configure(text='Bạn ơi cho mình đổi đơn vị nhiệt độ !')
            cb_1['values']=('°C','°F','K','°R')
            cb_1.current(0)
            if dv_choice==1:
                cb_2['values']=('K')
            if dv_choice==2:
                cb_2['values']=('°F')
            if dv_choice==3:
                cb_2['values']=('°F')
            if dv_choice==4:
                cb_2['values']=('°C','°F','K','°R')
            cb_2.current(0)
            mg_to_standard()
            return
        def đd():
            lb.configure(text='Bạn ơi cho mình đổi đơn vị độ dài !')
            cb_1['values']=('km','m','cm','mm','µm','nm','pm','Å','inch','mi','ft','yd')
            cb_1.current(0)
            if dv_choice==1:
                cb_2['values']=('m')
            if dv_choice==2:
                cb_2['values']=('inch','mi','ft','yd')
            if dv_choice==3:
                cb_2['values']=('inch','mi','ft','yd')
            if dv_choice==4:
                cb_2['values']=('km','m','cm','mm','µm','nm','pm','Å','inch','mi','ft','yd')
            cb_2.current(0)
            mg_to_standard()
            return
        def dt():
            lb.configure(text='Bạn ơi cho mình đổi đơn vị diện tích !')
            cb_1['values']=('km2','ha','a','m2','cm2','ft2','acre')
            cb_1.current(0)
            if dv_choice==1:
                cb_2['values']=('m2')
            if dv_choice==2:
                cb_2['values']=('acre')
            if dv_choice==3:
                cb_2['values']=('ft2','acre')
            if dv_choice==4:
                cb_2['values']=('km2','ha','a','m2','cm2','ft2','acre')
            cb_2.current(0)
            mg_to_standard()
            return
        def tht():
            lb.configure(text='Bạn ơi cho mình đổi đơn vị thể tích !')
            cb_1['values']=('m3','cm3','mm3','l','ml','bushel (UK)','bushel (US)','gal (US)','gal (UK)','ft3')
            cb_1.current(0)
            if dv_choice==1:
                cb_2['values']=('m3')
            if dv_choice==2:
                cb_2['values']=('bushel (UK)','gal (UK)')
            if dv_choice==3:
                cb_2['values']=('bushel (US)','gal (US)','ft3')
            if dv_choice==4:
                cb_2['values']=('m3','cm3','mm3','l','ml','bushel (UK)','bushel (US)','gal (US)','gal (UK)','ft3')
            cb_2.current(0)
            mg_to_standard()
            return
        def ap():
            lb.configure(text='Bạn ơi cho mình đổi đơn vị áp suất !')
            cb_1['values']=('Pa','bar','at','atm','Torr','lbf/in2','mmHg')
            cb_1.current(0)
            if dv_choice==1:
                cb_2['values']=('Pa')
            if dv_choice==2:
                cb_2['values']=('lbf/in2')
            if dv_choice==3:
                cb_2['values']=('lbf/in2')
            if dv_choice==4:
                cb_2['values']=('Pa','bar','at','atm','Torr','lbf/in2','mmHg')
            cb_2.current(0)
            mg_to_standard()
        def vt():
            lb.configure(text='Bạn ơi cho mình đổi đơn vị vận tốc !')
            cb_1['values']=('km/h','m/s','mph','ft/s','kn (kt)','M')
            cb_1.current(0)
            if dv_choice==1:
                cb_2['values']=('m/s')
            if dv_choice==2:
                cb_2['values']=('km/h','mph')
            if dv_choice==3:
                cb_2['values']=('km/h','mph')
            if dv_choice==4:
                cb_2['values']=('km/h','m/s','mph','ft/s','kn (kt)','M')
            cb_2.current(0)
            mg_to_standard()
            return
        def tg():
            lb.configure(text='Bạn ơi cho mình đổi đơn vị thời gian !')
            cb_1['values']=('giây','phút','giờ','ngày','tuần','tháng','quý','năm','thập kỷ','thế kỷ','thiên niên kỷ')
            cb_1.current(0)
            if dv_choice==1 or dv_choice==2 or dv_choice==3 :
                cb_2['values']=('giây')
            if dv_choice==4:
                cb_2['values']=('giây','phút','giờ','ngày','tuần','tháng','quý','năm','thập kỷ','thế kỷ','thiên niên kỷ')
            cb_2.current(0)
            mg_to_standard()
            return
        def nl():
            lb.configure(text='Bạn ơi cho mình đổi đơn vị năng lượng !')
            cb_1['values']=('J','kJ','cal','kcal','Btu','kWh','eV','MeV')
            cb_1.current(0)
            if dv_choice==1:
                cb_2['values']=('J')
            if dv_choice==2:
                cb_2['values']=('Btu')
            if dv_choice==3:
                cb_2['values']=('J','kJ','cal','kcal')
            if dv_choice==4:
                cb_2['values']=('J','kJ','cal','kcal','Btu','kWh','eV','MeV')
            cb_2.current(0)
            mg_to_standard()
            return
        def cs():
            lb.configure(text='Bạn ơi cho mình đổi đơn vị công suất !')
            cb_1['values']=('W','kW','MW','hp','Btu/s','dBm','cal/h')
            cb_1.current(0)
            if dv_choice==1:
                cb_2['values']='W'
            if dv_choice==2:
                cb_2['values']=('Btu/s','hp')
            if dv_choice==3:
                cb_2['values']=('W','kW','hp')
            if dv_choice==4:
                cb_2['values']=('W','kW','MW','hp','Btu/s','dBm','cal/h')
            cb_2.current(0)
            mg_to_standard()
            return
        def g():
            lb.configure(text='Bạn ơi cho mình đổi đơn vị góc !')
            cb_1['values']=('°',"'",'"','rad','^g')
            cb_1.current(0)
            if dv_choice==1:
                cb_2['values']=('rad')
            if dv_choice==2:
                cb_2['values']=('°','rad')
            if dv_choice==3:
                cb_2['values']=('°','rad')
            if dv_choice==4:
                cb_2['values']=('°',"'",'"','rad','^g')
            cb_2.current(0)
            mg_to_standard()
            return
        def mg():
            tb.delete(0,END)
            lb.configure(text='Bạn ơi cho mình đổi đơn vị múi giờ !')
            root.bind("<Return>",convert_datetime_timezone)
            cb_1['values'],cb_2['values']=pytz.all_timezones,pytz.all_timezones
            cb_1.current(306),cb_2.current(1)
            btn_n.configure(command=convert_datetime_timezone)
            dt_now=datetime.datetime.now().strftime("%H:%M:%S %d/%m/%Y")
            tb.insert(0,str(dt_now))
            return
        def dl():
            lb.configure(text='Bạn ơi cho mình đổi đơn vị dữ liệu !')
            cb_1['values'],cb_2['values']=('b','B','kB','MB','GB','TB','PB'),('b','B','kB','MB','GB','TB','PB')
            cb_1.current(0),cb_2.current(1)
            mg_to_standard()
            return
        def tt():
            tb.delete(0,END)
            lb.configure(text='Bạn ơi cho mình đổi đơn vị tiền tệ !')
            btn_n.configure(command=convert_currency)
            root.bind("<Return>",convert_currency)
            get_API_currency()
            cb_1['values'],cb_2['values']=list(currencies.keys()),list(currencies.keys())
            cb_1.current(149),cb_2.current(0)
            return
        def cđ():
            lb.configure(text=f'{username} ơi bạn cần mình đổi cái gì nè ?')
            cd=Toplevel()
            cd.grab_set()
            cd.title('Cài đặt')
            cd.geometry('400x600+400+50')
            cd.resizable(0,0)
            cd.iconbitmap("img\setting.ico")
            cb_1['values'],cb_2['values']=(),()
            cb_1.delete(0,END),cb_2.delete(0,END)
            def font_selected():
                global basic_font
                basic_font=font_choices.get()
            def bg_to_standard():
                bg_1.configure(relief=RIDGE,overrelief=RAISED)
                bg_2.configure(relief=RIDGE,overrelief=RAISED)
                bg_3.configure(relief=RIDGE,overrelief=RAISED)
                bg_4.configure(relief=RIDGE,overrelief=RAISED)
            def bg_1_selected():
                global basic_colour
                bg_to_standard()
                bg_1.configure(relief=SUNKEN,overrelief=SUNKEN)
                basic_colour='#fff894'


                return 
            def bg_2_selected():
                global basic_colour
                bg_to_standard()
                bg_2.configure(relief=SUNKEN,overrelief=SUNKEN)
                basic_colour='#ffb9ce'


                return 
            def bg_3_selected():
                global basic_colour
                bg_to_standard()
                bg_3.configure(relief=SUNKEN,overrelief=SUNKEN)
                basic_colour='#a2ffa2'
                return
            def bg_4_selected():
                global basic_colour
                bg_to_standard()
                bg_4.configure(relief=SUNKEN,overrelief=SUNKEN)
                basic_colour='#34d8eb'
                return
            
            
            def dv_SI():                
                dv_c2.deselect()
                dv_c3.deselect()
                dv_c4.deselect()
                return
            def dv_Anh():      
                dv_c1.deselect()
                dv_c3.deselect()
                dv_c4.deselect()
                return
            def dv_My():   
                dv_c1.deselect()
                dv_c2.deselect()
                dv_c4.deselect()
                return
            def dv_All():   
                dv_c1.deselect()
                dv_c2.deselect()
                dv_c3.deselect()
                return
            def thap_phan(Return=None):
                configure=round(9.1234567891,int(tp_cb.get()))          
                ex_1.configure(text='Ví dụ: '+str(configure))
                return 
            
            
            def chu_thich():
                ct=Tk()
                ct.geometry('300x500+1050+50')
                ct.title('Bảng chú thích')
                ct.resizable(0,0)
                ct.iconbitmap("img\info.ico")
                def ct_kl():
                    global lbl_kl,lbl_ct_1,lbl_ct_2,lbl_ct_3,lbl_ct_4,lbl_ct_5,lbl_ct_6,lbl_ct_7,lbl_ct_8,lbl_ct_9,lbl_ct_10,lbl_ct_11,lbl_ct_12,lbl_status,ct_colour
                    ct_colour='#aae4e6'
                    lbl_kl=Label(ct,text='* Khối lượng:',font=('Times',25,'bold','italic'),bg=ct_colour,fg='#ff4d00')
                    lbl_kl.place(x=20,y=10)
                    lbl_ct_1=Label(ct,text='+ Tấn:                 tấn theo hệ mét',font=('Times',15),bg=ct_colour)
                    lbl_ct_1.place(x=20,y=60)
                    lbl_ct_2=Label(ct,text='+ Tấn (UK):        tấn dài',font=('Times',15),bg=ct_colour)
                    lbl_ct_2.place(x=20,y=90)
                    lbl_ct_3=Label(ct,text='+ Tấn (US):        tấn ngắn',font=('Times',15),bg=ct_colour)
                    lbl_ct_3.place(x=20,y=120)
                    lbl_ct_4=Label(ct,text='+ Kg:                  kilogram',font=('Times',15),bg=ct_colour)
                    lbl_ct_4.place(x=20,y=150)
                    lbl_ct_5=Label(ct,text='+ g:                     gram',font=('Times',15),bg=ct_colour)
                    lbl_ct_5.place(x=20,y=180)
                    lbl_ct_6=Label(ct,text='+ mg:                  milligram',font=('Times',15),bg=ct_colour)
                    lbl_ct_6.place(x=20,y=210)
                    lbl_ct_7=Label(ct,text='+ lb:                   pound',font=('Times',15),bg=ct_colour)
                    lbl_ct_7.place(x=20,y=240)
                    lbl_ct_8=Label(ct,text='+ ct:                   carat',font=('Times',15),bg=ct_colour)
                    lbl_ct_8.place(x=20,y=270)
                    lbl_ct_9=Label(ct,text='+ oz:                  ounce',font=('Times',15),bg=ct_colour)
                    lbl_ct_9.place(x=20,y=300)
                    lbl_ct_10=Label(ct,text='+ gr:                  grain',font=('Times',15),bg=ct_colour)
                    lbl_ct_10.place(x=20,y=330)
                    lbl_ct_11=Label(ct,text='',font=('Times',15),bg=ct_colour)
                    lbl_ct_11.place(x=20,y=360)
                    lbl_ct_12=Label(ct,text='',font=('Times',15),bg=ct_colour)
                    lbl_ct_12.place(x=20,y=390)
                    pre_btn.configure(state=DISABLED)
                    next_btn.configure(command=ct_nd)
                    lbl_status=Label(ct,text='1/11',font=('Times',15,'bold'))
                    lbl_status.place(x=130,y=450)                  
                def ct_nd():
                    pre_btn.configure(state=NORMAL)
                    pre_btn.configure(command=ct_kl)
                    next_btn.configure(command=ct_đd)
                    lbl_kl.configure(text='* Nhiệt độ:')
                    lbl_ct_1.configure(text='+ °C:           độ Celsius')
                    lbl_ct_2.configure(text='+ °F:           độ Fahrenheit')
                    lbl_ct_3.configure(text='+ K:            độ Kelvin')
                    lbl_ct_4.configure(text='+ °R:           độ Rankine')
                    lbl_ct_5.configure(text='')
                    lbl_ct_6.configure(text='')
                    lbl_ct_7.configure(text='')
                    lbl_ct_8.configure(text='')
                    lbl_ct_9.configure(text='')
                    lbl_ct_10.configure(text='')
                    lbl_ct_11.configure(text='')
                    lbl_ct_12.configure(text='')
                    lbl_status.configure(text='2/11')
                def ct_đd ():
                    pre_btn.configure(command=ct_nd)
                    next_btn.configure(command=ct_dt)
                    lbl_kl.configure(text='* Độ dài:       ')
                    lbl_ct_1.configure(text='+ km:          kilometer       ')
                    lbl_ct_2.configure(text='+ m:            meter              ')
                    lbl_ct_3.configure(text='+ cm:          centimeter      ')
                    lbl_ct_4.configure(text='+ mm:         millimeter       ')
                    lbl_ct_5.configure(text='+ µm:          micrometer')
                    lbl_ct_6.configure(text='+ nm:          nanometer')
                    lbl_ct_7.configure(text='+ pm:          picometer')
                    lbl_ct_8.configure(text='+ Å:            armstrong')
                    lbl_ct_9.configure(text='+ inch:        inch')
                    lbl_ct_10.configure(text='+ mi:           mile (dặm)')
                    lbl_ct_11.configure(text='+ ft:             foot')
                    lbl_ct_12.configure(text='+ yd:           yard')
                    lbl_status.configure(text='3/11')
                def ct_dt ():
                    pre_btn.configure(command=ct_đd)
                    next_btn.configure(command=ct_tht)
                    lbl_kl.configure(text='* Diện tích:    ')
                    lbl_ct_1.configure(text='+ km2:           kilomet vuông  ')
                    lbl_ct_2.configure(text='+ ha:              hectare              ')
                    lbl_ct_3.configure(text='+ a:                are         ')
                    lbl_ct_4.configure(text='+ m2:             met vuông     ')
                    lbl_ct_5.configure(text='+ cm2:           centimet vuông ')
                    lbl_ct_6.configure(text='+ ft2:             foot vuông   ')
                    lbl_ct_7.configure(text='+ acre:           mẫu Anh       ')
                    lbl_ct_8.configure(text='')
                    lbl_ct_9.configure(text='')
                    lbl_ct_10.configure(text='')
                    lbl_ct_11.configure(text='')
                    lbl_ct_12.configure(text='')
                    lbl_status.configure(text='4/11')
                def ct_tht ():
                    pre_btn.configure(command=ct_dt)
                    next_btn.configure(command=ct_as)
                    lbl_kl.configure(text='* Thể tích:                       ')
                    lbl_ct_1.configure(text='+ m3:                      met khối         ')
                    lbl_ct_2.configure(text='+ cm3:                    centimet khối     ')
                    lbl_ct_3.configure(text='+ mm3:                   millimet khối      ')
                    lbl_ct_4.configure(text='+ l:                         lít            ')
                    lbl_ct_5.configure(text='+ ml:                      milli lít        ')
                    lbl_ct_6.configure(text='+ bushel (US):       bushel hệ Mỹ           ')
                    lbl_ct_7.configure(text='+ bushel (UK):      bushel hệ Anh           ')
                    lbl_ct_8.configure(text='+ gal (US):            gallon hệ Mỹ         ')
                    lbl_ct_9.configure(text='+ gal (UK):           gallon hệ Anh         ')
                    lbl_ct_10.configure(text='+ ft3:                     foot khối       ')
                    lbl_status.configure(text='5/11')
                def ct_as ():
                    pre_btn.configure(command=ct_tht)
                    next_btn.configure(command=ct_vt)
                    lbl_kl.configure(text='* Áp suất:                 ')
                    lbl_ct_1.configure(text='+ Pa:           pascal        ')
                    lbl_ct_2.configure(text='+ bar:          bar                ')
                    lbl_ct_3.configure(text='+ at:            atmosphere kỹ thuật        ')
                    lbl_ct_4.configure(text='+ atm:         atmosphere tiêu chuẩn        ')
                    lbl_ct_5.configure(text='+ Torr:        torr')
                    lbl_ct_6.configure(text='+ lbf/in2:    pound trên inch vuông')
                    lbl_ct_7.configure(text='+ mmHg:    millimet thủy ngân')
                    lbl_ct_8.configure(text='')
                    lbl_ct_9.configure(text='')
                    lbl_ct_10.configure(text='')
                    lbl_status.configure(text='6/11')
                def ct_vt ():
                    pre_btn.configure(command=ct_as)
                    next_btn.configure(command=ct_nl)
                    lbl_kl.configure(text='* Vận tốc:                 ')
                    lbl_ct_1.configure(text='+ km/h:           kilomet trên giờ                 ')
                    lbl_ct_2.configure(text='+ m/s:             met trên giây                 ')
                    lbl_ct_3.configure(text='+ mph:           dặm trên giờ                 ')
                    lbl_ct_4.configure(text='+ ft/s:             foot trên giây                 ')
                    lbl_ct_5.configure(text='+ kn (kt):        hải lý trên giờ')
                    lbl_ct_6.configure(text='+ M:              tốc độ âm thanh ')
                    lbl_ct_7.configure(text='')
                    lbl_ct_8.configure(text='')
                    lbl_ct_9.configure(text='')
                    lbl_ct_10.configure(text='')
                    lbl_status.configure(text='7/11')
                def ct_nl ():
                    pre_btn.configure(command=ct_vt)
                    next_btn.configure(command=ct_cs)
                    lbl_kl.configure(text='* Năng lượng:                      ')
                    lbl_ct_1.configure(text='+ J:               jun                      ')
                    lbl_ct_2.configure(text='+ kJ:             kilo jun                      ')
                    lbl_ct_3.configure(text='+ cal:            calo                      ')
                    lbl_ct_4.configure(text='+ kcal:          kilo calo                      ')
                    lbl_ct_5.configure(text='+ Btu:          đơn vị nhiệt Anh')
                    lbl_ct_6.configure(text='+ kWh:         kilowatt trên giờ')
                    lbl_ct_7.configure(text='+ eV:           electron volt')
                    lbl_ct_8.configure(text='+ MeV:        mega electron volt')
                    lbl_ct_9.configure(text='')
                    lbl_ct_10.configure(text='')
                    lbl_status.configure(text='8/11')
                def ct_cs ():
                    pre_btn.configure(command=ct_nl)
                    next_btn.configure(command=ct_g)
                    lbl_kl.configure(text='* Công suất:                        ')
                    lbl_ct_1.configure(text='+ W:           watt                        ')
                    lbl_ct_2.configure(text='+ kW:          kilowatt                        ')
                    lbl_ct_3.configure(text='+ MW:        megawatt                        ')
                    lbl_ct_4.configure(text='+ hp:           mã lực                        ')
                    lbl_ct_5.configure(text='+ Btu/s: đơn vị nhiệt Anh trên giây')
                    lbl_ct_6.configure(text='+ dBm:       decibel-milliwatt')
                    lbl_ct_7.configure(text='+ cal/h:       calo trên giờ')
                    lbl_ct_8.configure(text='')
                    lbl_ct_9.configure(text='')
                    lbl_ct_10.configure(text='')
                    lbl_status.configure(text='9/11')
                def ct_g ():
                    pre_btn.configure(command=ct_cs)
                    next_btn.configure(command=ct_dl)
                    next_btn.configure(state=NORMAL)    
                    lbl_kl.configure(text='* Góc:                  ')
                    lbl_ct_1.configure(text='+ °:              độ                  ')
                    lbl_ct_2.configure(text="+ ':              phút                  ")
                    lbl_ct_3.configure(text='+ ":              giây                  ')
                    lbl_ct_4.configure(text='+ rad:          radian                  ')
                    lbl_ct_5.configure(text='+ ^g:           gradian')
                    lbl_ct_6.configure(text='')
                    lbl_ct_7.configure(text='')
                    lbl_ct_8.configure(text='')
                    lbl_ct_9.configure(text='')
                    lbl_ct_10.configure(text='')
                    lbl_status.configure(text='10/11')
                def ct_dl ():
                    next_btn.configure(state=DISABLED)
                    pre_btn.configure(command=ct_g)
                    lbl_kl.configure(text='* Dữ liệu:               ')
                    lbl_ct_1.configure(text='+ b:                 bit                ')
                    lbl_ct_2.configure(text='+ B:                byte                 ')
                    lbl_ct_3.configure(text='+ kB:              kilobyte')
                    lbl_ct_4.configure(text='+ MB:            megabyte')
                    lbl_ct_5.configure(text='+ GB:            gigabyte')
                    lbl_ct_6.configure(text='+ TB:             tetrabyte ')
                    lbl_ct_7.configure(text='+ PB:             petabyte')
                    lbl_ct_8.configure(text='')
                    lbl_ct_9.configure(text='')
                    lbl_ct_10.configure(text='')
                    lbl_status.configure(text='11/11')


                next_btn=Button(ct,text='>>>',width=5,bd=5,relief=RIDGE,overrelief=RAISED)
                next_btn.place(x=200,y=450)
                pre_btn=Button(ct,text='<<<',width=5,bd=5,relief=RIDGE,overrelief=RAISED,state=DISABLED)
                pre_btn.place(x=50,y=450)
                ct_kl()
                ct['background']=ct_colour
                ct.mainloop()
         
            def phay_selected():
                dp_cb2.deselect()
                dp_cb3.deselect()
                ex_2=Label(cd,text='Ví dụ: 123,456,789.69',font=(basic_font,20,'italic'))
                ex_2.place(x=50,y=350)
            def cach_selected():
                dp_cb1.deselect()
                dp_cb3.deselect()
                ex_2=Label(cd,text='Ví dụ: 123 456 789.69',font=(basic_font,20,'italic'))
                ex_2.place(x=50,y=350)
            def khong_selected():
                dp_cb1.deselect()
                dp_cb2.deselect()
                ex_2=Label(cd,text='Ví dụ: 123456789.69',font=(basic_font,20,'italic'))
                ex_2.place(x=50,y=350)
            def default():
                font_choices.set('Times')
                bg_1_selected()
                dv_c4.select()
                dv_SI()
                tp_cb.set('3')
                thap_phan()
                dp_cb2.select()
                cach_selected()
                dv_c4.select()
                dv_All()
            def accept():
                global tp_choice,pc_choice,dv_choice
                set_bg()
                font_selected()
                set_font()
                tp_choice=tp_cb.get()
                if phay.get()==1:
                    pc_choice=1
                elif cach.get()==1:
                    pc_choice=2
                elif khong.get()==1:
                    pc_choice=3
                if var1.get()==1:
                    dv_choice=1
                elif var2.get()==1:
                    dv_choice=2
                elif var3.get()==1:
                    dv_choice=3
                elif var4.get()==1:
                    dv_choice=4  
                save_setting()
                cd.destroy()
            def last_setting():
                open_setting()
                font_choices.set(choice_font)
                if choice_colour=='#fff894':
                    bg_1_selected()
                elif choice_colour=='#ffb9ce':
                    bg_2_selected()
                elif choice_colour=='#a2ffa2':
                    bg_3_selected()
                elif choice_colour=='#34d8eb':
                    bg_4_selected()
                if choice_dv=='1':
                    dv_c1.select()
                elif choice_dv=='2':
                    dv_c2.select()
                elif choice_dv=='3':
                    dv_c3.select()
                elif choice_dv=='4':
                    dv_c4.select()
                tp_cb.set(tp_number)
                thap_phan()
                if pc_symbol=='1':
                    dp_cb1.select()
                    phay_selected()
                elif pc_symbol=='2':
                    dp_cb2.select()
                    cach_selected()
                elif pc_symbol=='3':
                    dp_cb3.select()
                    khong_selected()
            ##############Font############
            font_label=Label(cd,text='Font:',font=('Times',15,'bold'))
            font_label.place(x=10,y=10)
            font_choices=ttk.Combobox(cd,width=15)
            font_choices['values']=['Times','Helvetica','Arial']
            font_choices.current(0)
            font_choices.place(x=80,y=14)

            #######Background######
            bg_label=Label(cd,text='Màu nền:',font=('Times',15,'bold'))
            bg_label.place(x=10,y=60)

            bg_1=Button(cd,width=5,bg='#fff894',borderwidth=3,relief=RIDGE,overrelief=RAISED,command=bg_1_selected)
            bg_1.place(x=100,y=60)
            bg_2=Button(cd,width=5,bg='#ffb9ce',borderwidth=3,relief=RIDGE,overrelief=RAISED,command=bg_2_selected)
            bg_2.place(x=160,y=60)
            bg_3=Button(cd,width=5,bg='#a2ffa2',borderwidth=3,relief=RIDGE,overrelief=RAISED,command=bg_3_selected)
            bg_3.place(x=220,y=60)
            bg_4=Button(cd,width=5,bg='#34d8eb',borderwidth=3,relief=RIDGE,overrelief=RAISED,command=bg_4_selected)
            bg_4.place(x=280,y=60)
            

            ##################Hệ đơn vị############

            dv_label=Label(cd,text='Hệ đơn vị:',font=('Times',15,'bold'))
            dv_label.place(x=10,y=106)

            var1,var2,var3,var4=IntVar(),IntVar(),IntVar(),IntVar()
            dv_c1=Checkbutton(cd,text='SI',font=('Times',12),variable=var1,onvalue=1,offvalue=0,command=dv_SI)
            dv_c1.place(x=120,y=107)
            dv_c2=Checkbutton(cd,text='Anh',font=('Times',12),variable=var2,onvalue=1,offvalue=0,command=dv_Anh)
            dv_c2.place(x=180,y=107)
            dv_c3=Checkbutton(cd,text='Mỹ',font=('Times',12),variable=var3,onvalue=1,offvalue=0,command=dv_My)
            dv_c3.place(x=240,y=107)
            dv_c4=Checkbutton(cd,text='Tất cả',font=('Times',12),variable=var4,onvalue=1,offvalue=0,command=dv_All)
            dv_c4.place(x=300,y=107)
            ######################Chú thích##############################
            ct_label=Label(cd,text='Bảng chú thích đơn vị:',font=('Times',15,'bold'))
            ct_label.place(x=10,y=158)
            ct_btn=Button(cd,text='Nhấp để xem',font=('Times',15),width=10,borderwidth=3,command=chu_thich)
            ct_btn.place(x=220,y=152)

            ########################Thập phân ##############
            tp_label=Label(cd,text='Số chữ số thập phân:',font=('Times',15,'bold'))
            tp_label.place(x=10,y=210)
            tp_cb=ttk.Combobox(cd,width=5)
            lst=[]
            for i in range(0,11):
                lst.append(i)
            tp_cb['values']=lst
            tp_cb.current(3)
            tp_cb.place(x=200,y=215)
            
            ex_1=Label(cd,text='Ví dụ: 9.123',font=(basic_font,20,'italic'))
            ex_1.place(x=50,y=250)
            
            tp_cb.bind("<<ComboboxSelected>>", thap_phan)
            #######################Dấu phẩy phân cách#######################
            dp_label=Label(cd,text='Phân cách:',font=('Times',15,'bold'))
            dp_label.place(x=10,y=300)
            global phay,cach,khong
            phay=IntVar()
            cach=IntVar()
            khong=IntVar()  

            dp_cb1=Checkbutton(cd,text='Dấu phẩy',font=('Times',13),variable=phay,onvalue=1,offvalue=0,command=phay_selected)
            dp_cb1.place(x=110,y=300)
            dp_cb2=Checkbutton(cd,text='Dấu cách',font=('Times',13),variable=cach,onvalue=1,offvalue=0,command=cach_selected)
            dp_cb2.place(x=210,y=300)
            dp_cb3=Checkbutton(cd,text='Không',font=('Times',13),variable=khong,onvalue=1,offvalue=0,command=khong_selected)
            dp_cb3.place(x=310,y=300)

            ##################Setting###################
            default_btn=Button(cd,text='Mặc định',font=('Times',12),width=10,borderwidth=3,relief=RIDGE,overrelief=RAISED,command=default)
            default_btn.place(x=60,y=530)
            apply_btn=Button(cd,text='Xác nhận',font=('Times',12),width=10,borderwidth=3,relief=RIDGE,overrelief=RAISED,command=accept)
            apply_btn.place(x=170,y=530)
            cancel_btn=Button(cd,text='Hủy bỏ',font=('Times',12),width=10,borderwidth=3,command=cd.destroy,relief=RIDGE,overrelief=RAISED)
            cancel_btn.place(x=280,y=530)
            last_setting()

            return

        def ex():
            Input=cb_1.get()
            Output=cb_2.get()
            cb_1.set(Output)
            cb_2.set(Input)
            cb_1['values'],cb_2['values']=cb_2['values'],cb_1['values']
            tb.delete(0,END)
            tb.insert(0,str(process))
            return 
        ##############Hàm chuyển đổi ###################



        def convert_datetime_timezone(Return=None):
            try:
                global process
                Input=cb_1.get()
                Output=cb_2.get()
                process=tb.get()
                Input = pytz.timezone(Input)
                Output = pytz.timezone(Output)
                process = datetime.datetime.strptime(process,"%H:%M:%S %d/%m/%Y")
                process = Input.localize(process)
                process = process.astimezone(Output)
                process = process.strftime("%H:%M:%S %d/%m/%Y")
                list_box.insert(1,f'{tb.get()} {Input} = {process} {Output}')
                list_box.activate(END)
                list_box.config(xscrollcommand=scrollbar_2.set,yscrollcommand=scrollbar_1.set)
                scrollbar_1.config(command=list_box.yview)
                scrollbar_2.config(command=list_box.xview)
                return  lbl_3.configure(text=process+' '+str(Output))
            except ValueError:
                messagebox.showerror('Lỗi','Vui lòng nhập đúng định dạng thời gian\nVí dụ: 01:02:03 04/05/2006')
        def convert_currency(Return=None):
            try:
                global process
                get_API_currency()
                typing=tb.get()
                if ',' in typing:
                    typing=typing.replace(',','')
                if ' ' in typing:
                    typing=typing.replace(' ','')  
                process=float(typing)
                from_currency=cb_1.get()
                to_currency=cb_2.get()
                if from_currency != 'USD' : 
                    process = process / currencies[from_currency]   
                process = process * currencies[to_currency]
                round_process()
                comma_selected()
                list_box.insert(1,f'{tb.get()} {from_currency} = {process} {to_currency}')
                list_box.activate(END)
                list_box.config(xscrollcommand=scrollbar_2.set,yscrollcommand=scrollbar_1.set)
                scrollbar_1.config(command=list_box.yview)
                scrollbar_2.config(command=list_box.xview)
                return  lbl_3.configure(text=process+" "+to_currency)    
            except ValueError:
                messagebox.showerror('Lỗi','Vui lòng nhập đúng giá trị tiền tệ !')
        def convert(Return=None):
            try: 
                global process
                Input=cb_1.get()
                Output=cb_2.get()
                calculating=tb.get()
                if ',' in calculating:
                    calculating=calculating.replace(',','')
                if ' ' in calculating:
                    calculating=calculating.replace(' ','')  
                calculating=float(calculating)

                re_Input=Input

                #########Khối lượng:#########
                if Input==Output:
                    process=calculating
                
                if Input=='kg':
                    Input='g'
                    calculating=calculating*1000
                if Input=='mg':
                    Input='g'
                    calculating=calculating/1000
                if Input=='tấn':
                    Input='g'
                    calculating=calculating*(10**6)
                if Input=='tấn (UK)':
                    Input='g'
                    calculating=calculating*(453.59237*2240)
                if Input=='tấn (US)':
                    Input='g'
                    calculating=calculating*(453.59237*2000)
                if Input=='lb':
                    Input='g'
                    calculating=calculating*453.59237
                if Input=='oz':
                    Input='g'
                    calculating=calculating*28.349523125
                if Input=='ct':
                    Input='g'
                    calculating=calculating/5
                if Input=='gr':
                    Input='g'
                    calculating=(calculating/1000)*64.79891
                if Input=='g':
                    if Output=='tấn':
                        process=calculating/(10**6)
                    elif Output=='tấn (UK)':
                        process=calculating/(453.59237*2240)
                    elif Output=='tấn (US)':
                        process=calculating/(453.59237*2000)
                    elif Output=='kg':
                        process=calculating/1000
                    elif Output=='mg':
                        process=calculating*1000
                    elif Output=='lb':
                        process=calculating/453.59237
                    elif Output=='oz':
                        process=calculating/28.349523125
                    elif Output=='ct':
                        process=calculating*5
                    elif Output=='gr':
                        process=(calculating*1000)/64.79891
                    elif Output=='g':
                        process=calculating





                #########Nhiệt độ#########
                if Input=='°C':
                    if Output=='°F':
                        process=(calculating*1.8)+32
                    elif Output=='K':
                        process=calculating+273.15
                    elif Output=='°R':
                        process=(calculating*1.8)+32+459.67
                if Input=='°F':
                    if Output=='°C':
                        process=(calculating-32)/1.8
                    elif Output=='K':
                        process=((calculating-32)/1.8)+273.15
                    elif Output=='°R':
                        process=calculating+459.67
                if Input=='K':
                    if Output=='°F':
                        process=((calculating-273.15)*1.8)+32
                    elif Output=='°C':
                        process=calculating-273.15
                    elif Output=='°R':
                        process=((calculating-273.15)*1.8)+32+459.67
                if Input=='°R':
                    if Output=='°F':
                        process=calculating-459.67
                    elif Output=='°C':
                        process=(calculating-459.67-32)/1.8
                    elif Output=='K':
                        process=(calculating-459.67-32)/1.8+273.15
                
                
                


                #########Độ dài#########
                if Input=='yd':
                    Input='inch'
                    calculating=calculating*36
                if Input=='ft':
                    Input='inch'
                    calculating=calculating*12
                if Input=='mi':
                    Input='cm'
                    calculating=calculating*160934.4
                if Input=='inch':
                    Input='cm'
                    calculating=calculating*2.54
                if Input=='km':
                    Input='cm'
                    calculating=calculating*(10**5)
                if Input=='m':
                    Input='cm'
                    calculating=calculating*(10**2)
                if Input=='mm':
                    Input='cm'
                    calculating=calculating/(10)
                if Input=='µm':
                    Input='cm'
                    calculating=calculating/(10**4)
                if Input=='nm':
                    Input='cm'
                    calculating=calculating/(10**7)
                if Input=='pm':
                    Input='cm'
                    calculating=calculating/(10**10)
                if Input=='Å':
                    Input='cm'
                    calculating=calculating/(10**8)
                if Input=='cm':
                    if Output=='km':
                        process=calculating/100000
                    elif Output=='m' :
                        process=calculating/100
                    elif Output=='mm' :
                        process=calculating*10
                    elif Output=='µm' :
                        process=calculating*(10**4)
                    elif Output=='nm' :
                        process=calculating*(10**7)
                    elif Output=='pm' :
                        process=calculating*(10**10)
                    elif Output=='Å' :
                        process=calculating*(10**8)
                    elif Output=='inch' :
                        process=calculating/2.54
                    elif Output=='ft':
                        process=calculating/2.54/12
                    elif Output=='yd':
                        process=calculating/2.54/36
                    elif Output=='mi' :
                        process=calculating/160934.4
                    elif Output=='cm':
                        process=calculating
            
            
            
            
            
                #########Diện tích#########
                if Input=='km2':
                    Input='m2'
                    calculating=calculating*(10**6)
                if Input=='ha':
                    Input='m2'
                    calculating=calculating*(10**4)
                if Input=='a':
                    Input='m2'
                    calculating=calculating*(10**2)
                if Input=='cm2':
                    Input='m2'
                    calculating=calculating/(10**4)
                if Input=='ft2':
                    Input='m2'
                    calculating=calculating/10.7639104
                if Input=='acre':
                    Input='m2'
                    calculating=calculating*4046.8564224
                if Input=='m2':
                    if Output=='km2':
                        process=calculating/(10**6)
                    elif Output=='ha':
                        process=calculating/(10**4)
                    elif Output=='a':
                        process=calculating/(100)
                    elif Output=='cm2':
                        process=calculating*(10**4)
                    elif Output=='ft2':
                        process=calculating*10.7639104
                    elif Output=='acre':
                        process=calculating*(1/4046.8564224)
                    elif Output=='m2':
                        process=calculating
            
            
            
            
            
            
            
            
            
                #########Thể tích#########
                if Input=='m3':
                    Input='l'
                    calculating=calculating*(10**3)
                if Input=='ml' or Input=='cm3':
                    Input='l'
                    calculating=calculating/(10**3)
                if Input=='mm3':
                    Input='l'
                    calculating=calculating*(10**6)
                if Input=='bushel (US)':
                    Input='l'
                    calculating=calculating*35.23907016688 
                if Input=='bushel (UK)':
                    Input='l'
                    calculating=calculating*36.36872
                if Input=='gal (US)':
                    Input='l'
                    calculating=calculating*3.785411784
                if Input=='gal (UK)':
                    Input='l'
                    calculating=calculating*4.54609
                if Input=='ft3':
                    Input='l'
                    calculating=calculating*28.316846592
                if Input=='l':
                    if Output=='ml' or Output=='cm3':
                        process=calculating*1000
                    elif Output=='m3':
                        process=calculating/1000
                    elif Output=='mm3':
                        process=calculating*(10**3)
                    elif Output=='bushel (US)':
                        process=calculating/35.23907016688 
                    elif Output=='bushel (UK)':
                        process=calculating/36.36872
                    elif Output=='gal (US)':
                        process=calculating/3.785411784
                    elif Output=='gal (UK)':
                        process=calculating/4.54609
                    elif Output=='ft3':
                        process=calculating/28.316846592
                    elif Output=='l':
                        process=calculating
            
            







                #########Thể tích#########
                if Input=='bar':
                    Input='Pa'
                    calculating=calculating*(10**5)
                if Input=='at':
                    Input='Pa'
                    calculating=calculating*98066.5
                if Input=='atm':
                    Input='Pa'
                    calculating=calculating*101325
                if Input=='Torr':
                    Input='Pa'
                    calculating=calculating/(760/101325)
                if Input=='lbf/in2':
                    Input='Pa'
                    calculating=calculating/((0.0254**2)/(0.45359237*9.80665))
                if Input=='mmHg':
                    Input='Pa'
                    calculating=calculating/133.322387415 
                if Input=='Pa':
                    if Output=='bar':
                        process=calculating/(10**5)
                    elif Output=='at':
                        process=calculating/98066.5
                    elif Output=='atm':
                        process=calculating/101325
                    elif Output=='Torr':
                        process=calculating*(760/101325)
                    elif Output=='lbf/in2':
                        process=calculating*((0.0254**2)/(0.45359237*9.80665))
                    elif Output=='mmHg':
                        process=calculating*133.322387415 
                    elif Output=='Pa':
                        process=calculating
            
            
            
            #########Vận tốc#########
                if Input=='ft/s':
                    Input='m/s'
                    calculating=calculating*0.3048
                if Input=='m/s':
                    Input='km/h'
                    calculating=calculating*3.6
                if Input=='mph':
                    Input='km/h'
                    calculating=calculating*1.609344
                if Input=='kn (kt)':
                    Input='km/h'
                    calculating=calculating*1.852
                if Input=='M':
                    Input='km/h'
                    calculating=calculating*1234.8
                if Input=='km/h':
                    if Output=='m/s':
                        process=calculating/3.6
                    elif Output=='mph':
                        process=calculating/1.609344
                    elif Output=='ft/s':
                        process=calculating
                    elif Output=='kn (kt)':
                        process=calculating/1.852
                    elif Output=='M':
                        process=calculating/1234.8
                    elif Output=='km/h':
                        process=calculating
                    
                    
                    
                    
                    
                #########Thời gian#########
                if Input=='giây':
                    Input='ngày'
                    calculating=calculating/24/(60**2)
                if Input=='phút':
                    Input='ngày'
                    calculating=calculating/24/60
                if Input=='giờ':
                    Input='ngày'
                    calculating=calculating/24
                if Input=='tuần':
                    Input='ngày'
                    calculating=calculating*7
                if Input=='tháng':
                    Input='ngày'
                    calculating=calculating*(365/12)
                if Input=='quý':
                    Input='ngày'
                    calculating=calculating*(365/12)*3
                if Input=='năm':
                    Input='ngày'
                    calculating=calculating*365
                if Input=='thập kỷ':
                    Input='ngày'
                    calculating=calculating*365*10
                if Input=='thế kỷ':
                    Input='ngày'
                    calculating=calculating*365*100
                if Input=='thiên niên kỷ':
                    Input='ngày'
                    calculating=calculating*365*1000
                if Input=='ngày':
                    if Output=='giây':
                        process=calculating*24*(60**2)
                    elif Output=='phút':
                        process=calculating*24*60
                    elif Output=='giờ':
                        process=calculating*24
                    elif Output=='tuần':
                        process=calculating/7
                    elif Output=='tháng':
                        process=calculating/(365/12)
                    elif Output=='quý':
                        process=calculating/(365/12)/3
                    elif Output=='năm':
                        process=calculating/365
                    elif Output=='thập kỷ':
                        process=calculating/365/10
                    elif Output=='thế kỷ':
                        process=calculating/365/100
                    elif Output=='thiên niên kỷ':
                        process=calculating/365/1000
                    elif Output=='ngày':
                        process=calculating
            
            
            
            
            
            
            
            
            #########Năng lượng#########
                if Input=='kJ':
                    Input='J'
                    calculating=calculating*1000
                if Input=='cal':
                    Input='J'
                    calculating=calculating*4.184
                if Input=='kcal':
                    Input='J'
                    calculating=calculating*4184
                if Input=='kWh':
                    Input='J'
                    calculating=calculating*3600000
                if Input=='Btu':
                    Input='J'
                    calculating=calculating*1055.05585262
                if Input=='eV':
                    Input='J'
                    calculating=calculating*(1.602176634/(10**19))
                if Input=='MeV':
                    Input='J'
                    calculating=(calculating*(1.602176634/(10**19)))*(10**6)
                if Input=='J':
                    if Output=='kJ':
                        process=calculating/1000
                    elif Output=='cal':
                        process=calculating/4.184
                    elif Output=='kcal':
                        process=calculating/4184
                    elif Output=='Btu':
                        process=calculating/1055.05585262
                    elif Output=='kWh':
                        process=calculating/3600000
                    elif Output=='eV':
                        process=calculating/(1.602176634/(10**19))
                    elif Output=='MeV':
                        process=(calculating/(1.602176634/(10**19)))/(10**6)
                    elif Output=='J':
                        process=calculating
            
            
            
            
            
            
            
            
                #########Công suất#########
                if Input=='kW':
                    Input='W'
                    calculating=calculating*1000
                if Input=='MW':
                    Input='W'
                    calculating=calculating*(10**6)
                if Input=='hp':
                    Input='W'
                    calculating=calculating*745.6998715822702
                if Input=='Btu/s':
                    Input='W'
                    calculating=calculating*1055.05585262
                if Input=='cal/h':
                    Input='W'
                    calculating=calculating*(4.184/3600)
                if Input=='dBm':
                    Input='W'
                    calculating=(10**(calculating/10))/1000
                if Input=='W':
                    if Output=='kW':
                        process=calculating/1000
                    elif Output=='MW':
                        process=calculating/(10**6)
                    elif Output=='hp':
                        process=calculating/745.6998715822702
                    elif Output=='Btu/s':
                        process=calculating/1055.05585262
                    elif Output=='cal/h':
                        process=calculating/(4.184/3600)
                    elif Output=='dBm':
                        process=10*math.log10(1000*calculating)
                    elif Output=='W':
                        process=calculating
                    






                #########Góc#########
                if Input=='rad':
                    Input='°'
                    calculating=calculating/(math.pi/180)
                if Input=='^g':
                    Input='°'
                    calculating=calculating/(10/9)
                if Input=="'":
                    Input='°'
                    calculating=calculating/(60)
                if Input=='"':
                    Input='°'
                    calculating=calculating/(3600)
                if Input=='°':
                    if Output=='rad':
                        process=calculating*(math.pi/180)
                    elif Output=='^g':
                        process=calculating*(10/9)
                    elif Output=="'":
                        process=calculating*60
                    elif Output=='"':
                        process=calculating*3600
                    elif Output=='°':
                        process=calculating




                #########Góc#########
                if Input=='b':
                    Input='B'
                    calculating=calculating/8
                if Input=='kB':
                    Input='B'
                    calculating=calculating*(10**3)
                if Input=='MB':
                    Input='B'
                    calculating=calculating*(10**6)
                if Input=='GB':
                    Input='B'
                    calculating=calculating*(10**9)
                if Input=='TB':
                    Input='B'
                    calculating=calculating*(10**12)
                if Input=='PB':
                    Input='B'
                    calculating=calculating*(10**15)   
                if Input=='B':
                    if Output=='b':
                        process=calculating*8
                    elif Output=='kB':
                        process=calculating/(10**3)
                    elif Output=='MB':
                        process=calculating/(10**6)
                    elif Output=='GB':
                        process=calculating/(10**9)
                    elif Output=='TB':
                        process=calculating/(10**12)
                    elif Output=='PB':
                        process=calculating/(10**15)
                    elif Output=='B':
                        process=calculating
                # re_process=round(process,3)
                round_process()
                comma_selected()
                list_box.insert(1,f'{tb.get()} {re_Input} = {process} {Output}')
                list_box.activate(END)
            
                list_box.config(xscrollcommand=scrollbar_2.set,yscrollcommand=scrollbar_1.set)
                scrollbar_1.config(command=list_box.yview)
                scrollbar_2.config(command=list_box.xview)
                return lbl_3.configure(text=process+" "+Output)
                
            except ValueError:
                messagebox.showerror('Lỗi','Vui lòng nhập đúng kiểu giá trị số thực !')
            except UnboundLocalError:
                messagebox.showerror('Lỗi','Kiểu chuyển đổi không hợp lệ hoặc chưa được cập nhật')








        ########################GUI##########################    
        #label
        lb=Label(root,text=f'{username} ơi bạn cần mình đổi cái gì nè ?',font=(basic_font,25,'bold'),fg='#f40f0f',bg=basic_colour)
        lb.place(x=50,y=230)

        lbl_2=Label(root, text=f'Đáp án của bạn nè, {username} ơi: ',font=(basic_font,24,'bold'),bg=basic_colour)
        lbl_2.place(x=50,y=440)
        lbl_3=Label(root,text='',font=(basic_font,25),bg=basic_colour)
        lbl_3.place(x=200,y=500)

        #Button
        btn_1=Button(root,text='Khối lượng',font=(basic_font,18),fg='#1E1C0D',borderwidth=5,cursor='target',command=kl)
        btn_2=Button(root,text='Nhiệt độ',font=(basic_font,18),fg='#1E1C0D',borderwidth=5,cursor='target',command=nđ)
        btn_3=Button(root,text='Độ dài',font=(basic_font,18),fg='#1E1C0D',borderwidth=5,cursor='target',command=đd)
        btn_4=Button(root,text='Diện tích',font=(basic_font,18),fg='#1E1C0D',borderwidth=5,cursor='target',command=dt)
        btn_5=Button(root,text='Thể tích',font=(basic_font,18),fg='#1E1C0D',borderwidth=5,cursor='target',command=tht)
        btn_6=Button(root,text='Áp suất',font=(basic_font,18),fg='#1E1C0D',borderwidth=5,cursor='target',command=ap)
        btn_7=Button(root,text='Vận tốc',font=(basic_font,18),fg='#1E1C0D',borderwidth=5,cursor='target',command=vt)
        btn_8=Button(root,text='Thời gian',font=(basic_font,18),fg='#1E1C0D',borderwidth=5,cursor='target',command=tg)
        btn_9=Button(root,text='Năng lượng',font=(basic_font,18),fg='#1E1C0D',borderwidth=5,cursor='target',command=nl)
        btn_10=Button(root,text='Công suất',font=(basic_font,18),fg='#1E1C0D',borderwidth=5,cursor='target',command=cs)
        btn_11=Button(root,text='Góc',font=(basic_font,18),fg='#1E1C0D',borderwidth=5,cursor='target',command=g)
        btn_12=Button(root,text='Múi giờ',font=(basic_font,18),fg='#1E1C0D',borderwidth=5,cursor='target',command=mg)
        btn_13=Button(root,text='Dữ liệu',font=(basic_font,18),fg='#1E1C0D',borderwidth=5,cursor='target',command=dl)
        btn_14=Button(root,text='Tiền tệ',font=(basic_font,18),fg='#1E1C0D',borderwidth=5,cursor='target',command=tt)
        btn_15=Button(root,text='Cài đặt',font=(basic_font,18),fg='#1E1C0D',borderwidth=5,cursor='target',command=cđ)
        btn_n=Button(root,text='Chuyển đổi',font=(basic_font,20,'bold'),fg='#1E1C0D',borderwidth=5,cursor='exchange')
        btn_e=Button(root,text='<=>',font=(basic_font,20,'bold'),fg='#1E1C0D',borderwidth=5,cursor='exchange',command=ex)
        if basic_font=='Helvetica' or basic_font=='Arial':
                btn_1.configure(font=(basic_font,17))
                btn_9.configure(font=(basic_font,16))
                btn_10.configure(font=(basic_font,17))
        btn_1.place(x=45,y=10,height=50,width=120)
        btn_2.place(x=190,y=10,height=50,width=120)
        btn_3.place(x=335,y=10,height=50,width=120)
        btn_4.place(x=480,y=10,height=50,width=120)
        btn_5.place(x=625,y=10,height=50,width=120)
        btn_6.place(x=45,y=80,height=50,width=120)
        btn_7.place(x=190,y=80,height=50,width=120)
        btn_8.place(x=335,y=80,height=50,width=120)
        btn_9.place(x=480,y=80,height=50,width=120)
        btn_10.place(x=625,y=80,height=50,width=120)
        btn_11.place(x=45,y=150,height=50,width=120)
        btn_12.place(x=190,y=150,height=50,width=120)
        btn_13.place(x=335,y=150,height=50,width=120)
        btn_14.place(x=480,y=150,height=50,width=120)
        btn_15.place(x=625,y=150,height=50,width=120)
        btn_n.place(x=280,y=360,height=50,width=200)
        btn_e.place(x=725,y=330,height=50,width=50)


        #Textbox
        tb=Entry(root,font=(basic_font,20),borderwidth=5)
        tb.place(x=280,y=290,height=50,width=200)
        #Listbox
        list_box= Listbox(root,height=5,width=20,font=(basic_font,15),activestyle='none')
        list_box.place(x=45,y=290)
        list_box.insert(0,'Bạn vừa mới đổi:')
        scrollbar_1 = Scrollbar(root)
        scrollbar_1.place(x=249,y=290,height=120)
        scrollbar_2= Scrollbar(root,orient=HORIZONTAL)
        scrollbar_2.place(x=42,y=409,width=225)


        #Combobox:
        dv_1=tkinter.StringVar()
        cb_1= ttk.Combobox(root, width=13,textvariable=dv_1,font=(basic_font,20))
        dv_2=tkinter.StringVar()
        cb_2= ttk.Combobox(root, width=13,textvariable=dv_2,font=(basic_font,20))

        cb_1.place(x=500,y=290,height=50)
        cb_2.place(x=500,y=360,height=50)
        # cb_2.place(x=670,y=310,height=50)
        #Checkbox
        # Var1=IntVar()
        # Chb_1=Checkbutton(root,text='Thời gian hiện tại',font=(basic_font,10),variable=Var1,bg=basic_colour,activebackground=basic_colour)
        # Chb_2=Checkbutton(root,text='Năm không nhuận',font=(basic_font,10),variable=Var1,bg=basic_colour,activebackground=basic_colour)
        # Chb_2.grid(row=1,column=0)


        root.mainloop()
    if len(username)>15 and password=='minhtueit123':
        messagebox.showerror('Lỗi đăng nhập','Tên đăng nhập phải từ 1 đến 14 ký tự bao gồm dấu cách')
    if password != 'minhtueit123':
        messagebox.showerror ('Lỗi đăng nhập','Sai mật khẩu !\nMật khẩu là 1 chuỗi được Minh Tuệ cấp')
login=Tk()
login.title('Đăng nhập')
login.geometry('400x200+500+250')
login.resizable(0,0)
login.iconbitmap('img/icon.ico')
name_label=Label(login,text='Tên hiển thị:',font=('Times',15,'bold'))
name_label.place(x=20,y=20)


name_typing=Entry(login,font=('Times',15))
name_typing.place(x=150,y=22)

password_label=Label(login,text='Mật khẩu:',font=('Times',15,'bold'))
password_label.place(x=20,y=60)
password_typing=Entry(login,font=('Times',15),show='*')
password_typing.place(x=150,y=62)


save=IntVar()
save_checked=Checkbutton(login,text='Nhớ mật khẩu',font=('Times',12),variable=save,onvalue=1,offvalue=0)
save_checked.place(x=145,y=92)

login_btn=Button(login,text='Đăng nhập',font=('Times',15,'bold'),padx=10,bd=5,relief=RIDGE,overrelief=RAISED,command=open_application)
login_btn.place(x=150,y=130)

with open('login.txt','r',encoding='utf8') as r_login:
    get_info=r_login.readlines()
for i in get_info:
    if 'User' in i:
        fill_user=i[6:None].replace('\n','')
    if 'Password' in i:
        fill_password=i[10:None].replace('\n','')
    if 'Savepass' in i:
        auto_fill_password= i[10:None]
name_typing.insert(0,fill_user)
if auto_fill_password=='1':
    save_checked.select()
if auto_fill_password=='0':
    save_checked.deselect()
if save.get()==1:
    password_typing.insert(0,fill_password)



login.bind('<Return>',open_application)
login.mainloop()








#13/08/2021: Ver 1.0: main app
#15/08/2021: Ver 1.1: add độ dài
#17/08/2021: Ver 1.2: add inch,feet,yard,mile
#18/08/2021: Ver 1.3: add Diện tích
#19/08/2021: Ver 1.4: Update GUI
#20/08/2021: Ver 1.5: add Thể tích, áp suất, vận tốc , optimizing source code
#21/08/2021: Ver 1.6: add Năng lượng, công suất , thời gian , góc , dữ liệu
#22/08/2021: Ver 1.7: add Timezone, Currency
#23/08/2021: Ver 1.8: FIX GUI , thêm nút convert
#24/08/2021: Ver 1.9: add Setting
#25/08/2021: Ver 2.0: add save_setting
#26/08/2021: Ver 2.1: add history box
#27/08/2021: Ver 2.2: Complete edition