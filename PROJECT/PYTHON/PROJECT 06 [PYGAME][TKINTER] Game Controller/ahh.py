import tkinter as tk
from tkinter import ttk, messagebox
import random

class Hero:
    def __init__(self, name, health, attack_power, defense_power):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack_power = attack_power
        self.defense_power = defense_power

class TankGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hero Tank Battle Pro")
        
        # Daftar hero dengan stat seimbang
        self.hero_pool = [
            Hero('Sniper', 50, 90, 90),
            Hero('Fighter', 80, 35, 40),
            Hero('TeamZ', 120, 30, 80),
            Hero('ZeroHunter', 90, 70, 50),
            Hero('KruTank', 40, 30, 20),
            Hero('PenembakRunduk', 30, 70, 75),
            Hero('Captain', 150, 40, 85),
            Hero('RedBarret', 70, 60, 65),
            Hero('KamikazeDrone', 20, 200, 10)
        ]
        
        # Frame untuk pemilihan hero
        self.setup_frame = tk.Frame(root)
        self.setup_frame.pack(pady=20)
        
        tk.Label(self.setup_frame, text="Pilih Hero Anda:").pack()
        
        # ComboBox untuk memilih hero
        self.hero_choices = ttk.Combobox(
            self.setup_frame, 
            values=[hero.name for hero in self.hero_pool],
            state="readonly"
        )
        self.hero_choices.pack(pady=10)
        self.hero_choices.current(0)
        
        # Tombol mulai
        tk.Button(
            self.setup_frame, 
            text="Mulai Game", 
            command=self.start_game
        ).pack()
        
        # Variabel game (akan diinisialisasi setelah start)
        self.canvas = None
        self.player_hero = None
        self.ai_hero = None
        self.player_tank = None
        self.ai_tank = None
        self.bullets = []
        self.info_display = None
        self.health_bars = {}
    
    def start_game(self):
        # Hapus frame setup
        self.setup_frame.destroy()
        
        # Pilih hero player dan AI
        player_choice = self.hero_choices.get()
        self.player_hero = next(hero for hero in self.hero_pool if hero.name == player_choice)
        
        # Pilih AI hero random (bukan hero yang dipilih player)
        ai_options = [hero for hero in self.hero_pool if hero != self.player_hero]
        self.ai_hero = random.choice(ai_options)
        
        # Setup canvas
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='lightgreen')
        self.canvas.pack()
        
        # Inisialisasi tank
        self.player_tank = {
            'x': 100, 
            'y': 300, 
            'color': 'blue', 
            'hero': self.player_hero
        }
        
        self.ai_tank = {
            'x': 700, 
            'y': 300, 
            'color': 'red', 
            'hero': self.ai_hero
        }
        
        # Gambar arena
        self.draw_game_elements()
        
        # Info hero
        self.info_display = tk.Label(
            self.root,
            text=f"{self.player_hero.name} (Anda) vs {self.ai_hero.name} (AI)",
            font=('Arial', 12)
        )
        self.info_display.pack()
        
        # Health bars
        health_frame = tk.Frame(self.root)
        health_frame.pack(fill='x', padx=20)
        
        tk.Label(health_frame, text="Player:").pack(side='left')
        self.health_bars['player'] = tk.Label(
            health_frame, 
            text=f"{self.player_hero.health}/{self.player_hero.max_health} HP",
            fg='green'
        )
        self.health_bars['player'].pack(side='left', padx=10)
        
        tk.Label(health_frame, text="AI:").pack(side='left')
        self.health_bars['ai'] = tk.Label(
            health_frame, 
            text=f"{self.ai_hero.health}/{self.ai_hero.max_health} HP",
            fg='red'
        )
        self.health_bars['ai'].pack(side='left', padx=10)
        
        # Bind keyboard
        self.root.bind('<Key>', self.key_press)
        
        # AI behavior
        self.ai_move_counter = 0
        
        # Mulai game loop
        self.game_loop()
    
    def draw_game_elements(self):
        self.canvas.delete('all')
        
        # Gambar arena
        self.canvas.create_rectangle(0, 400, 800, 600, fill='saddlebrown', outline='')  # Tanah
        self.canvas.create_rectangle(0, 0, 800, 400, fill='lightblue', outline='')      # Langit
        
        # Gambar tank player
        self.draw_tank(self.player_tank, direction=1)
        
        # Gambar tank AI
        self.draw_tank(self.ai_tank, direction=-1)
        
        # Gambar peluru
        for bullet in self.bullets:
            self.canvas.create_oval(
                bullet['x']-5, bullet['y']-5,
                bullet['x']+5, bullet['y']+5,
                fill=bullet['color'], tags='bullet'
            )
        
        # Gambar health bar di atas tank
        self.draw_health_bar(self.player_tank)
        self.draw_health_bar(self.ai_tank)
    
    def draw_tank(self, tank, direction):
        # Body tank
        self.canvas.create_rectangle(
            tank['x']-25, tank['y']-15,
            tank['x']+25, tank['y']+15,
            fill=tank['color'], outline='black', width=2
        )
        
        # Barrel tank
        barrel_length = 30
        self.canvas.create_line(
            tank['x'], tank['y'],
            tank['x'] + (barrel_length * direction), tank['y'],
            width=4, fill='black'
        )
        
        # Nama hero
        self.canvas.create_text(
            tank['x'], tank['y']-30,
            text=tank['hero'].name,
            font=('Arial', 10, 'bold')
        )
    
    def draw_health_bar(self, tank):
        hero = tank['hero']
        width = 50
        height = 5
        fill_width = (hero.health / hero.max_health) * width
        
        # Background bar
        self.canvas.create_rectangle(
            tank['x']-width//2, tank['y']-25,
            tank['x']+width//2, tank['y']-20,
            fill='gray'
        )
        
        # Fill bar
        color = 'green' if tank['color'] == 'blue' else 'red'
        self.canvas.create_rectangle(
            tank['x']-width//2, tank['y']-25,
            tank['x']-width//2 + fill_width, tank['y']-20,
            fill=color
        )
    
    def key_press(self, event):
        # Gerakan player (WASD)
        move_speed = 8
        
        if event.char.lower() == 'a':
            self.player_tank['x'] -= move_speed
        elif event.char.lower() == 'd':
            self.player_tank['x'] += move_speed
        elif event.char.lower() == 'w':
            self.player_tank['y'] -= move_speed
        elif event.char.lower() == 's':
            self.player_tank['y'] += move_speed
        elif event.char.lower() == ' ':
            self.fire_bullet(self.player_tank, direction=1, color='gold')
        
        # Batasi gerakan dalam canvas
        self.player_tank['x'] = max(25, min(775, self.player_tank['x']))
        self.player_tank['y'] = max(25, min(575, self.player_tank['y']))
        
        self.draw_game_elements()
    
    def fire_bullet(self, tank, direction, color):
        # Tambahkan efek recoil
        recoil = 5
        tank['x'] -= recoil * direction
        
        self.bullets.append({
            'x': tank['x'] + (35 * direction),
            'y': tank['y'],
            'speed': 15 * direction,
            'owner': tank['color'],
            'power': tank['hero'].attack_power,
            'color': color
        })
    
    def ai_behavior(self):
        self.ai_move_counter += 1
        move_speed = 5
        
        # AI movement logic
        if self.ai_move_counter % 15 == 0:
            # 60% chance untuk mendekati player
            if random.random() < 0.6:
                if self.player_tank['x'] < self.ai_tank['x']:
                    self.ai_tank['x'] -= move_speed
                else:
                    self.ai_tank['x'] += move_speed
                
                if self.player_tank['y'] < self.ai_tank['y']:
                    self.ai_tank['y'] -= move_speed
                else:
                    self.ai_tank['y'] += move_speed
            else:  # 40% chance untuk gerakan random
                direction = random.choice(['left', 'right', 'up', 'down'])
                if direction == 'left':
                    self.ai_tank['x'] -= move_speed
                elif direction == 'right':
                    self.ai_tank['x'] += move_speed
                elif direction == 'up':
                    self.ai_tank['y'] -= move_speed
                elif direction == 'down':
                    self.ai_tank['y'] += move_speed
        
        # AI shooting logic
        if self.ai_move_counter % 30 == 0 and random.random() < 0.4:
            self.fire_bullet(self.ai_tank, direction=-1, color='orange')
        
        # Batasi gerakan AI
        self.ai_tank['x'] = max(25, min(775, self.ai_tank['x']))
        self.ai_tank['y'] = max(25, min(575, self.ai_tank['y']))
    
    def calculate_damage(self, attacker, defender):
        # Rumus damage dengan faktor random dan pertahanan
        base_damage = max(1, attacker.attack_power * random.uniform(0.8, 1.2))
        defense_reduction = defender.defense_power * 0.5
        final_damage = max(1, base_damage - defense_reduction)
        return int(final_damage)
    
    def update_bullets(self):
        bullets_to_remove = []
        
        for bullet in self.bullets:
            bullet['x'] += bullet['speed']
            
            # Cek tabrakan dengan tank lawan
            if bullet['owner'] == 'blue':
                target = self.ai_tank
                target_hero = self.ai_hero
            else:
                target = self.player_tank
                target_hero = self.player_hero
            
            if (target['x']-25 <= bullet['x'] <= target['x']+25 and
                target['y']-15 <= bullet['y'] <= target['y']+15):
                
                damage = self.calculate_damage(
                    self.player_hero if bullet['owner'] == 'blue' else self.ai_hero,
                    target_hero
                )
                
                target_hero.health -= damage
                bullets_to_remove.append(bullet)
                
                # Update health display
                self.update_health_display()
                
                # Cek jika game over
                if target_hero.health <= 0:
                    self.game_over(bullet['owner'])
                    return
            
            # Hapus bullet jika keluar layar
            if bullet['x'] < 0 or bullet['x'] > 800:
                bullets_to_remove.append(bullet)
        
        # Hapus bullet yang perlu dihapus
        for bullet in bullets_to_remove:
            if bullet in self.bullets:
                self.bullets.remove(bullet)
    
    def update_health_display(self):
        self.health_bars['player'].config(
            text=f"{self.player_hero.health}/{self.player_hero.max_health} HP",
            fg='green' if self.player_hero.health > self.player_hero.max_health/4 else 'red'
        )
        
        self.health_bars['ai'].config(
            text=f"{self.ai_hero.health}/{self.ai_hero.max_health} HP",
            fg='green' if self.ai_hero.health > self.ai_hero.max_health/4 else 'red'
        )
    
    def game_over(self, winner_color):
        if winner_color == 'blue':
            winner = self.player_hero.name
            message = "Anda Menang!"
        else:
            winner = self.ai_hero.name
            message = "AI Menang!"
        
        messagebox.showinfo(
            "Game Over", 
            f"{winner} {message}\n\n"
            f"Player HP: {self.player_hero.health}/{self.player_hero.max_health}\n"
            f"AI HP: {self.ai_hero.health}/{self.ai_hero.max_health}"
        )
        
        self.root.destroy()
    
    def game_loop(self):
        self.ai_behavior()
        self.update_bullets()
        self.draw_game_elements()
        self.root.after(30, self.game_loop)

# Jalankan game
root = tk.Tk()
game = TankGame(root)
root.mainloop()
