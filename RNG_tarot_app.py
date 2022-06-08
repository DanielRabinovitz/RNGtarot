import tkinter
import RNGtarot
import pandas

if __name__ == '__main__':
    #class instance with the word list and current card set
    tarot = RNGtarot.Tarot()
    tarot.new_cards()

    window = tkinter.Tk(className = 'RNG tarot')
    window.geometry('900x600')
    window.configure(bg='dark grey')

    #text for card displays
    past_text = 'Past...\n' + tarot.cards['Past']
    present_text = 'Present...\n' + tarot.cards['Present']
    future_text = 'Future...\n' + tarot.cards['Future']

    #past, present, future are the 3 cards
    past = tkinter.Canvas(window, width = 210, height = 330)
    present = tkinter.Canvas(window, width = 210, height = 330)
    future = tkinter.Canvas(window, width = 210, height = 330)
    #position them
    past.place(relx=.2, rely=.4, anchor=tkinter.CENTER)
    present.place(relx=.5, rely=.4, anchor=tkinter.CENTER)
    future.place(relx=.8, rely=.4, anchor=tkinter.CENTER)
    #text inside cards + card appearances
    past_label = tkinter.Label(past, bd=2, width = 8, height = 5, bg='pink', text = past_text)
    past_label.config(font='Papyrus 30', borderwidth=2, relief=tkinter.SOLID)
    past_label.pack()
    present_label = tkinter.Label(present, bd=2, width = 8, height = 5, bg='thistle', text = present_text)
    present_label.config(font='Papyrus 30', borderwidth=2, relief=tkinter.SOLID)
    present_label.pack()
    future_label = tkinter.Label(future, bd=2, width = 8, height = 5, bg='light sky blue', text = future_text)
    future_label.config(font='Papyrus 30', borderwidth=2, relief=tkinter.SOLID)
    future_label.pack()
    
    def update_cards():
        tarot.new_cards()
        print(tarot.cards)
        past_text = 'Past...\n' + tarot.cards['Past']
        present_text = 'Present...\n' + tarot.cards['Present']
        future_text = 'Future...\n' + tarot.cards['Future']
        past_label.config(text = past_text)
        present_label.config(text = present_text)
        future_label.config(text = future_text)

    draw_hand_button = tkinter.Button(
        window, 
        text ='Draw New Hand', 
        width = '15', 
        height='1',
        command = update_cards,
        font = 'Papyrus 15',
        borderwidth=2, relief=tkinter.SOLID
    )

    draw_hand_button.place(relx=.5, rely=.8, anchor=tkinter.CENTER)
    window.mainloop()

