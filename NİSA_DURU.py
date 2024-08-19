import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import json
import os
import pygame

pygame.mixer.init()

PROFILE_FILE = "profiles.json"

def load_profiles():
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "r") as file:
            return json.load(file)
    return {}

def save_profiles(profiles):
    with open(PROFILE_FILE, "w") as file:
        json.dump(profiles, file)

def create_profile(name):
    profiles = load_profiles()
    if name in profiles:
        messagebox.showerror("Hata", "Bu isimle bir profil zaten var.")
        return False
    profiles[name] = {"wins": 0, "losses": 0, "ties": 0}
    save_profiles(profiles)
    return True

def update_profile(name, result):
    profiles = load_profiles()
    if name not in profiles:
        return
    if result == "win":
        profiles[name]["wins"] += 1
    elif result == "loss":
        profiles[name]["losses"] += 1
    elif result == "tie":
        profiles[name]["ties"] += 1
    save_profiles(profiles)

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Taş Kağıt Makas")
        self.player_profile = None
        self.opponent_profile = None
        self.game_mode = None
        self.player_wins = 0
        self.opponent_wins = 0
        self.difficulty = "Kolay"

        self.root.configure(bg="lightblue")
        self.button_style = {"font": ("Arial", 12), "bg": "white", "fg": "black", "relief": "raised"}

        self.load_images()
        self.load_sounds()

        self.main_menu()

    def load_images(self):
        self.rock_image = ImageTk.PhotoImage(Image.open("tas.png").resize((100, 100)))
        self.paper_image = ImageTk.PhotoImage(Image.open("kagit.png").resize((100, 100)))
        self.scissors_image = ImageTk.PhotoImage(Image.open("makas.png").resize((100, 100)))

    def load_sounds(self):
        self.win_sound = pygame.mixer.Sound("win_sound.wav")
        self.lose_sound = pygame.mixer.Sound("lose_sound.wav")
        self.tie_sound = pygame.mixer.Sound("tie_sound.wav")


    def main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Taş Kağıt Makas", font=("Arial", 20), bg="lightblue").pack(pady=20)
        tk.Button(self.root, text="Tek Kişilik Oyna", command=self.single_player_menu, **self.button_style).pack(pady=10)
        tk.Button(self.root, text="Çift Kişilik Oyna", command=self.two_player_menu, **self.button_style).pack(pady=10)
        tk.Button(self.root, text="Eğitim", command=self.show_tutorial, **self.button_style).pack(pady=10)
        tk.Button(self.root, text="Skor Tablosu", command=self.display_high_scores, **self.button_style).pack(pady=10)
        tk.Button(self.root, text="Çıkış", command=self.root.quit, **self.button_style).pack(pady=10)

    def show_tutorial(self):
        self.clear_window()
        tutorial_text = (
            "Taş Kağıt Makas Oyunu:\n\n"
            "1. Oyuncu, taş, kağıt veya makas arasında bir seçim yapar.\n"
            "2. Bilgisayar (veya diğer oyuncu) da bir seçim yapar.\n"
            "3. Kazanan şu kurallara göre belirlenir:\n"
            "   - Taş, makası yener.\n"
            "   - Kağıt, taşı yener.\n"
            "   - Makas, kağıdı yener.\n"
            "4. İki galibiyete ulaşan oyuncu oyunu kazanır.\n"
            "\nEğlenin ve bol şans!"
        )
        tk.Label(self.root, text="Oyun Kuralları", font=("Arial", 20), bg="lightblue").pack(pady=10)
        tk.Label(self.root, text=tutorial_text, font=("Arial", 14), bg="lightblue", justify=tk.LEFT).pack(pady=10)
        tk.Button(self.root, text="Geri", command=self.main_menu, **self.button_style).pack(pady=10)

    def display_high_scores(self):
        self.clear_window()
        profiles = load_profiles()
        tk.Label(self.root, text="Skor Tablosu", font=("Arial", 20), bg="lightblue").pack(pady=10)
        for name, stats in profiles.items():
            tk.Label(self.root, text=f"{name} - Kazanma: {stats['wins']}, Kaybetme: {stats['losses']}, Beraberlik: {stats['ties']}",
                     font=("Arial", 14), bg="lightblue").pack(pady=5)
        tk.Button(self.root, text="Geri", command=self.main_menu, **self.button_style).pack(pady=10)

    def single_player_menu(self):
        self.game_mode = "single"
        self.select_difficulty()

    def select_difficulty(self):
        self.clear_window()
        tk.Label(self.root, text="Zorluk Seviyesi Seçin", font=("Arial", 16), bg="lightblue").pack(pady=10)
        tk.Button(self.root, text="Kolay", command=lambda: self.set_difficulty("Kolay"), **self.button_style).pack(pady=5)
        tk.Button(self.root, text="Orta", command=lambda: self.set_difficulty("Orta"), **self.button_style).pack(pady=5)
        tk.Button(self.root, text="Zor", command=lambda: self.set_difficulty("Zor"), **self.button_style).pack(pady=5)
        tk.Button(self.root, text="Geri", command=self.main_menu, **self.button_style).pack(pady=10)

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        self.select_profile()

    def two_player_menu(self):
        self.game_mode = "two_player"
        self.select_profile(player_num=1)

    def select_profile(self, player_num=1):
        self.clear_window()
        tk.Label(self.root, text=f"{player_num}. Oyuncu Profil Seçimi", font=("Arial", 16), bg="lightblue").pack(pady=10)
        profiles = load_profiles()
        profile_names = list(profiles.keys())

        for name in profile_names:
            tk.Button(self.root, text=name, command=lambda n=name: self.set_profile(n, player_num), **self.button_style).pack(pady=5)

        tk.Button(self.root, text="Yeni Profil Oluştur", command=lambda: self.create_new_profile(player_num), **self.button_style).pack(pady=10)
        tk.Button(self.root, text="Ana Menü", command=self.main_menu, **self.button_style).pack(pady=10)

    def create_new_profile(self, player_num):
        self.clear_window()
        tk.Label(self.root, text="Profil İsmi Girin", font=("Arial", 16), bg="lightblue").pack(pady=10)
        name_entry = tk.Entry(self.root)
        name_entry.pack(pady=10)
        tk.Button(self.root, text="Oluştur", command=lambda: self.confirm_create_profile(name_entry.get(), player_num), **self.button_style).pack(pady=10)
        tk.Button(self.root, text="Geri", command=lambda: self.select_profile(player_num), **self.button_style).pack(pady=10)

    def confirm_create_profile(self, name, player_num):
        if create_profile(name):
            self.set_profile(name, player_num)

    def set_profile(self, name, player_num):
        if player_num == 1:
            self.player_profile = name
            if self.game_mode == "single":
                self.start_game()
            else:
                self.select_profile(player_num=2)
        elif player_num == 2:
            self.opponent_profile = name
            self.start_game()

    def start_game(self):
        self.clear_window()
        self.player_wins = 0
        self.opponent_wins = 0
        tk.Label(self.root, text="Taş Kağıt Makas!", font=("Arial", 20), bg="lightblue").pack(pady=20)

        tk.Button(self.root, image=self.rock_image, command=lambda: self.play("Taş")).pack(side=tk.LEFT, padx=20)
        tk.Button(self.root, image=self.paper_image, command=lambda: self.play("Kağıt")).pack(side=tk.LEFT, padx=20)
        tk.Button(self.root, image=self.scissors_image, command=lambda: self.play("Makas")).pack(side=tk.LEFT, padx=20)

        tk.Button(self.root, text="Ana Menü", command=self.main_menu, **self.button_style).pack(pady=10)

    def play(self, player_choice):
        computer_choice = self.get_computer_choice()

        result = self.determine_winner(player_choice, computer_choice)

        if result == "win":
            self.win_sound.play()
        elif result == "loss":
            self.lose_sound.play()
        else:
            self.tie_sound.play()

        if self.game_mode == "single":
            self.update_game_result(result, computer_choice)
        else:
            self.update_game_result(result, computer_choice, two_player=True)

        # Eğer oyunculardan biri 2 galibiyete ulaştıysa skoru sıfırlayıp yeni oyuna başlat
        if self.player_wins == 2 or self.opponent_wins == 2:
            self.ask_restart()

    def get_computer_choice(self):
        if self.difficulty == "Kolay":
            return random.choice(["Taş", "Kağıt", "Makas"])
        elif self.difficulty == "Orta":
            if random.random() < 0.7:
                return random.choice(["Taş", "Kağıt", "Makas"])
            else:
                return "Kağıt" if self.player_wins > self.opponent_wins else "Taş"
        elif self.difficulty == "Zor":
            return "Taş" if self.opponent_wins > self.player_wins else random.choice(["Kağıt", "Makas"])

    def determine_winner(self, player, computer):
        if player == computer:
            return "tie"
        elif (player == "Taş" and computer == "Makas") or \
                (player == "Kağıt" and computer == "Taş") or \
                (player == "Makas" and computer == "Kağıt"):
            return "win"
        else:
            return "loss"

    def update_game_result(self, result, computer_choice, two_player=False):
        if two_player:
            opponent_choice = random.choice(["Taş", "Kağıt", "Makas"])
            opponent_result = self.determine_winner(opponent_choice, computer_choice)
            if opponent_result == "win":
                self.opponent_wins += 1
            update_profile(self.opponent_profile, opponent_result)
            messagebox.showinfo("Sonuç",
                                f"{self.opponent_profile} seçimi: {opponent_choice}\nSonuç: {opponent_result.capitalize()}")

        if result == "win":
            self.player_wins += 1
        elif result == "loss":
            self.opponent_wins += 1

        update_profile(self.player_profile, result)
        messagebox.showinfo("Sonuç", f"Bilgisayar seçimi: {computer_choice}\nSonuç: {result.capitalize()}")

        self.display_score()

    def ask_restart(self):
        # Skorları sıfırlama ve yeni oyuna başlama
        self.player_wins = 0
        self.opponent_wins = 0
        answer = messagebox.askyesno("Oyun Bitti", "Bir oyuncu iki galibiyet aldı. Yeni oyuna başlamak ister misiniz?")
        if answer:
            self.start_game()
        else:
            self.main_menu()

    def display_score(self):
        profiles = load_profiles()
        player_stats = profiles[self.player_profile]
        stats_text = f"Kazanma: {player_stats['wins']}  Kaybetme: {player_stats['losses']}  Beraberlik: {player_stats['ties']}"

        self.clear_window()
        tk.Label(self.root, text="Skor Tablosu", font=("Arial", 18), bg="lightblue").pack(pady=10)
        tk.Label(self.root,
                 text=f"Bu Oyun:\n{self.player_profile} Kazandı: {self.player_wins}\n{self.opponent_profile if self.opponent_profile else 'Bilgisayar'} Kazandı: {self.opponent_wins}",
                 font=("Arial", 16), bg="lightblue").pack(pady=10)
        tk.Label(self.root, text="Toplam Skorlar", font=("Arial", 16), bg="lightblue").pack(pady=10)
        tk.Label(self.root, text=stats_text, font=("Arial", 14), bg="lightblue").pack(pady=10)

        tk.Button(self.root, text="Tekrar Oyna", command=self.start_game, **self.button_style).pack(pady=10)
        tk.Button(self.root, text="Ana Menü", command=self.main_menu, **self.button_style).pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
        root = tk.Tk()
        game = RockPaperScissorsGame(root)
        root.mainloop()