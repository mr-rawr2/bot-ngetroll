import random

def gen_pass():
    sandi = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password_leght = 10
    password_new = ""

    for i in range(password_leght):
        password_new += random.choice(sandi)

    return password_new   

sampah_organik = ['daun', 'makanan sisa', 'kotoran hewan', 'ranting,', 'cangkang telur', 'sisa sayuran', 'buah busuk', 'tulang']
sampah_anorganik = ['plastik', 'kertas', 'ban/karet', 'kaca', 'melamin', 'kaleng', 'botol plastik', 'baterai', 'kabel']



    