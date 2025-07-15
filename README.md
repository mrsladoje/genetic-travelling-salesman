# Rešenje Problema Trgovačkog Putnika pomoću Genetskog Algoritma

## Pregled Projekta

Ovaj projekat implementira **Genetski algoritam (GA)** za rešavanje **Problema putujućeg trgovca (TSP)** koristeći Python. TSP je klasičan problem optimizacije gde trgovac mora da poseti sve gradove tačno jednom i vrati se u početni grad, minimizirajući ukupnu distancu putovanja.

## Struktura Projekta

```
genetic-travelling-salesman/
├── main.py                   # Glavna datoteka i testiranje
├── .env.py                   # Parametri konfiguracije (putanja ka testnom fajlu)
├── visualizer.py             # Modul za vizuelizaciju
├── models/                   # Osnovni modeli podataka
│   ├── city.py               # Reprezentacija grada
│   ├── route.py              # Reprezentacija rute/hromozoma
│   └── population.py         # Upravljanje populacijom
├── genetic/                  # Operacije genetskog algoritma
│   ├── selection.py          # Selekcija roditelja
│   ├── crossover.py          # Ukrštanje
│   └── mutation.py           # Mutacija
├── repository/               # Sloj za pristup podacima
│   └── reader.py             # Čitanje datoteka
└── test_cases/               # Test podaci
    └── data_tsp.txt          # 52 grada sa koordinatama
```

## Implementacija Genetskog Algoritma

### 1. Selekcija - Tournament Selection

```python
def tournament_selection(population, tournament_size=5):
    actual_tournament_size = min(tournament_size, len(population.routes))
    tournament = random.sample(population.routes, actual_tournament_size)
    return min(tournament, key=lambda x: x.distance)
```

**Algoritam:**
- Nasumično bira `tournament_size` jedinki
- Vraća najbolju jedinku (najmanja distanca)
- Obezbeđuje selekcijski pritisak uz održavanje raznovrsnosti

### 2. Ukrštanje - Partially Mapped Crossover (PMX)

```python
def partially_mapped_crossover(parent1, parent2):
    # Bira nasumični segment
    start = random.randint(0, len(route1) - 2)
    end = random.randint(start + 1, len(route1))
    
    # Kopira segment od roditelja 1
    child_route[start:end] = route1[start:end]
    
    # Kreira mapiranje i rešava konflikte
    # ... logika mapiranja ...
    
    return Route(parent1.cities, child_route)
```

**Algoritam:**
1. Bira nasumični segment od Roditelja 1
2. Kopira segment u dete
3. Kreira mapiranje za konfliktne elemente
4. Popunjava preostale pozicije bez duplikata

### 3. Mutacija - Inversion Mutation

```python
def inversion_mutation(route, mutation_rate=0.1):
    if random.random() < mutation_rate:
        # Bira nasumični segment
        start = random.randint(0, len(mutated_route) - 2)
        end = random.randint(start + 1, len(mutated_route))
        
        # Obrće segment
        mutated_route[start:end] = reversed(mutated_route[start:end])
        
        return Route(route.cities, mutated_route)
    return route
```

**Algoritam:**
1. Bira nasumični segment rute
2. Obrće redosled gradova u segmentu
3. Kreira novu rutu sa mutiranim redosledom

### 4. Evolucioni Proces

```python
def evolve(self, mutation_rate=0.1, elite_size=10):
    new_routes = []
    
    # Elitizam: čuva najbolje jedinke
    self.sort_by_distance()
    new_routes.extend(self.routes[:elite_size])
    
    # Generiše potomke
    while len(new_routes) < self.population_size:
        parent1 = tournament_selection(self)
        parent2 = tournament_selection(self)
        
        child = partially_mapped_crossover(parent1, parent2)
        child = inversion_mutation(child, mutation_rate)
        
        new_routes.append(child)
    
    self.routes = new_routes
    self.generation += 1
    self.update_statistics()
```

## Strukture Podataka

### Format Ulaznih Podataka
```
1 565.0 575.0
2 25.0 185.0
3 345.0 750.0
...
52 1740.0 245.0
```

### Reprezentacija Rute
```python
route = [1, 3, 7, 2, 5, 4, 6, 8, ...]  # ID-jevi gradova u redosledu posete
```

## Modul za Vizuelizaciju

### Funkcionalnosti
Modul `visualizer.py` pruža sveobuhvatne mogućnosti vizuelizacije:

#### 1. Grafik Distribucije Gradova

#### 2. Vizuelizacija Rute

#### 3. Rute Populacije

#### 4. Analiza Konvergencije



### Prednosti Algoritma
1. **Rešenje**: Pravilno rešava TSP ograničenja
2. **Skalabilnost**: Radi sa različitim brojem gradova
3. **Konfigurisanje**: Podesivi parametri
4. **Vizuelizacija**: Sveobuhvatno crtanje
5. **Statistično Praćenje**: Statistika performansi
