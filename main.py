import streamlit as st
import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt

st.title("Conociendo el desempeño de los colaboradores del área de Marketing de Socialize your Knowledge")
st.write("Este dashboard proporciona un análisis detallado del desempeño de los empleados de la empresa. Utilizando una base de datos de información de los colaboradores, se presentan gráficos y estadísticas para identificar las fortalezas y áreas de mejora de cada uno. Con esta herramienta, los empleados pueden monitorear su rendimiento y tomar medidas para mejorarlo.")

# Cargar la base de datos
data = pd.read_csv("employee_data.csv")

# Desplegar el logotipo de la empresa
st.sidebar.image('logo.png', width=150)

# Desplegar sidebar
st.sidebar.title("Filtros y Selectores")

# Desplegar un control para seleccionar el género del empleado
gender_options = st.sidebar.selectbox('Seleccione el género del empleado', data['gender'].unique())
#data = data[data['gender'] == gender_options]

# Desplegar un control para seleccionar un rango del puntaje de desempeño del empleado
performance_options = st.sidebar.slider('Seleccione el rango del puntaje de desempeño del empleado', 1, 5, (1, 5))
data = data[(data['performance_score'] >= performance_options[0]) & (data['performance_score'] <= performance_options[1])]

# Desplegar un control para seleccionar el estado civil del empleado
marital_options = st.sidebar.selectbox('Seleccione el estado civil del empleado', data['marital_status'].unique())
data = data[data['marital_status'] == marital_options]

# Gráfico para visualizar la distribución de los puntajes de desempeño
fig1, x1 = plt.subplots()
x1 = plt.hist(data['performance_score'], bins=5)
plt.xlabel('Puntaje de desempeño')
plt.ylabel('Numero de empleados')
plt.title('Distribución de los puntajes de desempeño')
st.pyplot(fig1)

# Gráfico para visualizar el promedio de horas trabajadas por el género del empleado
# data_grouped = data.groupby('gender').mean()
#fig2, x2 = plt.subplots()
data_grouped = data.groupby('gender').mean(numeric_only=True)
data_grouped.reset_index(inplace=True)
data_grouped.plot.bar(x='gender', y='average_work_hours', rot=0)
plt.xlabel('Género')
plt.ylabel('Promedio de horas trabajadas')
plt.title('Promedio de horas trabajadas por el género del empleado')
st.pyplot()

# Gráfico para visualizar la edad de los empleados con respecto al salario de estos
fig3, x3 = plt.subplots()
x3 = plt.scatter(data['age'], data['salary'])
plt.xlabel('Edad')
plt.ylabel('Salario')
plt.title('Edad de los empleados con respecto al salario')
st.pyplot(fig3)

# Gráfico para visualizar la relación del promedio de horas trabajadas versus el puntaje de desempeño
fig4, x4 = plt.subplots()
x4 = plt.scatter(data['average_work_hours'], data['performance_score'])
plt.xlabel('Promedio de horas trabajadas')
plt.ylabel('Puntaje de desempeño')
plt.title('Relación del promedio de horas trabajadas versus el puntaje de desempeño')
st.pyplot(fig4)

# Conclusión sobre el análisis mostrado en la aplicación web
st.markdown('En base a los datos mostrados en los gráficos y estadísticas, se pueden observar las siguientes conclusiones: '
            '- Los puntajes de desempeño no se distribuyen de manera equitativa entre los empleados, concentrándose la mayor parte en el puntaje de desempeño 3. '
            '- El promedio de horas trabajadas por los empleados es similar tanto para hombres como para mujeres. '
            '- La edad de los empleados no parece estar relacionada de manera significativa con el salario que reciben. '
            '- Se observa una relación clara entre el promedio de horas trabajadas y el puntaje de desempeño de los empleados. ')