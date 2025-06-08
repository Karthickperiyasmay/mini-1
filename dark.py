import tkinter as tk


def toggle_theme():
    if root.option_get('theme', 'light') == 'light':
      
        root.tk_setPalette(background='#2e2e2e', foreground='#ffffff')
        label.config(bg='#2e2e2e', fg='#ffffff')
        theme_button.config(bg='#555555', fg='#ffffff')
        root.option_add('theme', 'dark')
        theme_button.config(text="Switch to Light Theme")
    else:
      
        root.tk_setPalette(background='#ffffff', foreground='#000000')
        label.config(bg='#ffffff', fg='#000000')
        theme_button.config(bg='#e0e0e0', fg='#000000')
        root.option_add('theme', 'light')
        theme_button.config(text="Switch to Dark Theme")

root = tk.Tk()
root.title("Theme Toggle Example")
root.geometry("400x300")


root.option_add('theme', 'light')
root.tk_setPalette(background='#ffffff', foreground='#000000')


label = tk.Label(root, text="Toggle Theme", font=('Arial', 24))
label.pack(pady=50)


theme_button = tk.Button(root, text="Switch to Dark Theme", font=('Arial', 14), command=toggle_theme)
theme_button.pack(pady=20)


root.mainloop()
