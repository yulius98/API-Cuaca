import requests
import json
import tkinter as tk
from tkinter import messagebox

url_cuaca ="https://api.openweathermap.org/data/2.5/weather?q="
#url_lokasi ="http://api.openweathermap.org/geo/1.0/direct?q="
API="ebdeae18844f69ccf09c96bae8dd2c9b"

def keluar_program():
  root.destroy()


def Tampilan_Cuaca():
  nama_kota = kota.get()
  #coor_lokasi =(url_lokasi+nama_kota+"&limit=5&appid="+API)
  #data = requests.get(coor_lokasi)
  #data_jason = data.json()
  #coor_lat = str(data_jason[0].get('lat'))
  #coor_lon = str(data_jason[0].get('lon'))
  #show_data = json.dumps(data_jason,indent=4)
  coor_cuaca = (url_cuaca+nama_kota+"&lang=id&appid="+API+"&units=metric")
  cuaca = requests.get(coor_cuaca)
  data_cuaca_json = cuaca.json()
  print(json.dumps(data_cuaca_json,indent=4))
  data_utama = data_cuaca_json['main']
  nama_lokasi = data_cuaca_json['name']
  suhu = data_utama['temp']
  suhu_max = data_utama['temp_max']
  suhu_min = data_utama['temp_min']
  tekanan = data_utama['pressure']
  ketinggian = data_utama['grnd_level']
  info_cuaca = f"Lokasi : {nama_lokasi}\nSuhu : {suhu} C\nSuhu Max : {suhu_max} C\nSuhu Min : {suhu_min} C\n Tekanan : {tekanan} hPa"
  messagebox.showinfo("Info Cuaca",info_cuaca)
  

root = tk.Tk()
root.title("Aplikasi Cuaca")
tk.Label(root,text="Masukkan Nama Kota").grid(row=1,column=0)
kota = tk.Entry(root,width=50)
kota.grid(row=1,column=1)
tk.Button(root,text="Cuaca",command=Tampilan_Cuaca).grid(row=2,column=0)
tk.Button(root,text="Keluar",command=keluar_program).grid(row=2,column=1)


root.mainloop()

