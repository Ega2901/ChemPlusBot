# ChemPlusBot

https://miro.com/welcomeonboard/UXllcTFHZDR5S1hUeTlDMFJPV1dvNVFtUkNQdEQ0ZnZvWmIwQWlEdDZuS1VlbWdYTEw2bjI1RnZ1UWoyQkVocXwzNDU4NzY0NTcwOTk4MDE3NDg4fDI=?share_link_id=579654662729

**Bold**
# First
## Second
### Third

#Запуск
#### После клонирования репозитория на локальную машину, убедиться что установлена система Docker и выполнен вход, внутри репозитория выполнить сборку и запуск контейнера 
Сборка:
```bash
docker build chemplusbot
```
Запуск:
```bash
docker run -d -p 8080:80 chemplusbot
```

Убедитесь что в файле .env записан токен авторизации Telegram Api
