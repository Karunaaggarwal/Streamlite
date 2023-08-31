import streamlit as st
def find_largest(num1, num2, num3):
  return max(num1, num2, num3)
  
def main():
  st.title("Find the Largest Number")
  num1 = st.number_input("Enter the First number:")
  num2 = st.number_input("Enter the Second number:")
  num3 = st.number_input("Enter the Third number:")
  if st.button("Find Largest"):
    largest = find_largest(num1, num2, num3)
    st.write(f"The largest number is: {largest}")
    
if __name__ == "__main__":
  main()
