# Import this to use time.sleep() method 
import time

# This is must do step
# To install this write pip install win10toast then press enter without this you won't be able popup your notificaton
from win10toast import ToastNotifier

if __name__ == "__main__":
    # This loop is a infinite loop Which keps it running forver 
    while True:
        # ToastNotifier() initializes the module 
        # Here we initialize ToastNotifier() with the word notify its upto you you can give it any name 
        notify = ToastNotifier()
        
        # We did notify = ToastNotifier() so what we did here is notify.show_toast instead of ToastNotifier().show_toast()
        # It Contains notify.show_toast("Title Of The Notification", "Body Of The Notification", duration = time in seconds you want to show 
        #                               your notification in ex given below I did duration = 20, icon_path = icon file path which you want to show)
        notify.show_toast("Please Drink Water", "The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.", duration=25, icon_path="watericon.ico" )
        
        # time.sleep() makes our notification pop in every 60 minutes
        time.sleep(60 * 60)
