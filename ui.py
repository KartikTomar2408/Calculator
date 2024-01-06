from backend import *
import streamlit 
streamlit.title("Simple Calculator")
x=streamlit.number_input('Enter the first number ')
y=streamlit.number_input('Enter the Second number ')
operation = streamlit.radio('Select your Calculating operation: ',
                  ('Addition', 'Substraction', 'Multiplication', 'Division'))
if (operation == 'Addition'):
    streamlit.text(f'operation used is {operation}, outpuut of the operation is:  {add(x,y)}')
if (operation == 'Substraction'):
   streamlit.text(f'operation used is {operation}, outpuut of the operation is:  {subs(x,y)}')
if (operation == 'Multiplication'):
    streamlit.text(f'operation used is {operation}, outpuut of the operation is:  {multiply(x,y)}')
if (operation == 'Division'):
    streamlit.text(f'operation used is {operation}, outpuut of the operation is:  {divide(x,y)}')
