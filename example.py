import customtkinter as ct
from stk_widgets import ToolTip, OptionList, PasswordEntry, Spinner, ArcSpinner, VerticalTab, ClickableLabel, \
    CircleButton,  stkmessagebox, StkFileDialog, layouts,STk, screenshot_frame, STkMenuBar
from stk_widgets.window.layouts import DraggableWidget

#STk is a rudimentary attemt at a custom window, it is very buggy so only use if you can fix or are okay with it
# it's preferable to use regular tk, ttk or ctk
root = STk()
root.set_title("Test Application")
root.geometry("500x500")

#add the default buttons for window control
root.add_default_winbtns()
entry = PasswordEntry(root.set_titlebar.right_container)
x =ct.CTkSegmentedButton(root.set_titlebar.right_container, values=["system", "light", "dark"], command=lambda e:   ct.set_appearance_mode(e))

#add widgets to title bar
root.add_widget_to_titlebar(entry)
root.add_widget_to_titlebar(x)


#menubar doesn't work with stk
#menubar = STkMenuBar(root)
#
#menubar.add_menu("File", {
#    "New": lambda: print("New File"),
#    "Open": lambda: print("Open File"),
#    "Exit": root.destroy
#})
#
#menubar.add_menu("Edit", {
#    "Cut": lambda: print("Cut"),
#    "Copy": lambda: print("Copy"),
#    "Paste": lambda: print("Paste")
#})
#
#menubar.add_menu("Help", {
#    "About": lambda: print("About clicked")
#})


# vertical tabview
tabview = VerticalTab(root, width=600, height=400,)
tabview.pack(fill="both", expand=True)

button = ct.CTkButton(root, text="take screenshot",
                      command=lambda: screenshot_frame(root, "screenshots"))
button.pack()
ToolTip(button, "hey, i can take screenshots.")

# Add tabs
tab1 = tabview.add_tab("Home", button_style="circular")#button styles [circular, regular]
ct.CTkLabel(tab1, text="This is the Home tab").pack(pady=20)

tab2 = tabview.add_tab("Settings")
ct.CTkLabel(tab2, text="This is the Settings tab").pack(pady=20)

tab3 = tabview.add_tab("About")
ct.CTkLabel(tab3, text="This is the About tab").pack(pady=20)



frame = ct.CTkFrame(tab1)
frame.pack(padx=20, pady=20, fill="both", expand=True)

#appears on left click and displays a group of options
options = OptionList(frame)
# adds a label to the widget, also takes in a font argument
options.add_label("File Options")

#add buttons, buttons also take in argument like hover and color
options.add_button("Open", command=lambda: print("open clicked"))
options.add_button("Delete", color="red", command=lambda: print("delete clicked"))
options.add_button("Restore", command=lambda: print("restore clicked"))
lab = ct.CTkLabel(tab3)
lab.pack()

# a password entry with show and hide
p = PasswordEntry(tab3, password_hide_text="hide", password_show_text="show")
p.pack()

# a circular button
CircleButton(tab2, text="Click me", command=lambda: StkFileDialog(root, "just testing")).pack(pady=20)

#a clickable label, can be used for links or anything of the sort
ClickableLabel(tab3, text="This is the About tab",
               command=lambda :stkmessagebox.showinfo("Info", "This is a messagebox")).pack(pady=20)

# loading animations
Spinner(root).pack(pady=20, expand=True, fill="both")
ArcSpinner(root).pack(pady=20, expand=True, fill="both")

btn = ct.CTkButton(tab3, text="testing layout and drag")
btn2 = ct.CTkButton(tab3,text="testing layout")
btn3 = ct.CTkButton(tab3, text="testing layout")

# arranges widgets in a list, other layouts include:
#layouts.WeightedGridLayout
#layouts.VerticalListLayout
#layouts.GridLayout
layouts.ListLayout([btn, btn2, btn3])

# makes widgets draggable
DraggableWidget(
    btn,
    constrain_to_parent=False #detemines if the widget should be constrained to its parent/master
)



root.mainloop()
