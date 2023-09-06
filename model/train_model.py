from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pickle

# Загрузка данных
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2)

# Обучение модели
clf = LogisticRegression()
clf.fit(X_train, y_train)

# Сохранение модели
with open('model.pkl', 'wb') as model_file:
    pickle.dump(clf, model_file)
