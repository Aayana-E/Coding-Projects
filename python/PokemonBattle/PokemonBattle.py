import tkinter as tk
from PIL import Image, ImageTk #image library
import random
import io #input output tools
import json #Json is a big dictionary
import urllib.request

random.seed(57)

#Tkinter
Screen = tk.Tk()#Screen
Screen.geometry("700x700")
Screen.title("Pokemon Battle By Aayana")
Screen.configure(bg="black")

#Making requests to fetch pokemon data from API
def get_pokemon(id_or_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{id_or_name}"
    #try except - similar to if then statement
    #try except if it cant run try runs except so code keeps running
    try:
        with urllib.request.urlopen(url) as response:
            if response.status != 200: #api request fails
                return None
            data = json.loads(response.read().decode())#reads request and save to variable
            # print(data)
    except Exception as e:
        print(e)
    
    #Get name
    name = data["name"].title()#access a value from a dictionary with a key

    #image
    img_url = data['sprites']['front_default']
    image_data = urllib.request.urlopen(img_url).read()#download img data
    #pillow to open image and resize
    image = Image.open(io.BytesIO(image_data)).resize((200,200))


    #moves
    AllMoves = data['moves']
    # print(AllMoves)
    moveNames = []
    #for =definite/repeat
    #while = repeat until, infinite
    for move in AllMoves:
        moveNames.append(move['move']['name'])
    random.shuffle(moveNames)
    if len(moveNames) >= 4:
        moveNames = moveNames[:4]#slices it to length 4
    else:
        pass
    print(moveNames)


    # print(name)
    #return - has function give you data/objects after it runs
    return {
        "name":name,
        'image': ImageTk.PhotoImage(image), #convert to Tkinter image format
        'moves': moveNames
    }

p1_num = random.randint(1,1025)
p1 = get_pokemon(p1_num)
#frame for pokemon 1
p1_frame = tk.Frame(Screen,bg="black")
p1_frame.pack(side="left", padx=50)


p1_info = tk.StringVar() #changes variable into string
p1_info.set(f"{p1['name']}")
tk.Label(p1_frame, textvariable=p1_info, bg="black", fg="purple", font=("Arial", 14)).pack(pady=(10))#top and bottom

imageLabel1 =  tk.Label(p1_frame, bg="black")
imageLabel1.config(image=p1['image'])
imageLabel1.pack(padx=20)#padx = space on left and right

#p2
p2_num = random.randint(1,1025)
while p1_num == p2_num:
    p2_num = random.randint(1,1025)
p2 = get_pokemon(p2_num)
#frame for pokemon 1
p2_frame = tk.Frame(Screen, bg="black")
p2_frame.pack(side="right", padx=50)


p2_info = tk.StringVar() #changes variable into string
p2_info.set(f"{p2['name']}")
tk.Label(p2_frame, textvariable=p2_info, bg="black", fg="purple",font=("Arial", 14)).pack(pady=(10))#top and bottom

imageLabel2 =  tk.Label(p2_frame, bg="black")
imageLabel2.config(image=p2['image'])
imageLabel2.pack(padx=20)#padx = space on left and right

def ShowMove(p1):
    #p1 moves
    moveButton1 = []
    MoveLen1 = len(p1['moves'])
    for i in range(MoveLen1):
        BTN = tk.Button(p1_frame, text=p1['moves'][i], width= 10, height=3 , fg="red", bg="white", font=("Arial", 10))
        BTN.pack(pady=5)
        moveButton1.append(BTN)





#Labels
TitleLabel = tk.Label(Screen, text="Pokemon Battle By Aayana", font=("Arial", 30), fg="Red", bg="black")
#grid, place, pack
TitleLabel.place(x = 100, y = 50)

#vs label
VsLabel = tk.Label(Screen, text="VS", font=("Arial",20), fg="Red", bg="black",anchor="w")
VsLabel.place(relx= 0.45 , rely=0.5)

ShowMove(p1)#Displays both users moves

#keep at bottom
Screen.mainloop()#refreses screen infinite
