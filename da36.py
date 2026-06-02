#імпортуємо бібліотеки
import pandas as pd
import numpy as np
#ствоюємо таблицю
df = pd.DataFrame ({
    'Ім\'я': ['Олена', 'Ігор', 'Дмитро'],
    'Вік': [25, 30, 42]
})
print(df.head)
